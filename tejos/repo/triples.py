from typing import Callable, List, Tuple, Dict
from functools import reduce
from rdflib import Graph
from pathlib import Path

from tejos.util import singleton

from tejos import rdf


DB_MAP = {
    'fantasy_graph': (Path(__file__).parent.parent.parent / "data" / "db" / "fantasy.ttl"),
    'players_graph': (Path(__file__).parent.parent.parent / "data" / "db" / "players.ttl"),
    'tejos_graph': (Path(__file__).parent.parent.parent / "data" / "db" / "tejos.ttl")
}


class Db:

    def __init__(self,
                 empty_graph_fn: Callable,
                 ttl_writer: Callable):
        self.graphs = {}
        self.in_memory = None
        self.init_empty_graph_fn = empty_graph_fn
        self.ttl_writer = ttl_writer

    def configure(self, db_map):
        self.graphs = db_map

    def drop(self, name: str = None, all_graphs: bool = False):
        if not name and not all_graphs:
            breakpoint()
        [self.drop_graph(gname, location) for gname, location in self.graphs.items() if
         not name or (name and gname == name)]
        self.graphs = {}
        return self

    def load(self):
        [self.load_graph(name, location) for name, location in self.graphs.items()]
        return self

    def drop_graph(self, _name: str, location: str):
        if location.exists():
            self.ttl_writer(self.init_empty_graph_fn(), location=location)
        return self

    def graph_for(self, name: str) -> Graph:
        if name not in self.graphs.keys():
            return None
        return self.get_graph_attr(name)

    def graphs_for(self, names: List) -> Graph:
        return reduce(self.graph_for_name, names, {})

    def graph_for_name(self, accum, name):
        g_name = f"{name}_graph"
        return {**accum, **{g_name: getattr(self, g_name)}}

    def load_graph(self, name: str, location: str):
        if location.exists():
            self.set_graph_attr(name, self.init_empty_graph_fn().parse(location))
        else:
            self.set_graph_attr(name, self.init_empty_graph_fn())
        return self

    def graph_attr_name(self, name) -> str:
        return f"_{name}"

    def set_graph_attr(self, name, g: Graph):
        setattr(self, self.graph_attr_name(name), g)
        return self

    def get_graph_attr(self, name):
        atr = getattr(self, self.graph_attr_name(name), None)
        if atr is None:
            breakpoint()
        return atr

    def save(self, graph_names: List = None):
        save_args = self.persist_location_args(graph_names)
        for g, loc in save_args:
            if not loc:
                breakpoint()
            self.ttl_writer(g, location=loc)
        return self

    def persist_location_args(self, graph_names=None) -> List[Tuple]:
        return [(self.get_graph_attr(name), self.name_to_location(name)) for name in graph_names]

    def name_to_location(self, name):
        return self.graphs.get(name, None)

    def init_empty_graph(self) -> Graph:
        return self.init_empty_graph_fn()


class RepoContext(singleton.Singleton):

    def configure(self,
                  graphs: Dict = DB_MAP) -> None:
        if not self.already_configured():
            self.graphs = graphs
        pass

    def already_configured(self):
        return hasattr(self, 'graphs')

    def db_ctx(self, db: Db):
        self.db = db
        self.db.configure(self.graphs)
        self.db.load()
        return self


def empty_graph():
    return initgraph()


def init():
    return RepoContext().db_ctx(Db(empty_graph_fn=initgraph,
                                   ttl_writer=write_to_ttl))


def graph(name):
    return RepoContext().db.graph_for(name)


def save(graph_names: List[str] = None):
    return RepoContext().db.save(graph_names)


def reload():
    return init()


def drop(name: str = None):
    if not name:
        return RepoContext().db.drop(all_graphs=True)
    return RepoContext().db.drop(name=name)


def initgraph() -> Graph:
    return rdf.bind(rdf_graph())


def rdf_graph():
    return Graph()


def write_to_ttl(g, format="turtle", location: Path = None):
    if format == "turtle":
        txt = g.serialize(format=format)
    else:
        txt = g.serialize(format="json-ld", indent=4)
    if not location:
        return None
    with open(location, 'w') as f:
        f.write(txt)
