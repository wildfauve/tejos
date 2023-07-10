from rdflib import URIRef, RDF, Literal

from tejos.rdf import rdf_prefix
from tejos import model
from tejos.repo import repository
from tejos.util import fn


class Tournament(model.GraphModel):
    repo = repository.TournamentRepo
    repo_graph = model.GraphModel.tournament_graph
    repo_instance = None

    @classmethod
    def create(cls, name: str, subject_name: str, perma_id: str):
        tournie = cls(name, subject_name, perma_id)
        cls.repository().upsert(tournie)
        return tournie

    @classmethod
    def get_all(cls):
        return [cls(*tournie) for tournie in cls.repository().get_all()]


    @classmethod
    def get(cls, name):
        tournie = cls.repository().find_by_name(name)
        if not tournie:
            return None
        return cls(*tournie)

    @classmethod
    def get_by_sub(cls, sub: URIRef):
        tournie = cls.repository().get_by_sub(sub)
        if not tournie:
            return None
        return cls(*tournie)


    def __init__(self, name, subject_name: str, perma_id: str, sub: URIRef = None):
        self.name = name
        self.perma_id = perma_id
        self.subject_name = subject_name
        self.subject = rdf_prefix.clo_te_ind_tou[subject_name] if not sub else sub
        self.events = []
        self.repo(self.__class__.tournament_graph()).upsert(self)

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



class GrandSlam(Tournament):
    pass
