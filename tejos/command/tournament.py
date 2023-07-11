import csv
from tejos import model

from tejos.util import monad

from tejos.players import atp_players, wta_players

from . import helpers, commanda


@commanda.command()
def new_tournament(tournament_name, perma_id) -> monad.EitherMonad[model.GrandSlam]:
    wm = model.GrandSlam.create(name=tournament_name, subject_name=tournament_name, perma_id=perma_id)
    if not wm:
        breakpoint()
    return monad.Right(wm)


@commanda.command()
def new_event(tournament_name, year):
    tournie = _tournie(tournament_name)
    if not tournie:
        return monad.Left(tournie)

    ev = tournie.make_event(year)

    if not ev:
        breakpoint()
    return monad.Right(ev)


@commanda.command()
def new_draw(tournament_name, year, draw_name, best_of, draw_size):
    tournie = _tournie(tournament_name)
    event = model.TournamentEvent.get(tournament=tournie, year=year)
    if not event:
        return monad.Left(event)

    draw = event.make_draw(name=draw_name, best_of=best_of, draw_size=draw_size)

    if draw:
        draw.init_draw()
        return monad.Right(draw)


@commanda.command()
def add_entries(tournament_name, year, draw_name, in_file):
    tournie = _tournie(tournament_name)
    event = model.TournamentEvent.get(tournament=tournie, year=year)
    if not event:
        return monad.Left(event)

    draw = model.Draw.get(event=event, name=draw_name)
    entries = []
    with open(in_file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for player_klass_name, seed in reader:
            player = _get_player(draw_name, player_klass_name)
            if not player:
                breakpoint()
            # if "Wang" in player.klass_name:
            #     breakpoint()
            entries.append((player, seed))
    draw.add_entries(entries)
    return monad.Right(draw)


@commanda.command()
def first_round_draw(tournament_name, year, draw_name, in_file):
    tournie = _tournie(tournament_name)
    event = model.TournamentEvent.get(tournament=tournie, year=year)
    if not event:
        return monad.Left(event)

    draw = model.Draw.get(event=event, name=draw_name)


    first_rd = []
    with open(in_file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for match, pl1_klass_name, pl2_klass_name in reader:
            pl1 = _get_player(draw_name, pl1_klass_name)
            pl2 = _get_player(draw_name, pl2_klass_name)
            if not pl1 or not pl2:
                breakpoint()
            first_rd.append((int(match), pl1, pl2))

    draw.first_round_draw(first_rd)
    breakpoint()
    return monad.Right(draw)


def _get_player(draw_name, player_klass_name):
    if draw_name == "MensSingles":
        return getattr(atp_players, player_klass_name, None)
    return getattr(wta_players, player_klass_name, None)


def _tournie(name):
    return model.GrandSlam.get(name=name)
