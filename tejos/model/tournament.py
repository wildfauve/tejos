from rdflib import URIRef, RDF, Literal

from tejos.rdf import rdf_prefix
from tejos import model
from tejos.repo import repository

class Tournament(model.GraphModel):
    repo = repository.TournamentRepo

    def __init__(self, name, subject_name: str, perma_id: str, sub: URIRef = None):
        self.name = name
        self.perma_id = perma_id
        self.subject_name = subject_name
        self.subject = rdf_prefix.clo_te_ind_tou[subject_name] if not sub else sub
        self.repo(self.__class__.tournament_graph()).upsert(self)


class GrandSlam(Tournament):
    pass
