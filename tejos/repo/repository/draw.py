from typing import Tuple
from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from . import graphrepo
from tejos import rdf


class DrawRepo(graphrepo.GraphRepo):
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
        g.add((sub, rdf.notation, Literal(draw.name)))
        g.add((sub, rdf.hasBestOfSets, Literal(draw.best_of)))
        g.add((sub, rdf.hasInitialDrawSize, Literal(draw.number_of_matches)))
        g.add((sub, rdf.isDrawFromEvent, draw.tournament.subject))
        return g

    def get(self, event_subject, name):
        return self.to_draw(rdf.single_result_or_none(rdf.query(self.graph,
                                                                self._sparql(name=name,
                                                                             event_sub=event_subject))))

    def to_draw(self, result) -> Tuple:
        if not result:
            return None
        return (result.name.toPython(),
                result.best_of.toPython(),
                result.draw_size.toPython(),
                result.draw,
                result.event_sub)



    def _sparql(self, event_sub=None, name=None):
        if not name and not event_sub:
            filter_criteria = None
        else:
            filter_criteria = f"?event_sub = {event_sub.n3()} && ?name = {Literal(name).n3()}"
        filter = "" if not filter_criteria else f"filter({filter_criteria})"

        return f"""
        select ?draw ?name ?best_of ?draw_size ?event_sub

        where {{

  	    ?draw a clo-te:Draw ;
	           skos:notation ?name ;
	           clo-te:hasBestOfSets ?best_of ;
	           clo-te:hasInitialDrawSize ?draw_size ;
               clo-te:isDrawFromEvent ?event_sub .

        {filter} }}
        """
