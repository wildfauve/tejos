from enum import Enum
from functools import partial

from rdflib import URIRef, Graph, RDF, Literal
from rich.table import Table

from tejos.model.draw import Draw
from tejos.model.player import Player
from tejos.model.entry import Entry
from tejos.graph import rdf_prefix

from tejos.util import fn, identity


class Team:
    def __init__(self, name, members):
        self.name = name
        self.symbolic_name = name.replace(" ", "")
        self.members = members
        self.fantasy_draws = []
        self.subject = URIRef(f"https://fauve.io/fantasyTeam/{self.symbolic_name}")
        self.result_file_name = name.lower().replace(" ", "_")

    def build_graph(self, g: Graph):
        g.add((self.subject, RDF.type, rdf_prefix.fau_ten.FantasyTeam))
        g.add((self.subject, rdf_prefix.skos.notation, Literal(self.name)))
        g.add((self.subject, rdf_prefix.fau_ten.hasFantasyMembers, Literal(self.members)))
        return g

    def draw(self, for_draw: Draw):
        # print(f"Team: {self.name} Draw: {for_draw.name}")
        fantasy = self._find_fantasy_draw(for_draw)
        if not fantasy:
            fantasy = FantasyDraw(for_draw, self)
            self.fantasy_draws.append(fantasy)
        return fantasy

    def show_draws(self, for_round: int, table: Table):
        for draw in self.fantasy_draws:
            self.show_draw(draw, table, for_round)

    def show_draw(self, for_draw: Draw, table: Table, for_round: int = None):
        for_draw.show(table, for_round)

    def points_per_round(self, up_to_rd: int = None):
        """
        There are only ever 2 draws (mens and womens).  Get the total points for each match in the round in both draws.
        """
        d1, d2 = [fantasy_draw.points_per_round(up_to_rd) for fantasy_draw in self.fantasy_draws]
        return [sum(t) for t in zip(d1, d2)]

    def total_points(self, for_round=None):
        return sum([fantasy_draw.total_points(for_round) for fantasy_draw in self.fantasy_draws])

    def explain_points(self):
        return [fantasy_draw.explain_points() for fantasy_draw in self.fantasy_draws]

    def _find_fantasy_draw(self, for_draw):
        return fn.find(partial(self._draw_predicate, for_draw), self.fantasy_draws)

    def _draw_predicate(self, for_draw: Draw, fantasy_draw: Draw):
        return for_draw == fantasy_draw.draw

    def __hash__(self):
        return hash((self.symbolic_name,))

    def __eq__(self, other):
        return self.symbolic_name == other.symbolic_name

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"


class FantasyDraw:
    def __init__(self, draw: Draw, team: Team):
        self.draw = draw
        self.team = team
        self.match_selections = {}

    def show(self, table: Table, for_round: int = None):
        if for_round:
            for mt_id, selection in self.match_selections[1].items():
                selection.show(self.draw.name, table)
        else:
            for rd_id, matches in self.match_selections.items():
                for mt_id, selection in matches.items():
                    selection.show(self.draw.name, table)

    def points_per_round(self, up_to_rd: int = None):
        return [self._sum_round_points(round_selections) for round_selections in
                self._selected_filtered_by_rd(up_to_rd)]

    def _selected_filtered_by_rd(self, up_to_rd: int = None):
        if not up_to_rd:
            return self.match_selections.values()
        return dict(filter(lambda kv: kv[0] <= up_to_rd, self.match_selections.items())).values()

    def _sum_round_points(self, round_selections):
        return sum([sel.points() for sel in round_selections.values()])

    def total_points(self, for_round=None):
        if for_round:
            if for_round not in self.match_selections.keys():
                return 0
            return sum([sel.points() for sel in self.match_selections[for_round].values()])
        return sum([sel.points() for selections in self.match_selections.values() for sel in selections.values()])

    def explain_points(self):
        return {
            "event": self.draw.name,
            "matches": [sel.explain_points() for selections in self.match_selections.values() for sel in
                        selections.values()]
        }

    def match(self, match_id):
        rd_id, mt_id = identity.split_match_id(match_id)
        selection = self._find_match_selection(rd_id, mt_id)
        if not selection:
            selection = Selection(self.draw, rd_id, mt_id)
            self._add_selection(selection, rd_id, mt_id)
        return selection

    def selection_for(self, round_id, match_id):
        return self._find_match_selection(round_id, match_id)

    def _add_selection(self, selection, round_id, match_id):
        if not self.match_selections.get(round_id):
            self.match_selections[round_id] = {}
        self.match_selections[round_id][match_id] = selection
        return self

    def _find_match_selection(self, round_id, match_id):
        return fn.deep_get(self.match_selections, [round_id, match_id])


class Selection:
    def __init__(self, draw, round_id, match_id):
        self.round_id = round_id
        self.match = self._find_match(draw, round_id, match_id)
        self.selected_winner = None
        self.in_number_sets = None
        self.points_strategy = draw.points_strategy
        self.per_round_accum_strategy = draw.round_factor_strategy

    def points(self):
        if not self.match.is_finished():
            return 0
        return self.points_strategy.calc(self, explain=False)

    def explain_points(self):
        if not self.match.is_finished():
            return {
                "match": self.match.match_id,
                "between": f"{self.match.player1.player().name}, {self.match.player2.player().name}" if self.match.has_draw() else None,
                "result-winner": "Not Finished",
                "selected-winner": self.selected_winner.player().name if self.selected_winner else None,
                "selected-in-sets": self.in_number_sets if self.in_number_sets else None,
                "points": []
            }

        return {
            "match": self.match.match_id,
            "between": f"{self.match.player1.player().name}, {self.match.player2.player().name}",
            "result-winner": self.match.match_winner.player().name,
            "result-in-sets": self.match.number_of_sets_played(),
            "selected-winner": self.selected_winner.player().name if self.selected_winner else None,
            "selected-in-sets": self.in_number_sets if self.in_number_sets else None,
            "points": self.points_strategy.calc(self, explain=True)
        }

    def show(self, draw_name: str, table: Table):
        table.add_row(draw_name,
                      self.match.match_id,
                      self.match.match_block(),
                      self.selected_winner.player().name,
                      str(self.in_number_sets))

    def _find_match(self, draw, round_id, match_id):
        return draw.for_round(round_id).for_match(match_id)

    def winner(self, player_name=None):
        if not player_name:
            return self
        if (not isinstance(player_name, Player)) and (not isinstance(player_name, str)):
            return self
        if isinstance(player_name, Player):
            self.selected_winner = self.match.find_player_by_player(player_name, raise_error=False)
        else:
            self.selected_winner = self.match.player_from_player_name(player_name, raise_error=False)
            if not self.selected_winner:
                breakpoint()
        if not isinstance(self.selected_winner, Entry):
            breakpoint()
        return self

    def in_sets(self, number_of_sets=None):
        if not number_of_sets:
            return self
        self.in_number_sets = number_of_sets
        return self

    def has_made_selection(self):
        return self.selected_winner or self.in_number_sets

    def __repr__(self):
        return f"{self.__class__.__name__}(match_id='{self.match.match_id}', winner={self.selected_winner}, in_number_sets={self.in_number_sets})"
