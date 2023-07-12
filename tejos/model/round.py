from typing import Callable, List
from functools import partial

from rich.console import Console
from rich.table import Table
from rich import box

from rdflib import URIRef

from tejos.model import match, entry, model
from tejos.repo import repository
from tejos.util import fn, error

console = Console()


class Round(model.GraphModel):
    repo = repository.RoundRepo
    repo_graph = model.GraphModel.tournament_graph
    repo_instance = None

    @classmethod
    def create(cls, round_id,
               number_of_slots,
               best_of,
               draw):
        rd = cls(round_id, number_of_slots, best_of, draw)
        rd.build_match_slots()
        cls.repository().upsert(rd)
        return rd

    @classmethod
    def init_add_rds_for_draw(cls, draw):
        return [cls.init_matches(draw, rd) for rd in cls.repository().get_all_for_draw(draw.subject)]

    @classmethod
    def add_match_state(cls, draw):
        return [cls.for_round(draw, rd) for rd in draw.rounds]

    @classmethod
    def init_matches(cls, draw, rd):
        sub, draw_name, rd_number, best_of, draw_sub, match_subs = rd
        rd = cls(round_id=rd_number, number_match_slots=len(match_subs), games_best_of=best_of, draw=draw, sub=sub)
        rd.build_match_slots()
        return rd

    @classmethod
    def for_round(cls, draw, rd):
        matches = match.Match.get_or_update_all_for_round(for_round=rd, round_sub=rd.subject, update_match=True)
        if not matches:
            return rd
        # rd.add_matches(matches)
        return rd


    def __init__(self,
                 round_id,
                 number_match_slots,
                 games_best_of,
                 draw,
                 sub: URIRef = None):
        self.number_match_slots = number_match_slots
        self.name = self.determine_round_of()
        self.round_id = round_id
        self.matches = []
        self.games_best_of = games_best_of
        self.draw = draw
        self.subject = URIRef(f"{self.draw.subject.toPython()}/Round/{self.round_id}") if not sub else sub

    def determine_round_of(self):
        if self.number_match_slots > 4:
            return f"Round of {self.number_match_slots * 2}"
        if self.number_match_slots == 4:
            return "QF"
        if self.number_match_slots == 2:
            return "SF"
        if self.number_match_slots == 1:
            return "F"
        breakpoint()

    def show(self):
        table = Table(title=f"Draw and Results for round {self.round_id}",
                      box=box.ROUNDED)

        table.add_column("Match", justify="center", style="cyan", no_wrap=True)
        table.add_column("Player1", justify="left", style="magenta")
        table.add_column("Player2", justify="left", style="green")

        for match in self.matches:
            match.show(table)

        console.print(table)

    def result_template(self, event_name):
        return [match.result_template(event_name, self.round_id) for match in self.matches]

    def fantasy_score_template(self, draw_fn_symbol, trim_team_draw=None, add_selected=False, features=None):
        return [self._fn_definition_for_result_template(draw_fn_symbol)] + [
            match.fantasy_score_template(draw_fn_symbol,
                                         self.round_id,
                                         trim_team_draw=trim_team_draw,
                                         add_selected=add_selected,
                                         features=features) for match in self.matches]

    def _fn_definition_for_result_template(self, fn_symbol):
        return f"def {fn_symbol}_round_{self.round_id}({fn_symbol}):"

    def add_winner_to_match(self, match_number, player):
        if len(self.matches) < match_number:
            raise error.ConfigException(f"Match number {match_number} over total matches {len(self.matches)}")

        mt = self._find_match(match_number)
        return mt.add_player(player)

    def build_match(self, match_number, player1: entry.Entry, player2: entry.Entry):
        mt = self._find_match(match_number)
        mt.add_players(player1, player2)
        return self

    def for_match(self, match_number):
        return self._find_match(match_number)

    def _find_match(self, match_number):
        mt = fn.find(partial(self._match_number_predicate, match_number), self.matches)
        if not mt:
            raise error.ConfigException
        return mt

    def build_match_slots(self):
        [self.add_match(self._match_constructor(match_number)) for match_number in
         range(1, self.number_match_slots + 1)]
        return self

    def add_match(self, for_match: match.Match):
        # if for_match.match_id == "1.1":
        #     breakpoint()
        self.matches.append(for_match)
        return self

    def add_matches(self, matches: List[match.Match]):
        breakpoint()
        self.matches = self.matches + matches
        return self

    def _match_constructor(self, match_number):
        mt = match.Match.create(round_id=self.round_id,
                                match_number=match_number,
                                draw=self.draw,
                                for_round=self)
        self.repository().add_match(self.subject, mt.subject)
        return mt

    def _match_number_predicate(self, number, match):
        return match.number == number

    def __repr__(self):
        cls_name = self.__class__.__name__
        components = [
            f"name={self.name}",
            f"round_id={self.round_id}",
            f"number_of_slots={self.number_match_slots}"]
        return f"{cls_name}({', '.join(fn.remove_none(components))})"

