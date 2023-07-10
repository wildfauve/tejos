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
        g.add((sub, RDF.type, rdf.PLAYER_ENTRY))
        g.add((sub, rdf.isEntryForPlayer, entry.player().subject))
        g.add((sub, rdf.hasKlassName, Literal(entry.player().klass_name)))
        g.add((sub, rdf.hasSeed, Literal(entry.has_seed)))
        g.add((sub, rdf.isEnterForDraw, entry.is_in_draw.subject))
        return g


    def get_all_entries_for_draw(self, draw_sub):
        return [self.to_entry(entry) for entry in (rdf.many(rdf.query(self.graph, self._sparql(draw_sub))))]


    def to_entry(self, entry):
        if not entry:
            return None
        return (
            entry.entry,
            entry.player_sub,
            entry.player_klass_name.toPython(),
            entry.seed.toPython(),
            entry.draw
        )


    def _sparql(self, draw_sub=None):
        if not draw_sub:
            filter_criteria = None
        else:
            filter_criteria = f"?draw = {draw_sub.n3()}"

        filter = "" if not filter_criteria else f"filter({filter_criteria})"

        return f"""
        select ?entry ?player_klass_name ?seed ?draw ?player_sub

        where {{

  	    ?entry a clo-te:PlayerEntry ;
  	           clo-te-plr:hasKlassName ?player_klass_name ;
               clo-te:hasSeed ?seed ;
               clo-te:isEnterForDraw ?draw ;
               clo-te:isEntryForPlayer ?player_sub .

        {filter} }}
        """
