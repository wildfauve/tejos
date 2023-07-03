from typing import Callable
from functools import partial
from rich.console import Console
from rich.table import Table
from rich import box

from tejos.model import match, entry
from tejos.util import fn, error

console = Console()


class Round:
    def __init__(self, round_id, number_match_slots, games_best_of, advance_winner_fn: Callable):
        self.number_match_slots = number_match_slots
        self.name = f"Round of {number_match_slots}"
        self.round_id = round_id
        self.matches = []
        self.games_best_of = games_best_of
        self.advance_winner_fn = advance_winner_fn
        self._build_match_slots()

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

    def fantasy_score_template(self, draw_fn_symbol):
        return [self._fn_definition_for_result_template(draw_fn_symbol)] + [
            match.fantasy_score_template(draw_fn_symbol, self.round_id) for match in self.matches]

    def _fn_definition_for_result_template(self, fn_symbol):
        return f"\n\ndef {fn_symbol}_round_{self.round_id}({fn_symbol}):"

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

    def _build_match_slots(self):
        [self.matches.append(self._match_constructor(match_number)) for match_number in
         range(1, self.number_match_slots + 1)]
        return self

    def _match_constructor(self, match_number):
        return match.Match(self.round_id,
                           match_number,
                           self.games_best_of,
                           self.advance_winner_fn)

    def _match_number_predicate(self, number, match):
        return match.number == number
