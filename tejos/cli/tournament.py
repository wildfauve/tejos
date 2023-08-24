import click

from tejos.initialiser import environment, db

from tejos import command
from . import helpers


@click.group()
def cli():
    pass


@click.command()
@click.option("--tournament", "-t")  # , type=click.Choice(helpers.tournament_names()))
@click.option("--perma-id", "-p")
def new_tournament(tournament, perma_id):
    """
    """
    command.new_tournament(tournament_name=tournament, perma_id=perma_id)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()))
@click.option("--year", "-y", type=int)
def new_event(tournament, year):
    """
    """
    command.new_event(tournament=helpers.to_tournament(tournament), year=year)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()))
@click.option("--year", "-y", type=int)
@click.option("--name", "-n")
@click.option("--best-of", "-b", type=int)
@click.option("--draw-size", "-s", type=int)
@click.option("--draw-size", "-s", type=int)
@click.option('--fantasy-pt-strat', type=(str, str, str))
def new_draw(tournament, year, name, best_of, draw_size, fantasy_pt_strat):
    """
    """
    command.new_draw(helpers.to_tournament(tournament), year, name, best_of, draw_size, fantasy_pt_strat)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()))
@click.option("--year", "-y", type=int)
@click.option("--draw", "-d")
@click.option("--in-file", "-f")
def add_entries(tournament, year, draw, in_file):
    """
    """
    command.add_entries(helpers.to_tournament(tournament), year, draw, in_file)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()))
@click.option("--year", "-y", type=int)
@click.option("--draw", "-d")
@click.option("--in-file", "-f")
def first_round_draw(tournament, year, draw, in_file):
    """
    """
    command.first_round_draw(helpers.to_tournament(tournament), year, draw, in_file)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()))
@click.option("--year", "-y", type=int)
@click.option("--file", "-f", type=str, default=None, help="Entries class file")
def get_entries(tournament, year, file):
    """
    """
    command.get_entries(tournament=helpers.to_tournament(tournament), year=year, entries_file=file)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()))
@click.option("--year", "-y", type=int)
@click.option("--round", "-r", type=int, default=1, help="The round number to scrap.  Defaults to 1.")
@click.option('--scores-only/--full-draw', "-o/-f", default=False)
def results(tournament, year, round, scores_only):
    """
    """
    command.results(helpers.to_tournament(tournament), year, round, scores_only)
    pass


cli.add_command(new_tournament)
cli.add_command(new_event)
cli.add_command(new_draw)
cli.add_command(add_entries)
cli.add_command(first_round_draw)
cli.add_command(results)
cli.add_command(get_entries)
