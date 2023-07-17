from rdflib import URIRef, RDF, Literal

from tejos.rdf import rdf_prefix
from tejos import model
from tejos.repo import repository
from tejos.util import fn, singleton


class Tournament():
    repo = model.GraphModel2().new(repository.TournamentRepo, model.GraphModel2.tournament_graph)

    @classmethod
    def create(cls, name: str, subject_name: str, perma_id: str):
        tournie = cls(name, subject_name, perma_id)
        cls.repo().upsert(tournie)
        return tournie

    @classmethod
    def get_all(cls):
        return [cls(*tournie) for tournie in cls.repo().get_all()]

    @classmethod
    def get(cls, name):
        tournie = cls.repo().find_by_name(name)
        if not tournie:
            return None
        return cls(*tournie)

    @classmethod
    def get_by_sub(cls, sub: URIRef):
        tournie = cls.repo().get_by_sub(sub)
        if not tournie:
            return None
        return cls(*tournie)

    def __init__(self, name, subject_name: str, perma_id: str, sub: URIRef = None):
        self.name = name
        self.perma_id = perma_id
        self.subject_name = subject_name
        self.subject = rdf_prefix.clo_te_ind_tou[subject_name] if not sub else sub
        self.events = []

    def __hash__(self):
        return hash((self.subject,))

    def __eq__(self, other):
        if not self or not other:
            return None
        return self.subject == other.subject

    def make_event(self, year):
        event = fn.find(lambda ev: ev.scheduled_in_year == year, self.events)
        if event:
            return event
        event = model.TournamentEvent.create(year=year, tournament=self)
        self.events.append(event)
        return event

    def for_year(self, year, load: bool = False):
        event = fn.find(lambda event: event.scheduled_in_year == year, self.events)
        if not load:
            return event
        return event.load()

    def all_events(self):
        self.events = model.TournamentEvent.get_all_for_tournament(self)
        return self


class GrandSlam(Tournament):
    pass


class TournamentFinder(singleton.Singleton):

    def add_touraments(self, tournies):
        self.tournaments = tournies

    def slam(self, symbol):
        return fn.find(lambda tournie: tournie.subject_name == symbol, self.tournaments)

    def slam_names(self):
        return [tournie.name for tournie in self.tournaments]

    def slam_symbols(self):
        return [tournie.subject_name for tournie in self.tournaments]

    def slam_year(self, name, year, load: bool = False):
        tournie = self.slam(name)
        return tournie, tournie.for_year(year, load=load)


def tournaments():
    all_tournies = GrandSlam.get_all()
    TournamentFinder().add_touraments([Tournament.all_events(tournie) for tournie in all_tournies])
    return TournamentFinder()
