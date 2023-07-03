from typing import List
from itertools import accumulate


from rdflib import Graph, RDF, URIRef, Literal

from tejos.graph import rdf_prefix
class TournamentEvent:

    """
    ao:AustralianOpen2023
    a                 fau-ten:Event ;
    fau-ten:isEventOf ao:AustralianOpen ;
    skos:notation     "Australian Open 2023" ;
    fau-ten:hasDraw   <https://fauve.io/ao/2023/mensSingles>, <https://fauve.io/ao/2023/womensSingles> .

    """

    def __init__(self, event_of, year):
        self.is_event_of = event_of
        self.scheduled_in_year = year
        self.subject = URIRef(f"https://fauve.io/{self.is_event_of.subject_name}/{self.scheduled_in_year}")
        self.name = f"{self.is_event_of.subject_name}{self.scheduled_in_year}"
        self.label = f"{self.is_event_of.name} {self.scheduled_in_year}"
        self.draws = []

    def has_draw(self, draw):
        self.draws.append(draw)
        return self

    def build_graph(self, g: Graph):
        g.add((self.subject, RDF.type, rdf_prefix.fau_ten.Event))
        g.add((self.subject, rdf_prefix.fau_ten.isEventOf, self.is_event_of.subject))
        g.add((self.subject, rdf_prefix.skos.notation, Literal(self.label)))
        for draw in self.draws:
            g.add((self.subject, rdf_prefix.fau_ten.hasDraw, draw.subject))
            draw.build_graph(g)
        return g


    def fantasy_points_schedule(self, rd_number, accum:bool = False) -> List:
        sched = [len(self.draws) * pt for pt in (self.draws[0].fantasy_points_schedule(rd_number))]
        if not accum:
            return sched
        return list(accumulate(sched))

    def fantasy_points_allocation(self, rd_number: int) -> str:
        return self.draws[0].fantasy_points_allocation(rd_number)
