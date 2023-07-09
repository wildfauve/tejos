from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from tejos import rdf


class DrawRepo:
    rdf_type = rdf.DRAW

    def __init__(self, graph: Graph):
        self.graph = graph

    def upsert(self, draw):
        rdf.subject_finder_creator(self.graph, draw.subject, self.rdf_type, partial(self.creator, draw))
        pass

    def update_draw_size(self, draw):
        self.graph.set((draw.subject, rdf.hasInitialDrawSize, Literal(draw.number_of_matches)))

    def creator(self, draw, g, sub):
        g.add((sub, RDF.type, rdf.DRAW))
        g.add((sub, rdf.hasBestOfSets, Literal(draw.best_of)))
        g.add((sub, rdf.hasInitialDrawSize, Literal(draw.number_of_matches)))
        g.add((sub, rdf.isDrawFromEvent, draw.tournament.subject))
        return g

