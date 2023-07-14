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

    def get_all(self):
        results = rdf.many(rdf.query(self.graph, self._name_sparql()))
        return [self.to_player(player, props) for player, props in groupby(results, lambda x: x[0])]

    def to_player(self, player, props):
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
        g.add((sub, rdf.isSelectionForMatch, selection.match.subject))
        g.add((sub, rdf.hasSelectedWinner, selection.selected_winner.subject))
        g.add((sub, rdf.hasSelectedSets, Literal(selection.in_number_sets)))
        g.add((sub, rdf.hasFantasyPointsStrategy, selection.points_strategy.subject()))
        return g


    def updater(self, selection, sub):
        self.graph.set((sub, rdf.hasSelectedWinner, selection.selected_winner.subject))
        self.graph.set((sub, rdf.hasSelectedSets, Literal(selection.in_number_sets)))
