from typing import List, Union
from functools import partial
from rdflib import Graph, RDF, URIRef, Literal

from tejos.rdf import rdf_prefix
from tejos.model import player, model
from tejos.repo import repository
from tejos.util import fn, error


class Entry(model.GraphModel):
    repo = repository.EntryRepo
    repo_graph = model.GraphModel.tournament_graph
    repo_instance = None

    @classmethod
    def create(cls, player, draw, seed):
        en = cls(player=player, draw=draw, seed=seed)
        cls.repository().upsert(en)
        return en

    @classmethod
    def get_all_entries_for_draw(cls, draw):
        return [cls.builder(entry, draw) for entry in cls.repository().get_all_entries_for_draw(draw.subject)]


    @classmethod
    def builder(cls, entry, draw):
        sub, player_sub, klass_name, seed, draw_sub = entry
        return cls(player=player.Player.load(klass_name=klass_name),
                   draw=draw,
                   seed=seed,
                   sub=sub)

    def __init__(self, player, draw, seed, sub: URIRef = None):
        self.is_entry_for_player = player
        self.is_in_draw = draw
        self.has_seed = seed
        self.subject = URIRef(f"{self.is_in_draw.subject.toPython()}/{self.is_entry_for_player.uri_name()}") if not sub else sub


    def player(self):
        return self.is_entry_for_player

    def seeding(self):
        if not self.has_seed:
            return "   "
        return str(self.has_seed).rjust(3)


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
