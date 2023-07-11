from typing import Tuple
from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF, BNode

from tejos import rdf
from . import graphrepo


class MatchRepo(graphrepo.GraphRepo):
    rdf_type = rdf.MATCH


    def upsert(self, match):
        rdf.subject_finder_creator(self.graph, match.subject, self.rdf_type, partial(self.creator, match))
        pass


    def add_players_to_match(self, match, entries: Tuple):
        print(f"{match.subject}")
        e1, e2 = entries
        if e1:
            self.graph.add((match.subject, rdf.hasMatchUpPosition1, e1.subject))
        if e2:
            self.graph.add((match.subject, rdf.hasMatchUpPosition2, e2.subject))
        pass

    def add_score(self, match, entry, set_games):
        pos, entry = entry
        if pos not in [1, 2]:
            breakpoint()
        if pos == 1:
            _, _, o = rdf.first_match(self.graph, (match.subject, rdf.hasSetsScores1, None))
            if o:
                return
            self.add_scores_for_predicate(match.subject, set_games, rdf.hasSetsScores1)
        else:
            _, _, o = rdf.first_match(self.graph, (match.subject, rdf.hasSetsScores2, None))
            if o:
                return
            self.add_scores_for_predicate(match.subject, set_games, rdf.hasSetsScores2)
        pass


    def add_scores_for_predicate(self, sub, set_games, predicate):
        for set_game in set_games:
            self.graph.add((sub, predicate, set_game))
        pass

    def add_match_winner(self, match):
        self.graph.add((match.subject, rdf.hasMatchWinner, match.match_winner.subject))
        pass

    def add_retirement(self, match):
        self.graph.add((match.subject, rdf.retiredFromMatch, match.entry_retirement.subject))
        pass

    def add_withdrawal(self, match):
        self.graph.add((match.subject, rdf.withdrawnFromMatch, match.entry_withdrawal.subject))
        pass

    def creator(self, match, g, sub):
        g.add((sub, RDF.type, self.rdf_type))
        g.add((sub, rdf.hasMatchId, Literal(match.match_id)))
        g.add((sub, rdf.hasMatchNumber, Literal(match.number)))
        g.add((sub, rdf.isMatchInRound, match.for_round.subject))
        return g

    def get_all_for_round(self, round_sub):
        matches = rdf.many(rdf.query(self.graph, self._sparql(round_sub)))
        return [self.to_match(match) for match in matches]

    def to_match(self, match):
        # mt_props = [(p.match,
        #              p.match_id.toPython(),
        #              p.match_number.toPython(),
        #              p.pos1_sub,
        #              p.pos2_sub) for p in match_props]
        scores1 = rdf.all_matching(self.graph, (match.match_sub, rdf.hasSetsScores1, None), form=self.scores_from_matches)
        scores2 = rdf.all_matching(self.graph, (match.match_sub, rdf.hasSetsScores2, None),
                                   form=self.scores_from_matches)
        return (
            match.match_sub,
            match.round,
            match.match_id.toPython(),
            match.match_number.toPython(),
            match.pos1_sub,
            match.pos2_sub,
            match.winner,
            scores1,
            scores2
        )

    def scores_from_matches(self, triple):
        _, _, score = triple
        return score


    def _sparql(self, round_sub=None):
        if not round_sub:
            filter_criteria = None
        else:
            filter_criteria = f"?round = {round_sub.n3()}"

        filter = "" if not filter_criteria else f"filter({filter_criteria})"

        return f"""
select ?round ?match_sub ?match_id ?match_number ?pos1_sub ?pos2_sub ?winner ?player1_scores ?player2_scores

where {{

  		?match_sub clo-te:isMatchInRound ?round ; 
                   clo-te:hasMatchId ?match_id ;
                   clo-te:hasMatchNumber ?match_number ;
                   clo-te:hasMatchUpPosition1 ?pos1_sub ;
                   clo-te:hasMatchUpPosition2 ?pos2_sub .
               
	  	OPTIONAL {{
               ?match clo-te:hasMatchWinner ?winner .
             }}
               
        {filter} 
}}"""
