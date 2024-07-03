from typing import Callable, List, Dict
from dataclasses import dataclass

import bs4

from tejos import model
from tejos.util import fn

missing_file_name = '_temp/missing.csv'


@dataclass
class PlayerResult:
    name: str
    player_module: Callable
    scores: List = None
    match_state: model.MatchState = None
    seed: str = None
    player_klass: model.Player = None

    def __post_init__(self):
        # self.player_klass = players.search_player_by_name(self.name, self.player_module)
        self.player_klass = model.Player.load(name=self.name)
        if not self.player_klass:
            with open(missing_file_name, 'a') as missing_file:
                plyr_def = self.missing_player_csv_builder()
                plyr_def_rdf = self.missing_player_rdf_builder()
                print(plyr_def)
                missing_file.write(plyr_def_rdf)

    def missing_player_csv_builder(self):
        return f"{self.name},{self.player_module.TOUR}\n"

    def missing_player_rdf_builder(self):
        """
        clo-te-ind-plr:Todoni
        a                             clo-te:Player ;
        foaf:name                     "Anca Todoni" ;
        clo-te-plr:hasKlassName       "Todoni" ;
        clo-te-plr:hasTourDesignation "WTA" .
        """
        return f'''
        clo-te-ind-plr:{self.name}
        a                             clo-te:Player ;
        foaf:name                     "{self.name}" ;
        clo-te-plr:hasKlassName       "{self.name}" ;
        clo-te-plr:hasTourDesignation "{self.player_module.TOUR}" .\n\n
        '''


    def missing_player_klass_builder(self):
        return f"{self.name} = Player('{self.name}', tour_symbol=TOUR, klass_name='{self.name}', alt_names=[])\n"

    def player_entry_klass_name(self):
        return self.player_klass.klass_name

    def entry_definition(self):
        return f"{'':>12}({self.player_definition()}, {self._seed()}),\n"

    def score(self):
        """
        men.Medvedev, (6, 6, 6)
        """
        if len(self.scores) == 1:
            score_def = f"({self.scores[0]},)"
        else:
            score_def = f"({', '.join(self.scores_to_string())})"
        return f"{self.player_definition()}, {score_def}"

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
        return self if self.match_state == model.MatchState.WITHDRAWN else None

    def has_been_walkedover(self):
        # if self.match_state == model.MatchState.WALKOVER:
        #     breakpoint()
        return self if self.match_state == model.MatchState.WALKOVER else None


@dataclass
class MatchBlock:
    href: str
    match_id_fn: Callable
    round: int
    draw_attr_name: str
    draw_symbol: str
    player1: PlayerResult
    player2: PlayerResult
    event: model.TournamentEvent
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

    def save(self):
        # (draw.for_round(3).for_match(1)
        # .score(wta_players.Swiatek, (6, 7))
        # .score(wta_players.Martic, (2, 5))),
        # .retirement(atp_players.OneOfThePlayers)),

        match = self.event.find_draw_by_symbol(self.draw_symbol).for_round(self.round).for_match(self.match_number)
        if not self.no_score_walkover():
            match.score(self.player1.player_klass, tuple(self.player1.scores))
            match.score(self.player2.player_klass, tuple(self.player2.scores))
        if self.player1.match_state:
            self.add_state_to_match(match, self.player1)
        if self.player2.match_state:
            self.add_state_to_match(match, self.player2)
        pass

    def no_score_walkover(self):
        return self.player1.match_state == model.MatchState.WALKOVER or self.player2.match_state == model.MatchState.WALKOVER

    def add_state_to_match(self, match, player):
        if player.match_state == model.MatchState.RET:
            return match.retirement(player.player_klass)
        if player.match_state == model.MatchState.WITHDRAWN:
            return match.withdrawal(player.player_klass)
        if player.match_state == model.MatchState.WALKOVER:
            return match.walkover(player.player_klass)
        breakpoint()

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
        if len(self.player1.score()) == 1:
            breakpoint()
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
        return (self.player1.scores and self.player2.scores) or self._match_has_non_complete_state(
            [self.player1, self.player2])

    def _match_has_non_complete_state(self, players: List):
        return any([self._player_has_match_exception(pl) for pl in players])

    def _player_has_match_exception(self, pl):
        return pl.has_retired() or pl.has_withdrawn() or pl.has_been_walkedover()
