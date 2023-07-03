from typing import Callable, List, Dict
from dataclasses import dataclass

import bs4

from tejos.players import players
from tejos import model
from tejos.util import fn

missing_file_name = '_temp/missing.py'


@dataclass
class Player:
    name: str
    player_module: Callable
    scores: List = None
    match_state: model.MatchState = None
    seed: str = None
    player_klass: model.Player = None

    def __post_init__(self):
        self.player_klass = players.search_player_by_name(self.name, self.player_module)
        if not self.player_klass:
            with open('_temp/missing.py', 'a') as missing_file:
                plyr_def = (f"{self.name} = Player('{self.name}', tour_symbol=TOUR, klass_name='{self.name}', alt_names=[])\n")
                print(plyr_def)
                missing_file.write(plyr_def)

    def player_entry_klass_name(self):
        return self.player_klass.klass_name

    def entry_definition(self):
        return f"{'':>12}({self.player_definition()}, {self._seed()}),\n"

    def score(self):
        """
        men.Medvedev, (6, 6, 6)
        """
        return f"{self.player_definition()}, ({', '.join(self.scores_to_string())})"

    def scores_to_string(self):
        return [str(s) for s in self.scores]

    def _seed(self):
        return f"'{self.seed}'" if self.seed else None

    def player_definition(self):
        return f"{self._player_mod_name()}.{self.player_entry_klass_name()}"

    def _player_mod_name(self):
        return self.player_module.__name__.split(".")[-1]

    def has_retired(self):
        return self if self.match_state == model.MatchState.RET else None

    def has_withdrawn(self):
        return self if self.match_state == model.MatchState.WITHDRAWN else None;



@dataclass
class MatchBlock:
    href: str
    match_id_fn: Callable
    round: int
    draw_attr_name: str
    player1: Player
    player2: Player
    json: Dict = None
    html: bs4.element.Tag = None
    match_number: int = None
    match_id: int = None

    def __post_init__(self):
        self.match_id = self.match_id_fn(self.href)
        return self

    def set_match_number_from_1(self, min_match):
        self.match_number = (self.match_id - min_match) + 1
        return self

    def __hash__(self):
        return hash((self.href,))

    def __eq__(self, other):
        return self.href == other.href

    def entry_format(self):
        return self.player1.entry_definition() + self.player2.entry_definition()

    def match_format(self):
        return f"{'':>12}({self.match_number}, {self.player1.player_definition()}, {self.player2.player_definition()}),  \n"

    def results_format(self, sp):
        """
        mens_singles.for_round(1).for_match(64).score(men.Seyboth_Wild, ()).score(men.Medvedev, ())
        :return:
        """
        return f"""{sp}({self._rd_and_match()}
{sp}.score({self.player1.score()})
{sp}.score({self.player2.score()}){self._has_retirement(sp)}{self._has_withdrawal(sp)}),

"""
        pass

    def _rd_and_match(self):
        return f"draw.for_round({self.round}).for_match({self.match_number})"

    def _has_retirement(self, sp):
        ret = fn.remove_none([pl.has_retired() for pl in [self.player1, self.player2]])
        if not ret:
            return ""
        return f"\n{sp}.retirement({ret[0].player_definition()})"

    def _has_withdrawal(self, sp):
        wd = fn.remove_none([pl.has_withdrawn() for pl in [self.player1, self.player2]])
        if not wd:
            return ""
        return f"\n{sp}.withdrawal({wd[0].player_definition()})"


    def has_result(self):
        return (self.player1.scores and self.player2.scores) or self._match_has_exception([self.player1, self.player2])

    def _match_has_exception(self, players: List):
        return any([self._player_has_match_exception(pl) for pl in players])

    def _player_has_match_exception(self, pl):
        return pl.has_retired() or pl.has_withdrawn()
