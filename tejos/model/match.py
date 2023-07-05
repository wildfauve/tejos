from typing import Callable, Tuple
import math
from enum import Enum

from . import player, set, entry, draw
from tejos.presenter import console
from tejos.util import fn, error, echo


class MatchState(Enum):
    RET = 'retired'
    WITHDRAWN = 'withdrawn'


def split_match_id(match_id):
    return [int(ident) for ident in match_id.split(".")]


class Match:
    def __init__(self, round_id, match_number, best_of, advance_winner_fn: Callable):
        self.number = match_number
        self.match_id = f"{round_id}.{match_number}"
        self.advance_winner_fn = advance_winner_fn
        self.best_of = best_of
        self.player1 = None
        self.player2 = None
        self.scores = None
        self.sets = []
        self.match_winner = None
        self.entry_retirement = None
        self.entry_withdrawal = None

    def __repr__(self):
        cls_name = self.__class__.__name__
        components = [
            f"match_winner={self.match_winner})",
            f"player1={self.player1.player()}",
            f"player2={self.player2.player()}",
            f"entry_retirement={self.entry_retirement.player()}" if self.entry_retirement else None,
            f"entry_withdrawal={self.entry_withdrawal.player()}" if self.entry_withdrawal else None]
        return f"{cls_name}(match_id='{self.match_id}', {', '.join(fn.remove_none(components))}"

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
        return f"{' '.join([str(s) for s in self.scores[for_player]])} {ret}{wd}  {chevon}"

    def result_template(self, event_name, round_number):
        match_part = f"{event_name}.for_round({round_number}).for_match({self.number})"
        mod_nm = event_name.split("_")[0][0:-1]
        if self.has_draw():
            score_part = f"score({mod_nm}.{self.player1.player().klass_name}, ()).score({mod_nm}.{self.player2.player().klass_name}, ())"
        else:
            score_part = f"score(?, ()).score(?, ())"
        return f"{match_part}.{score_part}"

    def fantasy_score_template(self, event_name, round_number, fmt=None):
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
        entries = f"{self.player_klass_and_seed(self.player1)}  OR  {self.player_klass_and_seed(self.player2)}"
        return f"{'':>4}TEAM.draw({event_name}).match('{self.match_id}').winner({mod}).in_sets()  # {entries}"

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

    def add_player(self, player_to_add: entry.Entry):
        if self.player1 and self.player2:
            raise error.PlayerAdvanceError(
                f"Can't advance player, match {self.match_id} full with {self.player1.player().name} and {self.player2.player().name}")

        echo.echo(f"Add {player_to_add.player().name} to match {self.match_id}")

        if not self.player1:
            self.player1 = player_to_add
            self._init_scores(player_to_add)
        else:
            self.player2 = player_to_add
            self._init_scores(player_to_add)
        return self

    def add_players(self, player1: entry.Entry, player2: entry.Entry):
        self.player1 = player1
        self._init_scores(player1)
        self.player2 = player2
        self._init_scores(player2)
        return self

    def score(self, for_player, set_games: Tuple[int]):
        pl = draw.find_entry_for_player(for_player, [self.player1, self.player2])
        self.scores[pl] = set_games
        [self.sets[set_number].result_for_player(pl, set_games[set_number]) for set_number in range(len(set_games))]
        self.winner()
        return self

    def retirement(self, retired_player):
        pl = draw.find_entry_for_player(retired_player, [self.player1, self.player2])
        self.entry_retirement = pl
        self.winner()
        return self

    def withdrawal(self, wd_player):
        pl = draw.find_entry_for_player(wd_player, [self.player1, self.player2])
        self.entry_withdrawal = pl
        self.winner()
        return self

    def number_of_sets_played(self):
        return len(fn.remove_none([s.winner for s in self.sets]))

    def max_sets_played(self):
        return self.best_of == self.number_of_sets_played() or self.entry_retirement or self.entry_withdrawal

    def is_finished(self) -> bool:
        if not self.scores:
            return False
        if self.entry_retirement or self.entry_withdrawal:
            return True
        set_winners = fn.remove_none([s.determine_winner() for s in self.sets])
        if not set_winners:
            return False
        return (max([set_winners.count(self.player1), set_winners.count(self.player2)])) >= math.ceil(self.best_of / 2)

    def has_draw(self):
        return self.player1 and self.player2

    def winner(self):
        if not self.is_finished():
            return None
        if self.match_winner:
            return self.match_winner
        self.match_winner = self._determine_winner()

        console.print(console.panel().fit(f"""Match {self.match_id} Winner {self.match_winner.player().name}

        {self.match_winner.player().name}: {self.show_set_and_winner(self.match_winner)}
        {self._losing_player().player().name}: {self.show_set_and_winner(self._losing_player())}
        """))

        self.advance_winner_fn(self)
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
        if self.entry_retirement:
            return self.player2 if self.entry_retirement == self.player1 else self.player1
        if self.entry_withdrawal:
            return self.player2 if self.entry_withdrawal == self.player1 else self.player1

        winners_by_sets = fn.remove_none([s.winner for s in self.sets])
        if winners_by_sets.count(self.player1) > winners_by_sets.count(self.player2):
            return self.player1
        return self.player2
