from typing import Tuple, List
from functools import partial, reduce
import math
from rdflib import URIRef, Graph, RDF, Literal

from . import round, match
from tejos.model import tournament_event, player, entry, errors
from tejos.rdf import rdf_prefix
from tejos.util import fn, error, echo


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


class Draw:

    def __init__(self,
                 name,
                 fn_symbol,
                 best_of,
                 tournament: tournament_event.TournamentEvent):
        self.name = name
        self.fn_symbol = fn_symbol
        self.number_of_matches = None
        self.best_of = best_of
        self.rounds = []
        self.tournament = tournament
        self.entries = []
        self.errors = []
        self.points_strategy = None
        self.round_factor_strategy = None
        self.subject = URIRef(f"{self.tournament.subject.toPython()}/{self.name}")

    def build_graph(self, g: Graph):
        g.add((self.subject, RDF.type, rdf_prefix.fau_ten.Draw))
        g.add((self.subject, rdf_prefix.fau_ten.hasBestOfSets, Literal(self.best_of)))
        g.add((self.subject, rdf_prefix.fau_ten.hasInitialDrawSize, Literal(self.number_of_matches)))
        for e in self.entries:
            g.add((self.subject, rdf_prefix.fau_ten.hasQualifiedPlayer, e.subject))
            e.build_graph(g)
        return g

    def __hash__(self):
        return hash((self.name,))

    def __eq__(self, other):
        return self.name == other.name

    def draw_size(self, number_of_matches):
        self.number_of_matches = number_of_matches
        self._build_draw(1, number_of_matches)
        return self

    def fantasy_points_strategy(self, points_strategy):
        self.points_strategy = points_strategy
        return self

    def fantasy_round_points_accum_strategy(self, accum_strat):
        self.round_factor_strategy = accum_strat
        return self

    def add_entries(self, players):
        [self.has_entry(player_entry, seed) for player_entry, seed in players]
        return self

    def has_entry(self, player_entry: player.Player, seed: int):
        self.entries.append(entry.Entry(player_entry, draw=self, seed=seed))
        return self

    def init_draw(self, match_ups):
        if len(match_ups) != self.number_of_matches:
            er = errors.ConfigError(type_of_error=errors.TypeOfError.INITIALISAION,
                                    error_severity=errors.ErrorSeverity.FATAL,
                                    message_fn=errors.entry_mismatch_on_initialise_draw)
            self.errors.append(er)
            echo.echo(er.message_fn(self.name))
            return self
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
        # This is the next round
        # rd_id is indexed from 1, so next rd in rounds list is the same number
        return self.rounds[rd_id].add_winner_to_match(next_rd_match_number, for_match.winner())

    def fantasy_points_schedule(self, rd_number):
        return self.points_strategy.calc_points_schedule(self.number_of_matches)

    def fantasy_points_allocation(self, rd_number):
        return self.points_strategy.explain_points_for_round(rd_number)

    def _next_rd_match_number(self, rd_id, this_rd_match_number):
        if len(self.rounds[rd_id].matches) == 1:
            return 1
        return math.ceil(this_rd_match_number / 2)

    def _build_draw(self, round_id, number_of_slots):
        self.rounds.append(round.Round(round_id,
                                       number_of_slots,
                                       self.best_of,
                                       self.advance_winner))
        if number_of_slots == 1:
            return self
        self._build_draw(round_id + 1, int(number_of_slots / 2))

    def _place_in_first_round(self, match_up: Tuple[int, player.Player, player.Player]):
        match_number, player1, player2 = match_up
        self.rounds[0].build_match(match_number, self._player_to_entry(player1), self._player_to_entry(player2))
        return self

    def _player_to_entry(self, for_player: player.Player) -> entry.Entry:
        player_entry = find_entry_for_player(for_player, self.entries)
        if not player_entry:
            breakpoint()
            raise error.ConfigException(f"Player {for_player.name} is not in the draw")
        return player_entry

    def _round_number_predicate(self, number, round):
        return round.round_id == number


class MensSingles(Draw):
    pass


class WomensSingles(Draw):
    pass
