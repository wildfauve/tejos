from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from tejos import rdf

from . import graphrepo


class RoundRepo(graphrepo.GraphRepo):
    rdf_type = rdf.ROUND

    def upsert(self, draw_round):
        rdf.subject_finder_creator(self.graph, draw_round.subject, self.rdf_type, partial(self.creator, draw_round))
        pass

    def add_match(self, sub, match_subject):
        self.graph.add((sub, rdf.hasMatch, match_subject))
        pass

    def creator(self, draw_round, g, sub):
        g.add((sub, RDF.type, rdf.ROUND))
        g.add((sub, rdf.hasRoundNumber, Literal(draw_round.round_id)))
        g.add((sub, rdf.isRoundForDraw, Literal(draw_round.draw.subject)))
        g.add((sub, rdf.isBestOfGames, Literal(draw_round.games_best_of)))
        g.add((sub, rdf.notation, Literal(draw_round.name)))
        return g

    def get_all_for_draw(self, draw_sub):
        rounds = rdf.many(rdf.query(self.graph, self._sparql(draw_sub)))
        return [self.to_round(rd, props) for rd, props in groupby(rounds, lambda x: x[0])]


    def to_round(self, rd, props):
        rd_props = list(props)
        match_subs = [p.match for p in rd_props]
        rd_prop = rd_props[0]
        return (
            rd_prop.draw_rd,
            rd_prop.draw_name.toPython(),
            rd_prop.rd_number.toPython(),
            rd_prop.best_of.toPython(),
            rd_prop.draw_sub,
            match_subs
        )


    # def to_round(self, rd, props):
    #     rd_props = list(props)
    #     mt_props = [(p.match,
    #                  p.match_id.toPython(),
    #                  p.match_number.toPython(),
    #                  p.pos1_sub,
    #                  p.pos2_sub) for p in rd_props]
    #     rd_prop = rd_props[0]
    #     return (
    #         rd,
    #         rd_prop.draw_rd,
    #         rd_prop.draw_name.toPython(),
    #         rd_prop.rd_number.toPython(),
    #         rd_prop.best_of.toPython(),
    #         rd_prop.draw_sub,
    #         mt_props
    #     )

    def _sparql(self, draw_sub=None):
        if draw_sub:
            filter_criteria = None
        else:
            filter_criteria = f"?draw = {draw_sub.n3()}"

        filter = "" if not filter_criteria else f"filter({filter_criteria})"

        return f"""
        select ?draw_rd ?draw_name ?rd_number ?best_of ?draw_sub ?match

        where {{

  	    ?draw_rd a clo-te:DrawRound ;
	             skos:notation ?draw_name ;
	             clo-te:hasRoundNumber ?rd_number ;
	             clo-te:isBestOfGames ?best_of ;
                 clo-te:hasMatch ?match ;
                 clo-te:isRoundForDraw ?draw_sub .
                       

        {filter} }}
        """
