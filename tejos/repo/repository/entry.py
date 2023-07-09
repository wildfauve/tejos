from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from tejos import rdf


class EntryRepo:
    rdf_type = rdf.PLAYER_ENTRY

    def __init__(self, graph: Graph):
        self.graph = graph

    def upsert(self, entry):
        rdf.subject_finder_creator(self.graph, entry.subject, self.rdf_type, partial(self.creator, entry))
        pass

    def creator(self, entry, g, sub):
        """
        g.add((self.subject, RDF.type, rdf_prefix.fau_ten.QualifiedPlayer))
        g.add((self.subject, rdf_prefix.fau_ten.hasSeed, Literal(self.has_seed)))
        g.add((self.subject, rdf_prefix.fau_ten.isEntryForPlayer, self.player().subject))
        return g
        """
        g.add((sub, RDF.type, rdf.PLAYER_ENTRY))
        g.add((sub, rdf.isEntryForPlayer, entry.player().subject))
        g.add((sub, rdf.hasKlassName, Literal(entry.player().klass_name)))
        g.add((sub, rdf.hasSeed, Literal(entry.has_seed)))
        g.add((sub, rdf.isEnterForDraw, entry.is_in_draw.subject))
        return g

