import click

from tejos.initialiser import environment, db

from tejos import command, presenter
from tejos.majors import tournaments
from tejos.fantasy import teams


def tournament_names():
    return tournaments.tournament_names()


@click.group()
def cli():
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--round", "-r", type=int, default=None, help="Leaderboard for specific round")
@click.option("--board-type", "-b",
              type=click.Choice(['f1', 'fantasy']),
              default='fantasy',
              help="Either the Fantasy Leaderboard or the F1 leaderboard")
@click.option("--to-discord/--to-shell", "-d/-s", required=True, default=False, help="To discord or to the shell")
def leaderboard(tournament, round, board_type, to_discord):
    """
    Starts the tournament,  applies the results, applies the fantasy selection and prints the leaderboard
    """
    presenter.event_team_scores_table(
        command.leaderboard_df(tournament, command.BoardType(board_type), round),
        to_discord
    )
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--fantasy-team-name", "-f",
              type=click.Choice(teams.symbolised_names()),
              help="team name to explain points")
@click.option("--round_number", "-r", type=int, default=None, help="Leaderboard for specific round")
def show_draw(tournament, fantasy_team_name, round_number):
    command.show_draw(tournament_name=tournament, round=round_number, team_name=fantasy_team_name)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--draw", "-d",
              type=click.Choice(['MensSingles', 'WomensSingles']),
              default='MensSingles',
              help="Show the state of a round for an event.")
@click.option("--round", "-r", type=int, default=1, help="The round number to show.")
def show_round(tournament, round, draw):
    """
    Shows the round of an event
    """
    command.show_round(tournament, draw, round)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--round_number", "-r", type=int, default=1, help="The round number to show.")
@click.option("--draw", "-d",
              type=click.Choice(['MensSingles', 'WomensSingles']),
              default='MensSingles',
              help="Show the state of a round for an event.")
@click.option("--template_name", "-n",
              type=click.Choice(['mens_singles', 'womens_singles']),
              default='mens_singles',
              help="A result template to cut and paste")
def result_template(tournament, round_number, draw, template_name):
    """
    Get a result DSL template
    """
    command.result_template(tournament, draw, round_number, template_name)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--round", "-r", type=int, default=1, help="The round number to show.")
@click.option("--fmt", "-f",
              type=click.Choice(['py', 'csv']),
              default='py',
              help="PY or CSV")
@click.option("--trim-team", "-m",
              type=click.Choice(teams.symbolised_names()),
              help="Team to trim the score template by, when team has already made selection.",
              required=False)
@click.option('--file', '-f', required=False)
def fantasy_score_template(tournament, round, fmt, trim_team, file):
    """
    Get a result DSL template
    """
    presenter.fantasy_score_template(command.fantasy_score_template(tournament, round, trim_team), file)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--round", "-r", type=int, default=1, help="The round number to show.")
@click.option("--fmt", "-f",
              type=click.Choice(['py', 'csv']),
              default='py',
              help="PY or CSV")
def fantasy_score_template_inserter(tournament, round, fmt):
    """
    Get a result DSL template
    """
    presenter.fantasy_score_template_inserter(command.fantasy_score_template_inserter(tournament, round))
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--fantasy-team-name", "-f",
              type=click.Choice(teams.symbolised_names()),
              help="team name to explain points")
@click.option("--to-discord", "channel", required=False, flag_value="to-discord", default=False,
              help="Post the plot to Discord")
def explain_team_score(tournament, fantasy_team_name, channel):
    """
    Shows the round of an event
    """
    presenter.explain(fantasy_team_name, command.explain_team_points(tournament, fantasy_team_name), channel)
    pass


@click.command()
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--file", "-f", type=str, default=None, help="Parquet File Location")
def points_atomic(file, tournament):
    """
    Shows the round of an event
    """
    presenter.to_parquet(file, command.atomic_points_for_all_teams(tournament))
    pass


@click.command()
@click.option("--ttl-file", "-f", type=str, default=None, help="location of TTL Graph output")
def generate_graph(ttl_file):
    """
    Generates TTL Graph
    """
    command.generate_graph(ttl_file)
    pass



@click.option('--file', '-f', required=True)
@click.option("--tournament", "-t",
              type=click.Choice(tournament_names()),
              help="The name of the tournament")
@click.option("--ranking-plot/--accum-totals-plot", "-r/-a", required=True, help="Plot Position, or plot total scores")
@click.option("--to-discord", "channel", required=False, flag_value="to-discord", default=False,
              help="Post the plot to Discord")
@click.command()
def plot(file, tournament, ranking_plot, channel):
    """
    Generate a Ranking Graph
    """
    command.rank_plot(file=file, tournament_name=tournament, ranking_plot=ranking_plot)
    presenter.plot_to_channel(file, channel)
    pass


cli.add_command(leaderboard)
cli.add_command(show_round)
cli.add_command(show_draw)
cli.add_command(explain_team_score)
cli.add_command(result_template)
cli.add_command(generate_graph)
cli.add_command(plot)
cli.add_command(fantasy_score_template)
cli.add_command(fantasy_score_template_inserter)
cli.add_command(points_atomic)
