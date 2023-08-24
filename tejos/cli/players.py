import click

from tejos.initialiser import environment, db

from tejos import command
from . import helpers


@click.group()
def cli():
    pass

@click.command()
@click.option("--missing-file", "-f")
def add_missing_players(missing_file):
    """
    """
    command.add_new_players(missing_file)
    pass


cli.add_command(add_missing_players)
