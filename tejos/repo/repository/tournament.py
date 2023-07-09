from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from tejos import rdf


class TournamentRepo:
    rdf_type = rdf.TOURNAMENT

    def __init__(self, graph: Graph):
        self.graph = graph

    def upsert(self, tournament):
        rdf.subject_finder_creator(self.graph, tournament.subject, self.rdf_type, partial(self.creator, tournament))
        pass

    def creator(self, tournament, g, sub):
        g.add((sub, RDF.type, rdf.TOURNAMENT))
        g.add((sub, rdf.skos.notation, Literal(tournament.name)))
        return g

