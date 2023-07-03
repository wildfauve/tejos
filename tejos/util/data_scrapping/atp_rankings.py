from functools import reduce, partial
import requests
from bs4 import BeautifulSoup
# from markdownify import MarkdownConverter, markdownify as md
import argparse
import string

rankings = [('https://nytimes.stats.com/tennis/rankings.asp?tour=ATP&rank=3', 'ATP', '/tennis/players.asp?tour=ATP&id='),
            ('https://nytimes.stats.com/tennis/rankings.asp?tour=WTA&rank=3', 'WTA', '/tennis/players.asp?tour=WTA&id=')]


def build_players_file(file):
    klasses = _format_klasses(_display_dups(_player_links(_get_pages(rankings))))
    _write_file(file, klasses)


def _get_pages(urls):
    return [(BeautifulSoup(requests.get(url).text, "html.parser"), tour, link_pattern) for url, tour, link_pattern in urls]


def _player_links(pages):
    return reduce(_tour_links, pages, [])


def _tour_links(players, page_tuple):
    pg, tour, link_form = page_tuple
    [players.append(_player_model(tour, link)) for link in pg.find_all("a") if link_form in link.get('href')]
    return players


def _display_dups(players):
    klass_names = [name for _, _, name, _ in players]
    dups = {f"Duplicate: {dup} occurances: {klass_names.count(dup)}" for dup in klass_names if
            klass_names.count(dup) > 1}
    for dup in dups:
        print(dup)
    return players


def _player_model(tour, link):
    return (link.get('href'), link.string, _format_klass_name(link.string), tour)


def _format_klass_name(name):
    return name.rstrip().split(' ')[-1].replace("-", "_").replace("'", "")


def _format_klasses(players):
    """
    from tejos.model.player import Player

    Nishioka = Player("Y. Nishioka", tour_symbol="ATP")
    """
    return reduce(partial(_player_def, [player[2] for player in players]), players, _imports_hdr())

def _imports_hdr():
    return "from tejos.model.player import Player\n\n"


def _player_def(players_klass_names, klasses, player):
    link, name, klass_name, tour = player
    if players_klass_names.count(klass_name) > 1:
        klass_name = _deal_with_dup(klass_name, name)
    return klasses + f"{klass_name} = Player(\"{name}\", tour_symbol='{tour}')\n\n"


def _deal_with_dup(klass_name, name):
    first_name = name.split(' ')[0].replace("-", "_").replace("'", "")
    return f"{klass_name}_{first_name}"


def _write_file(file_name, klasses):
    with open(f"{file_name}", 'w') as f:
        f.write(klasses)
