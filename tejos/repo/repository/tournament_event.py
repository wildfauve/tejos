from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from tejos import rdf


class TournamentEventRepo:
    rdf_type = rdf.TOURNAMENT_EVENT

    def __init__(self, graph: Graph):
        self.graph = graph

    def upsert(self, event):

        rdf.subject_finder_creator(self.graph, event.subject, self.rdf_type, partial(self.creator, event))
        pass

    def creator(self, event, g, sub):
        g.add((sub, RDF.type, rdf.TOURNAMENT_EVENT))
        g.add((sub, rdf.skos.notation, Literal(event.name)))
        g.add((sub, rdf.isEventOf, event.is_event_of.subject))
        return g

