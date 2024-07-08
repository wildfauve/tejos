from dataclasses import dataclass
from typing import Tuple, List
from functools import reduce, partial
import re

import requests
import json
# from bs4 import BeautifulSoup

from tejos import model
from tejos.players import atp_players, wta_players
from tejos.util import fn

draw_map = {
    'Wimbledon2024WomensSingles': {'name': "womens_singles",
                            'player_module': wta_players,
                            'draw_symbol': 'WomensSingles'},
    'Wimbledon2024MensSingles': {'name': "mens_singles",
                          'player_module': atp_players,
                          'draw_symbol': 'MensSingles'}}

round_code_map = {'1': 1,
                  '2': 2,
                  '3': 3,
                  '4': 4,
                  'Q': 5,
                  'S': 6,
                  'F': 7}

draws = [("https://www.wimbledon.com/en_GB/scores/feeds/2024/draws/LS.json", 'Wimbledon2024WomensSingles'),
         ('https://www.wimbledon.com/en_GB/scores/feeds/2024/draws/MS.json', 'Wimbledon2024MensSingles')]

match_ids = {'mens_singles': [], 'womens_singles': []}

COMPLETED = "Completed"
RETIRED = "Retired"
WALKOVER = "Walkover"

@dataclass
class Round:
    uuid: str
    name: str
    rd_number: int

    round_code_map = {'1st Round': 1,
                      '2nd Round': 2,
                      '3rd Round': 3,
                      '4th Round': 4,
                      'Quarterfinals': 5,
                      'Semifinals': 6,
                      'Final': 7}

    @classmethod
    def build(cls, rd):
        return cls(uuid=rd.get('uuid'),
                   name=rd.get('name'),
                   rd_number=cls.round_code_map.get(rd.get('name')))

    @classmethod
    def find_rd(cls, uuid, rounds):
        return fn.find(lambda rd: rd.uuid == uuid, rounds)


ROUNDS: list[Round] = []


@dataclass
class Player:
    uuid: str
    team_id: str
    team: dict
    struct: dict
    seed: int | None

    @classmethod
    def build(cls, data, teams):
        uuid = data.get('uuid')
        team = cls.find_team(uuid, teams)
        if not team:
            breakpoint()
        return cls(uuid=uuid,
                   team_id=team.get('uuid'),
                   team=team,
                   struct=data,
                   seed=team.get('seed'))

    @classmethod
    def find_team(cls, uuid, teams):
        return fn.find(partial(cls.team_player_predicate, uuid), teams)

    @classmethod
    def team_player_predicate(cls, uuid, team):
        return uuid in team.get('players')

    @property
    def full_name(self):
        return self.struct.get('full_name', None)

    def seed_or_entry_status(self):
        if self.seed:
            return self.seed
        es = self.team.get('entry_status')
        return es if not isinstance(es, dict) else es.get('abbr')

PLAYERS = {}



def build_draw(event, for_rd, scores_only, full_draw=False):
    return _assign_match_numbers(_brackets(_get_json(draws, for_rd), event, for_rd, scores_only, full_draw))


def _get_json(urls, for_rd) -> List[Tuple]:
    return [(_get_doc(url, for_rd), draw) for url, draw in urls]


def _get_doc(url_or_file, for_rd):
    if 'http' in url_or_file:
        headers = {'Content-Type': 'application/json', 'User-Agent': 'vscode-restclient'}
        result = requests.get(url_or_file, headers=headers)
        return result.json()
    f = open(url_or_file, "r")
    return json.loads(f.read())


def _brackets(pages, event, for_rd, scores_only, full_draw):
    return reduce(partial(_singles_brackets, event, for_rd, scores_only, full_draw), pages, {})


def _assign_match_numbers(draws):
    for draw, matches in draws.items():
        min_number = min([_match_id_fn(m_id) for m_id in match_ids[draw_map[draw]['name']]])
        for m in matches:
            m.set_match_number_from_1(min_number)
    return draws


def _singles_brackets(event, for_rd, scores_only, full_draw, acc, draw_tuple):
    draw, draw_name = draw_tuple
    # matches = draw.get('matches')
    matches = fn.remove_none(
        [_match(draw_map[draw_name], event, for_rd, scores_only, full_draw, match) for match in draw.get('matches')])
    return {**acc, **{draw_name: matches}}


def _match(draw_mapping, event, for_rd, scores_only, full_draw, match):
    match_id = match.get('match_id')
    match_status = match.get('status')
    rd = round_code_map.get(match.get('roundCode'))
    if for_rd and rd != for_rd:
        return None
    if match_id in match_ids[draw_mapping['name']]:
        return None
    match_ids[draw_mapping['name']].append(match_id)
    match_bloc = model.MatchBlock(href=match_id,
                                  json=match,
                                  round=rd,
                                  draw_attr_name=draw_mapping['name'],
                                  draw_symbol=draw_mapping['draw_symbol'],
                                  event=event,
                                  player1=_player(draw_mapping,
                                                  match.get('team1'),
                                                  team=1,
                                                  scores=match.get('scores'),
                                                  winner=match.get('winner'),
                                                  status=match_status),
                                  player2=_player(draw_mapping,
                                                  match.get('team2'),
                                                  team=2,
                                                  scores=match.get('scores'),
                                                  winner=match.get('winner'),
                                                  status=match_status),
                                  match_id_fn=_match_id_fn)
    if scores_only and match_bloc.has_result() and _match_in_finished_state(match_status):
        return match_bloc
    if full_draw:
        return match_bloc

    return None


def _match_in_finished_state(match_status):
    return match_status in [COMPLETED, RETIRED, WALKOVER]


def _player(draw_mapping, player_content, team, scores, winner, status):
    seed = player_content.get('seed', None) if player_content.get('seed', None) else player_content.get('entryStatus',
                                                                                                        None)
    return model.PlayerResult(name=f"{player_content.get('firstNameA')} {player_content.get('lastNameA')}",
                              seed=seed,
                              match_state=_determine_match_state_exceptions(team, winner, status),
                              player_module=draw_mapping['player_module'],
                              scores=_scores(scores, team))


def _scores(content, team_number):
    sets = content.get('sets', None)
    if not sets:
        return None
    return [set_team_scores[team_number - 1].get('score', None) for set_team_scores in sets]


def _determine_match_state_exceptions(team, winner, status):
    if status == COMPLETED or not winner:
        return None
    if (status == RETIRED or status == WALKOVER) and not winner:
        return model.MatchState(status.lower())
    if status == COMPLETED or not winner:
        return None
    if (status == RETIRED or status == WALKOVER) and winner:
        return None
    breakpoint()
    return None


def _match_id_fn(match_id):
    return int(match_id[2:4])
