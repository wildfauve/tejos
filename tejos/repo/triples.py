from typing import Callable
from rdflib import Graph
from pathlib import Path

from tejos import rdf
from tejos.util import singleton

DB_PLAYERS_LOCATION = (Path(__file__).parent.parent.parent / "data" / "db" / "players.ttl")
DB_LOCATION = (Path(__file__).parent.parent.parent / "data" / "db" / "tejos.ttl")


class Db:

    def __init__(self,
                 empty_graph_fn: Callable,
                 ttl_writer: Callable):
        self.tournament_graph = None
        self.players_graph = None
        self.in_memory = None
        self.init_empty_graph_fn = empty_graph_fn
        self.ttl_writer = ttl_writer

    def drop(self):
        self.ttl_writer(self.init_empty_graph_fn(), file=self.persist_location())
        return self

    def load(self):
        if RepoContext().triples_location.exists():
            players_g = self.init_empty_graph_fn().parse(RepoContext().players_triples_location)
            g = self.init_empty_graph_fn().parse(RepoContext().triples_location)
        else:
            players_g = self.init_empty_graph_fn()
            g = self.init_empty_graph_fn()
            self.in_memory = True
        self.tournament_graph = g
        self.players_graph = players_g
        return self

    def save(self):
        self.ttl_writer(self.tournament_graph, file=self.persist_location())
        return self

    def persist_location(self):
        return RepoContext().triples_location

    def init_empty_graph(self) -> Graph:
        return self.init_empty_graph_fn()


class RepoContext(singleton.Singleton):

    def configure(self, triples_location: Path = DB_LOCATION,
                  players_triples_location: Path = DB_PLAYERS_LOCATION) -> None:
        if not self.already_configured():
            self.triples_location = triples_location
            self.players_triples_location = players_triples_location
        pass

    def already_configured(self):
        return hasattr(self, 'triples_location') and hasattr(self, 'players_triples_location')

    def db_ctx(self, db: Db):
        self.db = db


def empty_graph():
    return initgraph()


def init():
    return RepoContext().db_ctx(Db(empty_graph_fn=initgraph,
                                   ttl_writer=write_to_ttl).load())


def tournament_graph():
    return RepoContext().db.tournament_graph


def players_graph():
    return RepoContext().db.players_graph


def save():
    return RepoContext().db.save()


def reload():
    return init()


def drop():
    RepoContext().db.drop()


def initgraph() -> Graph:
    return rdf.bind(rdf_graph())


def rdf_graph():
    return Graph()


def write_to_ttl(g, format="turtle", file=None):
    if format == "turtle":
        txt = g.serialize(format=format)
    else:
        txt = g.serialize(format="json-ld", indent=4)
    if file:
        with open(file, 'w') as f:
            f.write(txt)
