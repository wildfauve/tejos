from typing import Tuple
from functools import reduce, partial
import re

import requests
from bs4 import BeautifulSoup

from tejos import model
from tejos.players import atp_players, wta_players
from tejos.util import fn

from tejos.util.data_scrapping import value

match_id_pattern = re.compile('matches\\/\\d+\\/\\w{2}(\\d+)')

draw_map = {
    'FO2023WomensSingles': {'name': "womens_singles",
                            'player_module': wta_players,
                            'url_pattern': '/en-us/matches/2023/SD'},
    'FO2023MensSingles': {'name': "mens_singles",
                          'player_module': atp_players,
                          'url_pattern': '/en-us/matches/2023/SM'},
    'FO2023QualMensSingles': {'name': "qual_mens_singles",
                              'player_module': atp_players,
                              'url_pattern': '/en-us/matches/2023/QM'}
}

round_map = {'first round': 1,
             'second round': 2,
             'third round': 3,
             'fourth round': 4,
             'quarterfinals': 5,
             'semifinals': 6,
             'final': 7}

draws = [("https://www.rolandgarros.com/en-us/results/SM?round={}", 'FO2023MensSingles'),
         ("https://www.rolandgarros.com/en-us/results/SD?round={}", 'FO2023WomensSingles')]

match_ids = {'mens_singles': [], 'womens_singles': []}

def build_draw(for_rd, scores_only):
    return _assign_match_numbers(_brackets(_get_pages(draws, for_rd), for_rd, scores_only))


def _get_pages(urls, for_rd):
    return [(_get_page(url, for_rd), draw) for url, draw in urls]


def _get_page(url_or_file, for_rd):
    if 'http' in url_or_file:
        return BeautifulSoup(requests.get(url_or_file.format(for_rd)).text, "html.parser")
    return BeautifulSoup(open(url_or_file, encoding='UTF-8'), "html.parser")


def _brackets(pages, for_rd, scores_only):
    return reduce(partial(_singles_brackets, for_rd, scores_only), pages, {})


def _assign_match_numbers(draws):
    for draw, matches in draws.items():
        min_number = min([_match_id_fn(m_id) for m_id in match_ids[draw_map[draw]['name']]])
        for m in matches:
            m.set_match_number_from_1(min_number)
    return draws

def _singles_brackets(for_rd, scores_only, acc, draw_tuple):
    draw, draw_name = draw_tuple
    links = draw.find_all('a')
    matches = [x for x in links if x.get('href') and draw_map[draw_name]['url_pattern'] in x.get('href')]

    matches = sorted(fn.remove_none(map(partial(_match, draw_map[draw_name], for_rd, scores_only), matches)),
                     key=lambda m: m.href)

    return {**acc, **{draw_name: matches}}


def _match(draw_mapping, for_rd, scores_only, match_html):
    match_id = match_html.get('href')
    rd = _round(match_html)
    if for_rd and rd != for_rd:
        return None
    if match_id in match_ids[draw_mapping['name']]:
        return None
    match_ids[draw_mapping['name']].append(match_id)

    bloc = match_html.find('div', class_='player-bloc')
    match_bloc = value.MatchBlock(href=match_id,
                                  html=bloc,
                                  round=rd,
                                  draw_attr_name=draw_mapping['name'],
                                  player1=_player_and_scoring_bloc(draw_mapping, bloc, 'team-a-content'),
                                  player2=_player_and_scoring_bloc(draw_mapping, bloc, 'team-b-content'),
                                  match_id_fn=_match_id_fn)
    if scores_only and not match_bloc.has_result():
        return None
    return match_bloc


def _player_and_scoring_bloc(draw_mapping, player_bloc, klass):
    bloc = player_bloc.find('div', class_=klass)
    return _player(draw_mapping, bloc)


def _round(match_html):
    rd_div = match_html.find('div', class_='roundLabel')
    if not rd_div:
        return None
    rd = rd_div.text.lstrip().rstrip()
    if rd not in round_map.keys():
        breakpoint()
    return round_map[rd]


def _player(draw_mapping, content):
    seed_content = content.find('span', class_='num')
    if seed_content:
        seed = seed_content.text.replace(")", "").replace("(", "")
    else:
        seed = None

    name = content.find('div', class_='name').text.lstrip().rstrip()
    scores = [s.contents[0] for s in content.find_all('div', class_='set')]
    return value.Player(name=name,
                        seed=seed,
                        match_state=_determine_match_state_exceptions(content),
                        player_module=draw_mapping['player_module'],
                        scores=scores)


def _determine_match_state_exceptions(content):
    if content('span', class_='abandon'):
        return model.MatchState.RET
    if content('span', class_='forfait'):
        return model.MatchState.WITHDRAWN
    return None


def _match_id_fn(match_id):
    mtch_id = re.search(match_id_pattern, match_id)
    if not mtch_id:
        breakpoint()
    return int(mtch_id[1])
