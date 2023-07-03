from typing import List, Union
from functools import partial
from rdflib import Graph, RDF, URIRef, Literal

from tejos.graph import rdf_prefix
from tejos.model import player
from tejos.util import fn, error


class Entry:
    """
    <https://fauve.io/ao/2023/entries/Aliassime>
    a                        fau-ten:QualifiedPlayer ;
    fau-ten:hasSeed          6 ;
    fau-ten:isInDraw         <https://fauve.io/ao/2023/mensSingles> ;
    fau-ten:isEntryForPlayer fau-ten-ind:Aliassime .
    """

    def __init__(self, player, draw, seed):
        self.is_entry_for_player = player
        self.is_in_draw = draw
        self.has_seed = seed
        self.subject = URIRef(f"{self.is_in_draw.subject.toPython()}/{self.is_entry_for_player.uri_name()}")

    def player(self):
        return self.is_entry_for_player

    def seeding(self):
        if not self.has_seed:
            return "   "
        return str(self.has_seed).rjust(3)


    def build_graph(self, g: Graph):
        g.add((self.subject, RDF.type, rdf_prefix.fau_ten.QualifiedPlayer))
        g.add((self.subject, rdf_prefix.fau_ten.hasSeed, Literal(self.has_seed)))
        g.add((self.subject, rdf_prefix.fau_ten.isEntryForPlayer, self.player().subject))
        return g


def find_player_from_entry(for_player: Union[Entry, player.Player], players: List[Entry]):
    predicate = _player_entry_predicate if isinstance(for_player, Entry) else _player_predicate
    pl = fn.find(partial(predicate, for_player), players)
    return pl


def find_player_by_name(player_name, players):
    pl = fn.find(partial(_player_name_predicate, player_name), players)
    if not pl:
        raise error.ConfigException(f"Player with name {player_name} not found")
    return pl


def _player_entry_predicate(player_to_find, player_entry):
    return player_to_find.player() == player_entry.player()

def _player_predicate(player_to_find: player.Player, player_entry: Entry):
    return player_to_find == player_entry.player()


def _player_name_predicate(for_player_name, player: Entry):
    if not player:
        return None
    return for_player_name in player.player().name
