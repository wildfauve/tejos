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
        bn = BNode()
        for set_number, set_game in enumerate(set_games):
            self.graph.add((bn, rdf.forSet + str(set_number + 1), Literal(set_game)))
        self.graph.add((sub, predicate, bn))
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
        return g
