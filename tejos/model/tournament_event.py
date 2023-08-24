from typing import List
from itertools import accumulate

from rdflib import Graph, RDF, URIRef, Literal

from tejos.util import fn
from tejos.rdf import rdf_prefix
from tejos import model
from tejos.repo import repository
from tejos.model.player import Player
from tejos import adapter


class TournamentEvent(model.GraphModel):
    repo = repository.TournamentEventRepo
    repo_graph = model.GraphModel.tournament_graph
    repo_instance = None

    @classmethod
    def create(cls, year: int, tournament_name: str = None, tournament=None):
        event_of = tournament if isinstance(tournament, model.GrandSlam) else model.GrandSlam.get(name=tournament_name)
        event = cls(event_of=event_of, year=year)
        cls.repository().upsert(event)
        return event

    @classmethod
    def get_all(cls):
        # res = cls.repository().get_all()
        # breakpoint()
        return [cls(*[event[-1:][0]] + list(event[:-1])) for event in cls.repository().get_all()]

    @classmethod
    def get(cls, year: int, tournament):
        event = cls.repository().find_by_year(tournament.subject, year)
        if not event:
            return None
        return cls(*[tournament] + list(event[:-1]))

    @classmethod
    def get_all_for_tournament(cls, tournament):
        return [cls.build_event(tournament, event) for event in cls.repository().find_by_tournament(tournament.subject)]

    @classmethod
    def build_event(cls, tournament, event):
        year, name, sub, _tourn_sub = event
        return cls(event_of=tournament,
                   year=year,
                   sub=sub,
                   name=name)


    @classmethod
    def get_by_sub(cls, sub):
        event = cls.repository().get_by_sub(sub)
        if not event:
            return None
        return cls(*[event[-1:][0]] + list(event[:-1]))


    def __init__(self, event_of, year, name: str = None, sub: URIRef = None):
        self.is_event_of = event_of if isinstance(event_of, model.GrandSlam) else self.tournament_by_sub(event_of)
        self.scheduled_in_year = year
        self.relative_subject = f"{self.is_event_of.subject_name}/{self.scheduled_in_year}"
        self.subject = rdf_prefix.clo_te_ind_tou[self.relative_subject] if not sub else sub
        self.name = f"{self.is_event_of.subject_name}{self.scheduled_in_year}" if not name else name
        self.label = f"{self.is_event_of.name} {self.scheduled_in_year}"
        self.draws = []
        # This loads all players into the players module to make the entries config faster
        Player.loadall()

    def load(self):
        model.Draw.get_all_for_event(self)
        return self

    def tournament_by_sub(self, sub):
        return model.GrandSlam.get_by_sub(sub)


    def get_full_draw(self):
        return adapter.us_build_draw(event=self, for_rd=1, scores_only=False, full_draw=True)

    def make_draw(self, name: str, best_of: int, draw_size=int, points_strategy_components: tuple = None):
        draw = self.find_draw_by_symbol(name)
        if draw:
            return draw
        draw = model.Draw.create(name=name,
                                 best_of=best_of,
                                 draw_size=draw_size,
                                 event=self,
                                 points_strategy_components=points_strategy_components)
        self.has_draw(draw)
        return draw


    def has_draw(self, draw):
        if fn.find(lambda dr: dr == draw, self.draws):
            return self
        self.draws.append(draw)
        return self

    def for_draw(self, name):
        return self.find_draw_by_symbol(name)

    def find_draw_by_symbol(self, symbol):
        return fn.find(lambda dr: dr.name == symbol, self.draws)

    def fantasy_points_schedule(self, rd_number, accum: bool = False) -> List:
        sched = [len(self.draws) * pt for pt in (self.draws[0].fantasy_points_schedule(rd_number))]
        if not accum:
            return sched
        return list(accumulate(sched))

    def fantasy_points_allocation(self, rd_number: int) -> str:
        return self.draws[0].fantasy_points_allocation(rd_number)

    def __hash__(self):
        return hash((self.subject,))

    def __eq__(self, other):
        if not self or not other:
            return None
        return self.subject == other.subject

