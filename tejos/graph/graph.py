from rdflib import Graph, URIRef
from pathlib import Path

from . import binding

BASE_PATH = (Path(__file__).parent.parent / "ontology")
EVENT_BASE_PATH = (Path(__file__).parent.parent / "majors")

TENNIS_ONTO = (BASE_PATH / "ontology.ttl")
PLAYERS_IND = (BASE_PATH / "players.ttl")
AO2023 = (EVENT_BASE_PATH / "year_2023" / "australian_open" / "triple_store" / "ao2023.ttl")


def empty_graph():
    return initgraph()


def graph():
    g = initgraph()
    g.parse(TENNIS_ONTO)
    g.parse(PLAYERS_IND)
    g.parse(AO2023)
    return g


def initgraph() -> Graph:
    return binding.bind(rdf_graph())


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
