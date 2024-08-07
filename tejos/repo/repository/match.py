from typing import Tuple
from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF, BNode

from tejos import rdf
from . import graphrepo
from tejos.util import logger, fn


class MatchRepo(graphrepo.GraphRepo):
    rdf_type = rdf.MATCH

    def upsert(self, match):
        rdf.subject_finder_creator(self.graph, match.subject, self.rdf_type, partial(self.creator, match))
        pass

    def add_players_to_match(self, match, entries: Tuple):
        logger.log(f"Add Players to Match with Subject: {match.subject}")
        e1, e2 = entries
        if e1:
            self.graph.set((match.subject, rdf.hasMatchUpPosition1, e1.subject))
        if e2:
            self.graph.set((match.subject, rdf.hasMatchUpPosition2, e2.subject))
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

    def add_walkover(self, match):
        self.graph.add((match.subject, rdf.walkoverFromMatch, match.entry_walkover.subject))
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
        return self.query_for_matches(round_sub, perf_ctx=round_sub)

    @logger.with_perf_log(name="Match.query_for_matches")
    def query_for_matches(self, round_sub, perf_ctx):
        return [self.build_match(match_sub) for _, _, match_sub in self.all_for_round_sub(round_sub)]

    def all_for_round_sub(self, round_sub):
        return rdf.all_matching(self.graph, (round_sub, rdf.hasMatch, None))

    def build_match(self, match_sub):
        match_triples = rdf.all_matching(self.graph, (match_sub, None, None))
        match_id = rdf.triple_finder(rdf.hasMatchId, match_triples)
        match_num = rdf.triple_finder(rdf.hasMatchNumber, match_triples)
        match_rd_sub = rdf.triple_finder(rdf.isMatchInRound, match_triples)
        pos1 = rdf.triple_finder(rdf.hasMatchUpPosition1, match_triples)
        pos2 = rdf.triple_finder(rdf.hasMatchUpPosition2, match_triples)
        retired_player = rdf.triple_finder(rdf.retiredFromMatch, match_triples)
        withdrawn_player = rdf.triple_finder(rdf.withdrawnFromMatch, match_triples)
        walkover_player = rdf.triple_finder(rdf.walkoverFromMatch, match_triples)
        winner = rdf.triple_finder(rdf.hasMatchWinner, match_triples)
        scores1 = rdf.triple_finder(rdf.hasSetsScores1, match_triples, filter_fn=fn.select, builder=rdf.all_objects)
        scores2 = rdf.triple_finder(rdf.hasSetsScores2, match_triples, filter_fn=fn.select, builder=rdf.all_objects)
        return (
            match_sub,
            match_rd_sub,
            match_id.toPython(),
            match_num.toPython(),
            pos1,
            pos2,
            winner,
            scores1,
            scores2,
            retired_player,
            withdrawn_player,
            walkover_player
        )

    def scores_from_matches(self, triple):
        _, _, score = triple
        return score
