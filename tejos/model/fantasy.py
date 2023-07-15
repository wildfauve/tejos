from __future__ import annotations
from typing import List, Dict, Union
from functools import partial
from itertools import groupby
import json
from pathlib import Path

from rdflib import Graph, URIRef

from rich.table import Table

from tejos import model, rdf
from tejos.repo import repository

from tejos.util import fn, error, identity, singleton, logger


class Team:
    repo = model.GraphModel2().new(repository.TeamRepo, model.GraphModel2.fantasy_graph)

    @classmethod
    def create(cls, name: str, members: str, features: List[model.FantasyFeature] = None):
        team = cls(name, members, features)
        cls.repo().upsert(team)
        return team

    @classmethod
    def get(cls, name):
        team = cls.repo().find_by_name(name)
        if not team:
            return None
        name, members, features, sub = team
        return cls(name=name, members=members, features=[model.FantasyFeature[feat] for feat in features])

    @classmethod
    def get_all(cls):
        return [cls.to_team(team) for team in cls.repo().get_all()]

    @classmethod
    def to_team(cls, team):
        name, members, features, sub = team
        return cls(name=name, members=members, features=[model.FantasyFeature[feat] for feat in features])

    def __init__(self, name, members, features=None, sub: URIRef = None):
        self.name = name
        self.symbolic_name = name.replace(" ", "")
        self.members = members
        self.fantasy_draws = []
        self.subject = rdf.clo_te_ind_fan[self.symbolic_name] if not sub else sub
        self.result_file_name = name.lower().replace(" ", "_")
        self.features = features if features else []

    def apply_new_selections(self, event: model.TournamentEvent, for_round: int, load_directory: str):
        """
            return {'event': event,
            'draw': "MensSingles",
            'match': '1.1',
            'matchup': matchup,
            'winner': 'Alcaraz',
            'in_sets': 3}

        :return:
        """
        load_file = Path(load_directory) / f"{self.symbolic_name.lower()}_selections.json"
        if not load_file.exists():
            logger.debug(f"{load_file} does not exist")
            return self
        with open(load_file, 'r') as selections_file:
            selections = json.loads(selections_file.read())
            for draw_name, rounds in selections.items():
                for round_number, matchups in rounds.items():
                    if int(round_number) == for_round:
                        for mt, matchup in matchups.items():
                            self.make_selection(self.make_match_up_dict(event, draw_name, round_number, mt, matchup))
                    else:
                        logger.debug(f"{self.name} selection not processed for round {round_number}")

    def make_match_up_dict(self, event, draw_name, rd_num, mt_num, matchup):
        return {
            'event': event,
            'draw': draw_name,
            'match': f"{rd_num}.{mt_num}",
            'winner': matchup['winner'],
            'in_sets': matchup['in_sets']
        }

    def load_all_selections(self, event):
        selections = Selection.get_all_for_team(self, event)
        [self.add_draw_selections(draw, sels) for draw, sels in groupby(selections, lambda sel: sel.draw)]
        return selections

    def add_draw_selections(self, for_draw: model.Draw, sels):
        selections_for_draw = list(sels)
        fan_draw = self.draw(for_draw)
        fan_draw.load_selections(selections_for_draw)
        return self

    def make_selection(self, selection: Dict):
        for_draw = model.Draw.get(selection['event'], selection['draw'])
        if not for_draw:
            breakpoint()
        draw = self.draw(for_draw)
        plr = model.Player.load(klass_name=selection['winner'])
        return draw.match(selection['match']).winner(player_klass_or_name=plr, in_sets=selection['in_sets'])

    def draw(self, for_draw, match_id: str = None):
        fantasy = self._find_fantasy_draw(for_draw)
        if not fantasy:
            fantasy = FantasyDraw(for_draw, self)
            self.fantasy_draws.append(fantasy)
        if match_id:
            return fantasy.match(match_id)
        fantasy.features(self.features)
        return fantasy

    def show_draws(self, for_round: int, table: Table):
        for draw in self.fantasy_draws:
            self.show_draw(draw, table, for_round)

    def show_draw(self, for_draw, table: Table, for_round: int = None):
        for_draw.show(table, for_round)

    def points_per_round(self, up_to_rd: int = None):
        """
        There are only ever 2 draws (mens and womens).  Get the total points for each match in the round in both draws.
        """
        pts = [fantasy_draw.points_per_round(up_to_rd) for fantasy_draw in self.fantasy_draws]
        return [sum(t) for t in zip(*pts)]

    def total_points(self, for_round=None):
        return sum([fantasy_draw.total_points(for_round) for fantasy_draw in self.fantasy_draws])

    def explain_points(self):
        return [fantasy_draw.explain_points() for fantasy_draw in self.fantasy_draws]

    def _find_fantasy_draw(self, for_draw):
        return fn.find(partial(self._draw_predicate, for_draw), self.fantasy_draws)

    def _draw_predicate(self, for_draw, fantasy_draw):
        return for_draw == fantasy_draw.draw

    def __hash__(self):
        return hash((self.symbolic_name,))

    def __eq__(self, other):
        return self.symbolic_name == other.symbolic_name

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"


class FantasyDraw:
    def __init__(self, draw, team: Team):
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

    def load_selections(self, selections: List[Selection]):
        [self._add_selection(selection, selection.round_id, selection.match.number) for selection in selections]
        return self

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
            selection = Selection(draw=self.draw, fantasy_draw=self, round_id=rd_id, match_id=mt_id)
            self._add_selection(selection, rd_id, mt_id)
        return selection

    def features(self, feats: List[model.FantasyFeature]):
        self.fantasy_features = feats
        return self

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
    repo = model.GraphModel2().new(repository.SelectionRepo, model.GraphModel2.fantasy_graph)

    @classmethod
    def upsert(cls, self):
        cls.repo().upsert(self)
        return self

    @classmethod
    def get_all_for_team(cls, team: Team, event: model.TournamentEvent):
        return [cls.to_selection(team, event, sel) for sel in cls.repo().get_all_for_team(team.subject)]

    @classmethod
    def to_selection(cls, team, event, selection):
        sel_sub, match_sub, winner_entry_sub, in_num_sets, pts_strat = selection
        draw_name, for_round, match_id = model.Match.decompose_match_subject(match_sub)
        sel = cls(draw=event.for_draw(draw_name),
                  round_id=for_round,
                  match_id=match_id,
                  team=team,
                  sub=sel_sub)
        return sel.winner(winner_entry_sub, in_sets=in_num_sets)

    def __init__(self, draw, round_id, match_id, team: Team = None, fantasy_draw=None, sub: URIRef = None):
        self.round_id = round_id
        self.match = self._find_match(draw, round_id, match_id)
        self.selected_winner = None
        self.selected_player_number = None
        self.draw = draw
        if fantasy_draw and not sub:
            self.fantasy_draw = fantasy_draw
            self.relative_subject = draw.relative_subject + f"/{self.fantasy_draw.team.symbolic_name}/{round_id}/{match_id}"
            self.subject = rdf.clo_te_ind_fan[self.relative_subject] if not sub else sub
            self.team_subject = self.fantasy_draw.team.subject
        elif not fantasy_draw and (sub and team):
            self.team_subject = team.subject
            self.subject = sub
        else:
            breakpoint()
        self.in_number_sets = None
        self.points_strategy = draw.points_strategy
        # self.per_round_accum_strategy = draw.round_factor_strategy

    def matchup(self, pos1, player1, pos2, player2):
        if not player1 or not player2:
            return self
        if player1 != self.match.player1.player() or player2 != self.match.player2.player():
            breakpoint()
        return self

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

    # def _find_match_by_match_sub(self, match_sub):
    #     return draw.for_round(round_id).for_match(match_id)

    def winner(self, player_klass_or_name=None, player_klass_name: str = None, in_sets: int = None):
        if not player_klass_or_name:
            return self
        if (not isinstance(player_klass_or_name, model.Player)) and (not isinstance(player_klass_or_name, str)):
            return self
        self.selected_winner = self.get_entry_by_player_or_name_or_sub(player_klass_or_name)
        if not self.selected_winner or not isinstance(self.selected_winner, model.Entry):
            breakpoint()
        if in_sets:
            self.in_number_sets = in_sets
        self.__class__.upsert(self)
        return self

    def get_entry_by_player_or_name_or_sub(self,
                                           player: Union[str, model.Player, URIRef]) -> Union[
        model.Entry, error.ConfigException]:
        if isinstance(player, URIRef):
            return self.match.player_from_player_subject(player, raise_error=False)
        if isinstance(player, model.Player):
            return self.match.find_player_by_player(player, raise_error=False)
        if isinstance(player, str):
            return self.match.player_from_player_name(player, raise_error=False)

    def in_sets(self, number_of_sets=None):
        if not number_of_sets:
            return self
        self.in_number_sets = number_of_sets
        return self

    def select(self, player_number=None, in_sets=None):
        if not player_number or not in_sets:
            return self
        winner_number = model.MatchPlayerNumber(player_number)
        if winner_number == model.MatchPlayerNumber.PLAYER1:
            self.winner(self.match.player1.player())
        else:
            self.winner(self.match.player2.player())
        self.in_sets(in_sets)
        self.selected_player_number = winner_number
        return self

    def has_made_selection(self):
        return self.selected_winner or self.in_number_sets

    def __repr__(self):
        return f"{self.__class__.__name__}(match_id='{self.match.match_id}', winner={self.selected_winner}, in_number_sets={self.in_number_sets})"


class TeamDirectory(singleton.Singleton):

    def add_teams(self, teams):
        self.teams = teams

    def symbolic_names(self):
        return [team.symbolic_name for team in self.teams]

    def load_all_selections(self, event):
        [team.load_all_selections(event) for team in self.teams]
        return self


def teams():
    all_teams = model.Team.get_all()
    TeamDirectory().add_teams(all_teams)
    return TeamDirectory()


def load_all_selections(event):
    return TeamDirectory().load_all_selections(event)
