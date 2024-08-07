from typing import Callable, Tuple, List
import math
from enum import Enum

from rdflib import URIRef

from . import player, set, entry, draw, feature, base
from tejos.presenter import console
from tejos.util import fn, error, echo, logger
from tejos import rdf
from tejos.repo import repository


class MatchState(Enum):
    RET = 'retired'
    WITHDRAWN = 'withdrawn'
    WALKOVER = 'walkover'


def split_match_id(match_id):
    return [int(ident) for ident in match_id.split(".")]


class Match():
    repo = base.GraphModel2().new(repository.MatchRepo, base.GraphModel2.tournament_graph)

    @classmethod
    def create(cls, round_id, match_number, draw, for_round):
        mt = cls(round_id, match_number, draw, for_round)
        cls.repo().upsert(mt)
        return mt

    @classmethod
    def get_or_update_all_for_round(cls, for_round, round_sub, update_match=True):
        matches = cls.repo().get_all_for_round(round_sub)
        return [cls.to_match(for_round, match, update_match) for match in matches]

    @classmethod
    def to_match(cls, for_round, match, update_match=True):
        (sub,
         _match_sub,
         _match_id,
         match_number,
         pos1_sub,
         pos2_sub,
         winner,
         scores1,
         scores2,
         retired_player_sub,
         withdrawn_player_sub,
         walkover_player_sub) = match
        if not update_match:
            mt = cls(round_id=for_round.round_id,
                     match_number=match_number,
                     draw=for_round.draw,
                     for_round=for_round,
                     sub=sub)
        else:
            mt = for_round.for_match(match_number)

        # if match_number == 25 and for_round.round_id == 2:
        #     breakpoint()
        entries = entry.Entry.get_by_subs([pos1_sub, pos2_sub])
        if entries and len(entries) == 2:
            mt.add_players(*entries)
        if entries and len(entries) == 1:
            mt.add_player(player_to_add=entries[0])

        if retired_player_sub:
            mt.entry_retirement = entry.Entry.find_or_get(retired_player_sub)
            mt.allow_equal_games_in_set = True
        mt.entry_withdrawal = entry.Entry.find_or_get(withdrawn_player_sub) if withdrawn_player_sub else None
        mt.entry_walkover = entry.Entry.find_or_get(walkover_player_sub) if walkover_player_sub else None

        if scores1:
            mt.load_score(position1_subject_sets=scores1)
        if scores2:
            mt.load_score(position2_subject_sets=scores2)
        return mt

    @classmethod
    def decompose_match_subject(cls, match_sub):
        draw_name, _, for_round, _, match_id = match_sub.split("/")[-5:]
        return (draw_name, int(for_round), int(match_id.split(".")[-1]))

    def __init__(self,
                 round_id,
                 match_number,
                 draw,
                 for_round,
                 sub: URIRef = None,
                 entry_retirement=None,
                 entry_withdrawal=None,
                 entry_walkover=None):
        self.number = match_number
        self.match_id = f"{round_id}.{match_number}"
        self.draw = draw
        self.for_round = for_round
        self.best_of = for_round.games_best_of
        self.round_subject = for_round.subject
        self.subject = URIRef(f"{self.round_subject.toPython()}/Match/{self.match_id}") if not sub else sub
        self.player1 = None
        self.player2 = None
        self.scores = None
        self.sets = []
        self.match_winner = None
        self.entry_retirement = None
        self.entry_withdrawal = None
        self.entry_walkover = None
        self.allow_equal_games_in_set = False if not self.entry_withdrawal else True

    def __repr__(self):
        cls_name = self.__class__.__name__
        components = [
            f"match_winner={self.match_winner}",
            f"player1={self.player1.player()}" if self.player1 else "player1=None",
            f"player2={self.player2.player()}" if self.player2 else "player2=None",
            f"entry_retirement={self.entry_retirement.player()}" if self.entry_retirement else None,
            f"entry_withdrawal={self.entry_withdrawal.player()}" if self.entry_withdrawal else None,
            f"entry_walkover={self.entry_walkover.player()}" if self.entry_walkover else None]
        return f"{cls_name}(match_id='{self.match_id}', {', '.join(fn.remove_none(components))})"

    def show(self, table):
        table.add_row(self.match_id,
                      f"{self.show_player(self.player1)}",
                      f"{self.show_player(self.player2)}")

    def match_block(self):
        return f"{self.show_player(self.player1)}\n{self.show_player(self.player2)}"

    def show_player(self, for_entry: entry.Entry):
        if not for_entry:
            return "?"
        return f"{self.player_and_seed(for_entry)} {self.show_set_and_winner(for_entry)}"

    def player_and_seed(self, for_entry):
        if not for_entry:
            return "TBD"
        return f"({for_entry.seeding()}) {for_entry.player().name}"

    def player_klass_and_seed(self, for_entry):
        if not for_entry:
            return "TBD"
        return f"({for_entry.seeding()}) {for_entry.player().klass_name}"

    def show_set_and_winner(self, for_player: entry.Entry):
        if not self.is_finished():
            return ""
        chevon = "<" if for_player == self.match_winner else ""
        ret = "(RET)" if self.entry_retirement == for_player else ""
        wd = "(WD)" if self.entry_withdrawal == for_player else ""
        wo = "(WO)" if self.entry_walkover == for_player else ""
        return f"{' '.join([str(s) for s in self.scores[for_player]])} {ret}{wd}{wo}  {chevon}"

    def result_template(self, event_name, round_number):
        match_part = f"{event_name}.for_round({round_number}).for_match({self.number})"
        mod_nm = event_name.split("_")[0][0:-1]
        if self.has_draw():
            score_part = f"score({mod_nm}.{self.player1.player().klass_name}, ()).score({mod_nm}.{self.player2.player().klass_name}, ())"
        else:
            score_part = f"score(?, ()).score(?, ())"
        return f"{match_part}.{score_part}"

    def fantasy_score_template(self, event_name, round_number, fmt=None, trim_team_draw=None, add_selected=False,
                               features=None):
        """
        TeamBearNecessities.draw(mens_singles).match("1.1").winner(Khachanov).in_sets(5)
        """
        mod = 'men' if event_name == "mens_singles" else "women"
        entries = f"{self.player_and_seed(self.player1)}  OR  {self.player_and_seed(self.player2)}"
        if fmt == "csv":
            return [
                event_name,
                self.match_id,
                f"{self.player1.player().klass_name}  {self.player2.player().klass_name}",
                None,
                entries
            ]
        if trim_team_draw.match(self.match_id).has_made_selection() and not add_selected:
            return ""
        # if trim_team_draw.team.name == "Team Clojo" and self.match_id == '4.7':
        #     breakpoint()
        if trim_team_draw.match(self.match_id).has_made_selection() and add_selected:
            return self._template_with_selection(event_name, trim_team_draw, entries, mod)

        if feature.FantasyFeature.PlayerNumberSelector not in features:
            return f"{'':>4}TEAM.draw({event_name}).match('{self.match_id}').winner({mod}).in_sets()  # {entries}"

        # TEAM.draw(mens_singles, '3.16').matchup(1, men.Wawrinka, 2, men.Djokovic).select(2).in_sets(3)
        pl1 = f"1, {mod}.{self.player1.player().klass_name}" if self.player1 else "1, None"
        pl2 = f"2, {mod}.{self.player2.player().klass_name}" if self.player2 else "2, None"
        return f"{'':>4}TEAM.draw({event_name}, '{self.match_id}').matchup({pl1}, {pl2}).select()  # {entries}"

    def _template_with_selection(self, event_name, team_draw, entries, mod):
        sel = team_draw.match(self.match_id)
        sel_winner = sel.selected_winner.player().klass_name
        sel_sets = sel.in_number_sets
        return f"{'':>4}TEAM.draw({event_name}).match('{self.match_id}').winner({mod}.{sel_winner}).in_sets({sel_sets})  # {entries}"

    def find_player_by_player(self, for_player: player.Player, raise_error: bool = True):
        if not self.has_draw():
            err = error.ConfigException(
                f"Match {self.match_id} has no draw when trying to find player {for_player.name}")
            if not raise_error:
                return err
            raise err
        pl = entry.find_player_from_entry(for_player, [self.player1, self.player2])
        if not pl:
            err = error.ConfigException(f"{for_player.name} is either not found or is not in Match: {self.match_id}")
            if not raise_error:
                return err
            raise err
        return pl

    def player_from_player_name(self, player_name, raise_error: bool = True):
        if not self.has_draw():
            err = error.ConfigException("No draw has been set for match")
            if not raise_error:
                return err
            raise err
        return entry.find_player_by_name(player_name, [self.player1, self.player2])

    def player_from_player_subject(self, player_sub, raise_error: bool = True):
        if not self.has_draw():
            err = error.ConfigException("No draw has been set for match")
            if not raise_error:
                return err
            raise err
        return entry.find_player_by_sub(player_sub, [self.player1, self.player2])

    def add_player(self, player_to_add: entry.Entry):
        if self.player1 and self.player2:
            if player_to_add in [self.player1, self.player2]:
                return self
            raise error.PlayerAdvanceError(
                f"Can't advance player, match {self.match_id} full with {self.player1.player().name} and {self.player2.player().name}")

        echo.echo(f"Add {player_to_add.player().name} to match {self.match_id}")

        if not self.player1:
            self.player1 = player_to_add
            self._init_scores(player_to_add)
        else:
            self.player2 = player_to_add
            self._init_scores(player_to_add)
        self.repo().add_players_to_match(self, (self.player1, self.player2))
        return self

    def add_players(self, player1: entry.Entry, player2: entry.Entry):
        """
        Add both players to the draw
        :param player1:
        :param player2:
        :return:
        """
        self.player1 = player1
        self._init_scores(player1)
        self.player2 = player2
        self._init_scores(player2)
        logger.log(f"Add Players to {self.match_id}; 1: {player1.player()} 2: {player2.player()}")
        self.repo().add_players_to_match(self, (player1, player2))
        return self

    def score(self, for_player, set_games: Tuple[int], possible_state_fn: Callable = None):
        if not self.player1 or not self.player2:
            breakpoint()
        if for_player == self.player1.player():
            pos_player = (1, self.player1)
        elif for_player == self.player2.player():
            pos_player = (2, self.player2)
        else:
            breakpoint()
        _pos, pl = pos_player


        if possible_state_fn == self.retirement:
            self.allow_equal_games_in_set = True

        self.update_sets(pl, set_games)

        self.repo().add_score(self, pos_player,
                              [self.set_game_subjects(for_set, score) for for_set, score in enumerate(set_games)])
        self.winner()
        return self

    def load_score(self, position1_subject_sets=None, position2_subject_sets=None):
        if position1_subject_sets:
            self.update_sets(self.player1, self.score_sbjects_to_score(position1_subject_sets))
        if position2_subject_sets:
            self.update_sets(self.player2, self.score_sbjects_to_score(position2_subject_sets))
        self.winner(advance=False)
        return self

    def update_sets(self, for_player: entry.Entry, set_games):
        if isinstance(set_games, int):
            breakpoint()
        self.scores[for_player] = set_games
        for set_number in range(len(set_games)):
            self.sets[set_number].result_for_player(for_player, set_games[set_number], self.allow_equal_games_in_set)
        # if "Fil" in for_player.player().name:
        #     breakpoint()
        return self

    def set_game_subjects(self, for_set, score):
        return rdf.SCORE + f"/{for_set + 1}/{score}"

    def score_sbjects_to_score(self, score_subjects: URIRef) -> Tuple[int]:
        return tuple(
            int(p) for _, p in sorted([tuple(sub.split('/')[-2:]) for sub in score_subjects], key=lambda s: s[0]))

    def retirement(self, retired_player):
        pl = draw.find_entry_for_player(retired_player, [self.player1, self.player2])
        self.entry_retirement = pl
        self.repo().add_retirement(self)
        self.winner()
        return self

    def withdrawal(self, wd_player):
        pl = draw.find_entry_for_player(wd_player, [self.player1, self.player2])
        self.entry_withdrawal = pl
        self.repo().add_withdrawal(self)
        self.winner()
        return self

    def walkover(self, wo_player):
        pl = draw.find_entry_for_player(wo_player, [self.player1, self.player2])
        self.entry_walkover = pl
        self.repo().add_walkover(self)
        self.winner()

    def number_of_sets_played(self):
        return len(fn.remove_none([s.winner for s in self.sets]))

    def max_sets_played(self):
        return self.best_of == self.number_of_sets_played() or self.entry_retirement or self.entry_withdrawal or self.entry_walkover

    def is_finished(self) -> bool:
        if not self.scores:
            return False
        if self.entry_retirement or self.entry_withdrawal or self.entry_walkover:
            return True
        set_winners = fn.remove_none([s.determine_winner(self.allow_equal_games_in_set) for s in self.sets])
        if not set_winners:
            return False
        return (max([set_winners.count(self.player1), set_winners.count(self.player2)])) >= math.ceil(self.best_of / 2)

    def has_draw(self):
        return self.player1 and self.player2

    def winner(self, advance: bool = True):
        if not self.is_finished():
            return None
        if self.match_winner:
            return self.match_winner

        self.match_winner = self._determine_winner()

        console.print(console.panel().fit(f"""Match {self.match_id} Winner {self.match_winner.player().name}

        {self.match_winner.player().name}: {self.show_set_and_winner(self.match_winner)}
        {self._losing_player().player().name}: {self.show_set_and_winner(self._losing_player())}
        """))

        if advance:
            # if self.match_id == "5.1":
            #     breakpoint()
            self.repo().add_match_winner(self)
            self.draw.advance_winner(self)
        return self.match_winner

    def _init_scores(self, for_player):
        if not self.scores:
            self.scores = {for_player: tuple()}
        else:
            self.scores[for_player] = tuple()
        if self.has_draw():
            self.sets = [set.Set(set_num, self.player1, self.player2) for set_num in range(1, self.best_of + 1)]
        return self

    def _losing_player(self):
        if not self.is_finished():
            return None
        if self.player1 == self.match_winner:
            return self.player2
        return self.player1

    def _determine_winner(self):
        if self.entry_retirement and self.player1 and self.player2:
            return self.player2 if self.entry_retirement == self.player1 else self.player1
        if self.entry_withdrawal and self.player1 and self.player2:
            return self.player2 if self.entry_withdrawal == self.player1 else self.player1
        if self.entry_walkover and self.player1 and self.player2:
            return self.player2 if self.entry_walkover == self.player1 else self.player1

        winners_by_sets = fn.remove_none([s.winner for s in self.sets])
        if winners_by_sets.count(self.player1) > winners_by_sets.count(self.player2):
            return self.player1
        return self.player2
