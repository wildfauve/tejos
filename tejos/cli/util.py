import click

from tejos import command, presenter
from tejos.majors import tournaments
from tejos.fantasy import teams

from tejos.initialiser import environment


def tournament_names():
    return tournaments.tournament_names()


@click.group()
def cli():
    pass


@click.command()
@click.option("--file", "-f", type=str, default=None, help="Player class file")
def player_scrap(file):
    """
    Generates a player class file from the top 200 from the ATP and WTA
    """
    command.player_scrap(file)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--entries-file", "-e", type=str, default=None, help="Entries class file")
@click.option("--draws-file", "-d", type=str, default=None, help="draws class file")
@click.option("--results/--no-results", default=False, help="generate results to tournament results file")
@click.option("--round", "-r", type=int, default=1, help="The round number to scrap.  Defaults to 1.")
@click.option('--scores-only/--full-draw', "-o/-f", default=False)
def draw_scrap(tournament, entries_file, draws_file, results, round, scores_only):
    """
    """
    presenter.scores_scrap_inserter(command.draw_scrap(tournament=tournament,
                                                       entries_file=entries_file,
                                                       draws_file=draws_file,
                                                       results=results,
                                                       round_number=round,
                                                       scores_only=scores_only))
    pass


cli.add_command(player_scrap)
cli.add_command(draw_scrap)
