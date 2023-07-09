from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from tejos import rdf

from . import graphrepo


class RoundRepo(graphrepo.GraphRepo):
    rdf_type = rdf.ROUND

    def upsert(self, draw_round):
        rdf.subject_finder_creator(self.graph, draw_round.subject, self.rdf_type, partial(self.creator, draw_round))
        pass

    def creator(self, draw_round, g, sub):
        g.add((sub, RDF.type, rdf.ROUND))
        g.add((sub, rdf.hasRoundNumber, Literal(draw_round.round_id)))
        g.add((sub, rdf.isRoundForDraw, Literal(draw_round.draw_subject)))
        g.add((sub, rdf.notation, Literal(draw_round.name)))
        return g

