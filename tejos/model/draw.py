from typing import Tuple, List, Union
from functools import partial, reduce
import math
from rdflib import URIRef, Graph, RDF, Literal

from . import round, match
from tejos.model import tournament_event, player, entry, errors, model
from tejos.fantasy import points_strategy
from tejos.repo import repository

from tejos.rdf import rdf_prefix
from tejos.util import fn, error, echo, logger


def find_draw(draw_name, draws):
    return fn.find(partial(_draw_name_predicate, draw_name), draws)


def find_draw_by_cls(draw_cls, draws):
    return fn.find(partial(_draw_cls_predicate, draw_cls), draws)


def _draw_name_predicate(draw_name, draw):
    return draw_name == draw.name


def find_entry_for_player(for_player: player.Player, entries: List[entry.Entry]):
    return fn.find(partial(_entry_player_predicate, for_player), entries)


def _entry_player_predicate(for_player, entry):
    return entry.player() == for_player


def _draw_cls_predicate(draw_cls, draw):
    return isinstance(draw, draw_cls)


class Draw(model.GraphModel):
    repo = repository.DrawRepo
    repo_graph = model.GraphModel.tournament_graph
    repo_instance = None

    @classmethod
    def create(cls, name: str, best_of: int, draw_size: int, event, points_strategy_components: tuple = None):
        draw = cls(name=name,
                   best_of=best_of,
                   event=event,
                   points_strategy_components=points_strategy_components).draw_size(number_of_matches=draw_size)
        cls.repository().upsert(draw)
        return draw

    @classmethod
    def get_all_for_event(cls, event):
        return [cls.build_draw_and_add_to_event(draw, event) for draw in
                cls.repository().get_for_event(event_subject=event.subject)]

    @classmethod
    def get(cls, event, name: str):
        result = cls.repository().get(event_subject=event.subject, name=name)
        if not result:
            return None
        return cls.build_draw_and_add_to_event(result, event)

    @classmethod
    def build_draw_and_add_to_event(cls, result, for_event):
        name, best_of, draw_size, sub, fantasy_pts, event_sub = result
        event = tournament_event.TournamentEvent.get_by_sub(event_sub) if not for_event else for_event
        draw = cls(name=name, best_of=best_of, points_strategy_components=fantasy_pts, sub=sub, event=event)
        draw.entries = entry.Entry.get_all_entries_for_draw(draw)
        event.has_draw(draw)
        draw.draw_size(draw_size)  # builds the rounds and draws
        draw.load_rounds()
        return draw

    def __init__(self,
                 name,
                 best_of,
                 event: tournament_event.TournamentEvent,
                 points_strategy_components: Union[tuple, URIRef] = None,
                 sub: URIRef = None):
        self.name = name
        self.number_of_matches = None
        self.best_of = best_of
        self.rounds = []
        self.tournament = event
        self.entries = []
        self.errors = []
        self.points_strategy = self.fantasy_strategy(points_strategy_components)
        self.fn_symbol = "mens_singles" if self.name == 'MensSingles' else "womens_singles"
        self.round_factor_strategy = None
        self.subject = URIRef(f"{self.tournament.subject.toPython()}/{self.name}") if not sub else sub

    def __hash__(self):
        return hash((self.name,))

    def __eq__(self, other):
        return self.name == other.name

    def fantasy_strategy(self, components: Union[Tuple, URIRef] = None):
        if components:
            return points_strategy.PointsStrategyCalculator.build(components)
        return points_strategy.strategy_2_1_point5_double()

    def draw_size(self, number_of_matches):
        self.number_of_matches = number_of_matches
        self.repo(self.__class__.tournament_graph()).update_draw_size(self)
        return self

    def load_rounds(self):
        logger.log(f"Load Draw: {self.name}")
        self.rounds = round.Round.init_add_rds_for_draw(self)
        round.Round.add_match_state(self)
        return self

    def init_draw(self):
        """
        Creates an empty set of rounds an matches
        """
        if not self.number_of_matches:
            breakpoint()
        self._build_draw(1, self.number_of_matches)
        return self

    def fantasy_points_strategy(self, points_strategy):
        self.points_strategy = points_strategy
        return self

    def fantasy_round_points_accum_strategy(self, accum_strat):
        self.round_factor_strategy = accum_strat
        return self

    def add_entries(self, players: List[player.Player]):
        [self.has_entry(player_entry, seed) for player_entry, seed in players]
        return self

    def has_entry(self, player_entry: player.Player, seed: int):
        en = entry.Entry.create(player_entry, draw=self, seed=seed)
        if en in self.entries:
            return self
        self.entries.append(en)
        return self

    def first_round_draw(self, match_ups):
        if len(match_ups) != self.number_of_matches:
            er = errors.ConfigError(type_of_error=errors.TypeOfError.INITIALISAION,
                                    error_severity=errors.ErrorSeverity.FATAL,
                                    message_fn=errors.entry_mismatch_on_initialise_draw)
            self.errors.append(er)
            echo.echo(er.message_fn(self.name))
            return self
        logger.log(f"Create First round for {self.name}")
        [self._place_in_first_round(match_up) for match_up in match_ups]
        return self

    def for_round(self, round_id):
        rd = fn.find(partial(self._round_number_predicate, round_id), self.rounds)
        if not rd:
            raise error.ConfigException(f"Round id: {round_id} does not exist")
        return rd

    def advance_winner(self, for_match):
        rd_id, mt_id = match.split_match_id(for_match.match_id)
        if len(self.rounds) < rd_id + 1:
            # we are finished
            echo.echo(f"Draw Finished: Winner {for_match.winner().player().name}")
            return self
        next_rd_match_number = self._next_rd_match_number(rd_id, mt_id)
        return self.for_round(rd_id + 1).add_winner_to_match(next_rd_match_number, for_match.winner())

    def fantasy_points_schedule(self, rd_number):
        return self.points_strategy.calc_points_schedule(self.number_of_matches)

    def fantasy_points_allocation(self, rd_number):
        return self.points_strategy.explain_points_for_round(rd_number)

    def _next_rd_match_number(self, rd_id, this_rd_match_number):
        if len(self.rounds[rd_id].matches) == 1:
            return 1
        return math.ceil(this_rd_match_number / 2)

    def _build_draw(self, round_id, number_of_slots):
        """
        recursiving build the draw
        """
        self.rounds.append(round.Round.create(round_id,
                                              number_of_slots,
                                              self.best_of,
                                              self))
        if number_of_slots == 1:
            return self
        self._build_draw(round_id + 1, int(number_of_slots / 2))

    def _place_in_first_round(self, match_up: Tuple[int, player.Player, player.Player]):
        match_number, player1, player2 = match_up
        rd1 = self.for_round(1)
        if not rd1:
            breakpoint()
        rd1.build_match(match_number, self._player_to_entry(player1), self._player_to_entry(player2))
        return self

    def _player_to_entry(self, for_player: player.Player) -> entry.Entry:
        player_entry = find_entry_for_player(for_player, self.entries)
        if not player_entry:
            breakpoint()
            raise error.ConfigException(f"Player {for_player.name} is not in the draw")
        return player_entry

    def _round_number_predicate(self, number, round):
        return round.round_id == number

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name})"


class MensSingles(Draw):
    fn_symbol = "mens_singles"


class WomensSingles(Draw):
    fn_symbol = "womens_singles"
