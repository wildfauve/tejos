import click

from tejos.initialiser import environment, db

from tejos import command, presenter
from tejos.fantasy import teams

from . import helpers



@click.group()
def cli():
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
@click.option("--round", "-r", type=int, default=None, help="Leaderboard for specific round")
@click.option("--to-discord/--to-shell", "-d/-s", required=True, default=False, help="To discord or to the shell")
def leaderboard(tournament, year, round, to_discord):
    """
    Starts the tournament,  applies the results, applies the fantasy selection and prints the leaderboard
    """
    presenter.event_team_scores_table(command.leaderboard_df(helpers.to_tournament(tournament), year, round), to_discord)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
@click.option("--fantasy-team-name", "-f",
              type=click.Choice(helpers.symbolised_names()),
              help="team name to explain points")
@click.option("--round_number", "-r", type=int, default=None, help="Leaderboard for specific round")
def show_draw(tournament, fantasy_team_name, round_number):
    command.show_draw(tournament=helpers.to_tournament(tournament), round=round_number, team_name=fantasy_team_name)
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()))
@click.option("--year", "-y", type=int)
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
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
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
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
@click.option("--round", "-r", type=int, default=1, help="The round number to show.")
@click.option("--fmt", "-f",
              type=click.Choice(['py', 'csv']),
              default='py',
              help="PY or CSV")
@click.option("--trim-team", "-m",
              type=click.Choice(helpers.symbolised_names()),
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
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
def load_selections(tournament, year):
    command.load_selections(helpers.to_tournament(tournament), year)
    pass

@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
@click.option("--round", "-r", type=int, default=1, help="The round number to show.")
@click.option("--fmt", "-f",
              type=click.Choice(['py', 'csv']),
              default='py',
              help="PY or CSV")
def fantasy_score_template_inserter(tournament, year, round, fmt):
    """
    Get a result DSL template
    """
    presenter.fantasy_score_template_inserter(
        command.fantasy_score_template_inserter(helpers.to_tournament(tournament), year, round))
    pass


@click.command()
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
@click.option("--fantasy-team-name", "-f",
              type=click.Choice(helpers.symbolised_names()),
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
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
@click.option("--file", "-f", type=str, default=None, help="Parquet File Location")
def points_atomic(file, tournament):
    """
    Shows the round of an event
    """
    presenter.to_parquet(file, command.atomic_points_for_all_teams(helpers.to_tournament(tournament)))
    pass



@click.option('--file', '-f', required=True)
@click.option("--tournament", "-t", type=click.Choice(helpers.tournament_names()), )
@click.option("--year", "-y", type=int)
@click.option("--ranking-plot/--accum-totals-plot", "-r/-a", required=True, help="Plot Position, or plot total scores")
@click.option("--round", "-r", type=int, default=None, help="Leaderboard for specific round")
@click.option("--to-discord", "channel", required=False, flag_value="to-discord", default=False,
              help="Post the plot to Discord")
@click.command()
def plot(file, tournament, year, ranking_plot, channel, round):
    """
    Generate a Ranking Graph
    """
    command.rank_plot(file=file,
                      tournament=helpers.to_tournament(tournament),
                      year=year, ranking_plot=ranking_plot,
                      round_number=round)
    presenter.plot_to_channel(file, channel)
    pass

@click.option("--name", "-n", type=str)
@click.option("--members", "-m")
@click.option("--features", "-f")
@click.command()
def create_team(name, members, features):
    """
    Generate a Ranking Graph
    """
    command.create_team(name=name, members=members.split(","), features=features.split(",") if features else [])


cli.add_command(leaderboard)
cli.add_command(show_round)
cli.add_command(show_draw)
cli.add_command(explain_team_score)
cli.add_command(result_template)
cli.add_command(plot)
cli.add_command(fantasy_score_template)
cli.add_command(fantasy_score_template_inserter)
cli.add_command(points_atomic)
cli.add_command(create_team)
cli.add_command(load_selections)
