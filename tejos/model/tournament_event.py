from typing import List
from itertools import accumulate

from rdflib import Graph, RDF, URIRef, Literal

from tejos.util import fn
from tejos.rdf import rdf_prefix
from tejos import model
from tejos.repo import repository
from tejos.model.player import Player


class TournamentEvent(model.GraphModel):
    repo = repository.TournamentEventRepo

    def __init__(self, event_of, year, sub: URIRef = None):
        self.is_event_of = event_of
        self.scheduled_in_year = year
        self.subject = rdf_prefix.clo_te_ind_tou[self.is_event_of.subject_name] + f"/{self.scheduled_in_year}" if not sub else sub
        self.name = f"{self.is_event_of.subject_name}{self.scheduled_in_year}"
        self.label = f"{self.is_event_of.name} {self.scheduled_in_year}"
        self.draws = []
        self.repo(self.__class__.tournament_graph()).upsert(self)
        # This loads all players into the players module to make the entries config faster
        Player.loadall()

    def has_draw(self, draw):
        self.draws.append(draw)
        return self

    def find_draw_by_symbol(self, symbol):
        return fn.find(lambda dr: dr.name == symbol, self.draws)

    def fantasy_points_schedule(self, rd_number, accum: bool = False) -> List:
        sched = [len(self.draws) * pt for pt in (self.draws[0].fantasy_points_schedule(rd_number))]
        if not accum:
            return sched
        return list(accumulate(sched))

    def fantasy_points_allocation(self, rd_number: int) -> str:
        return self.draws[0].fantasy_points_allocation(rd_number)
