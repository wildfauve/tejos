from functools import partial
from itertools import groupby

from rdflib import Graph, URIRef, Literal, RDF

from tejos import rdf
from tejos.util import logger
from . import graphrepo


class SelectionRepo(graphrepo.GraphRepo):
    rdf_type = rdf.SELECTION

    def __init__(self, graph: Graph):
        self.graph = graph

    def get_all_for_team(self, team_sub):
        return self.query_for_selections(team_sub, perf_ctx=team_sub)

    @logger.with_perf_log(name="Selection.query_for_selections")
    def query_for_selections(self, team_sub, perf_ctx):
        return [self.build_selection(select_sub) for select_sub, _, _ in self.all_for_team_sub(team_sub)]

    def all_for_team_sub(self, team_sub):
        return rdf.all_matching(self.graph, (None, rdf.isSelectionForTeam, team_sub))

    def build_selection(self, select_sub):
        sel_triples = rdf.all_matching(self.graph, (select_sub, None, None))
        num_of_sets = rdf.triple_finder(rdf.hasSelectedSets, sel_triples)
        selected_winner = rdf.triple_finder(rdf.hasSelectedWinner, sel_triples)
        for_match = rdf.triple_finder(rdf.isSelectionForMatch, sel_triples)
        pts_strat = rdf.triple_finder(rdf.hasFantasyPointsStrategy, sel_triples)
        return (
            select_sub,
            for_match,
            selected_winner,
            num_of_sets.toPython(),
            pts_strat
        )

    def to_selection(self, selection, props):
        player_props = props if isinstance(props, list) else list(props)
        return (player_props[0].sub,
                player_props[0].name.toPython(),
                player_props[0].tour_symbol.toPython(),
                player_props[0].klass_name.toPython(),
                [r.alt_names.toPython() for r in player_props] if player_props[0].alt_names else None)

    def upsert(self, selection):
        rdf.subject_finder_creator(self.graph, selection.subject,
                                   self.rdf_type,
                                   partial(self.creator, selection),
                                   update_fn=partial(self.updater, selection))
        pass

    def get_by_name_or_klass_name(self, name=None, klass_name=None, alt_name=None):
        result = rdf.many(rdf.query(self.graph, self._name_sparql(name=name, klass_name=klass_name, alt_name=alt_name)))
        if not result:
            return None
        return self.to_player(result[0].sub, result)

    def creator(self, selection, g, sub):
        g.add((sub, RDF.type, self.rdf_type))
        g.add((sub, rdf.isSelectionForTeam, selection.team_subject))
        g.add((sub, rdf.isSelectionForMatch, selection.match.subject))
        g.add((sub, rdf.hasSelectedWinner, selection.selected_winner.subject))
        g.add((sub, rdf.hasSelectedSets, Literal(selection.in_number_sets)))
        g.add((sub, rdf.hasFantasyPointsStrategy, selection.points_strategy.subject()))
        return g

    def updater(self, selection, sub):
        logger.log(f"Updating selection: {sub}", log_type=logger.LogType.INFO)
        self.graph.set((sub, rdf.hasSelectedWinner, selection.selected_winner.subject))
        self.graph.set((sub, rdf.hasSelectedSets, Literal(selection.in_number_sets)))
