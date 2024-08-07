from typing import Tuple
import csv

from tejos import model, adapter, config
from tejos.util import monad
from tejos.players import atp_players, wta_players

from . import helpers, commanda


@commanda.command(graph_names=['tejos_graph'])
def new_tournament(tournament_name, perma_id) -> monad.EitherMonad[model.GrandSlam]:
    wm = model.GrandSlam.create(name=tournament_name, subject_name=tournament_name, perma_id=perma_id)
    if not wm:
        breakpoint()
    return monad.Right(wm)


@commanda.command(graph_names=['tejos_graph'])
def new_event(tournament, year):
    ev = tournament.make_event(year)

    if not ev:
        breakpoint()
    return monad.Right(ev)


@commanda.command(graph_names=['tejos_graph'])
def new_draw(tournament, year, draw_name, best_of, draw_size, fantasy_pt_strat: Tuple = None):
    event = tournament.for_year(year, load=True)
    if not event:
        return monad.Left(event)

    draw = event.make_draw(name=draw_name,
                           best_of=best_of,
                           draw_size=draw_size,
                           points_strategy_components=fantasy_pt_strat)

    if draw:
        draw.init_draw()
        return monad.Right(draw)


def get_entries(tournament, year, entries_file):
    event = tournament.for_year(year, load=True)
    parser = _get_adapter(tournament)
    if not parser:
        return monad.Left("No Parser Adapter found")
    result = event.get_full_draw(parser)
    return monad.Right(result)


@commanda.command(graph_names=['tejos_graph'])
def add_entries(tournament, year, draw_name, in_file):
    event = tournament.for_year(year, load=True)

    if not event:
        return monad.Left(event)

    draw = model.Draw.get(event=event, name=draw_name)
    entries = []
    with open(in_file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader, None)
        for _player_name, player_klass_name, seed in reader:
            player = _get_player(draw_name, player_klass_name)
            if not player:
                breakpoint()
            entries.append((player, seed))
    draw.add_entries(entries)
    return monad.Right(draw)


@commanda.command(graph_names=['tejos_graph'])
def first_round_draw(tournament, year, draw_name):
    event = tournament.for_year(year, load=True)

    if not event:
        return monad.Left(event)

    first_round_draws = event.get_full_draw()

    draw = model.Draw.get(event=event, name=draw_name)

    rd1 = first_round_draws.get(f"{event.name}{draw_name}", None)
    if not rd1:
        breakpoint()

    first_rd = []
    for matchup in rd1:
        matchup.match_number
        if not matchup.player1.player_klass or not matchup.player2.player_klass:
            breakpoint()
        first_rd.append((int(matchup.match_number), matchup.player1.player_klass, matchup.player2.player_klass))

    draw.first_round_draw(first_rd)
    return monad.Right(draw)


@commanda.command(graph_names=['tejos_graph'])
def results(tournament, year, round_number, scores_only):
    event = tournament.for_year(year, load=True)

    parser = _get_adapter(tournament)
    if not parser:
        return monad.Left("No Parser Adapter found")

    rd_results = model.results(event=event,
                               draw_parser=parser,
                               for_round=round_number,
                               scores_only=scores_only)
    return monad.Right(event)


def _get_player(draw_name, player_klass_name):
    if draw_name == "MensSingles":
        return getattr(atp_players, player_klass_name, None)
    return getattr(wta_players, player_klass_name, None)


def _get_adapter(tournament):
    return config.tournament_adapters.get(tournament.name, None)