from rdflib import URIRef, RDF, Literal

from tejos.graph import rdf_prefix

class Tournament:
    """
    ao:AustralianOpen
    a             fau-ten:GrandSlam ;
    skos:notation "Australian Open" .

    """
    def __init__(self, name, subject_name: str, perma_id: str):
        self.name = name
        self.perma_id = perma_id
        self.subject_name = subject_name
        self.subject = URIRef(f"https://fauve.io/{subject_name}")

    def build_graph(self, g):
        g.add((self.subject, RDF.type, rdf_prefix.fau_ten.GrandSlam))
        g.add((self.subject, rdf_prefix.skos.notation, Literal(self.name)))
        return g


class GrandSlam(Tournament):
    pass
