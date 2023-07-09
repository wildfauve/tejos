from functools import reduce
import csv

import polars as pl

from tejos.model import draw
from . import leaderboard
from tejos.fantasy import teams, selections
from tejos.majors import tournaments
from tejos import fantasy, dataframe
from tejos.util import echo
from tejos.util.data_scrapping import atp_rankings, draw_parser


def leaderboard_df(tournament_name, board_type, round_number=None) -> pl.DataFrame:
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return

    return leaderboard.current_leaderboard(tournie, _apply_fantasy(_start(tournie)), board_type, round_number)


def show_round(tournament_name, draw_name, round_number):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    _start(tournie)
    for_draw = draw.find_draw(draw_name, tournie.draws)
    if not for_draw:
        echo.echo(f"Draw with name {draw_name} not found in {tournie.label}")
    for_draw.for_round(round_number).show()


def rank_plot(file: str, tournament_name: str, ranking_plot: bool):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    leaderboard.scores_plot(file, tournie, _apply_fantasy(_start(tournie)), ranking_plot)
    pass


def result_template(tournament_name, draw_name, round_number, template_name):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    _start(tournie)
    for_draw = draw.find_draw(draw_name, tournie.draws)
    if not for_draw:
        echo.echo(f"Draw with name {draw_name} not found in {tournie.label}")
        return
    results = for_draw.for_round(round_number).result_template(template_name)
    for result in results:
        echo.echo(result)


def fantasy_score_template(tournament_name, round_number, trim_with="TeamFauve"):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    if not trim_with:
        _start(tournie)
    else:
        trim_team = teams.find_team_by_name(trim_with, _apply_fantasy(_start(tournie)))
    results = {}
    for for_draw in tournie.draws:
        trim_team_draw = trim_team.draw(for_draw) if trim_team else None
        results[for_draw.fn_symbol] = (for_draw.for_round(round_number)
                                       .fantasy_score_template(for_draw.fn_symbol,
                                                               trim_team_draw=trim_team_draw))
    return results


def fantasy_score_template_inserter(tournament_name, round_number):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    fantasy_module = _fantasy_module(tournie)
    teams = _apply_fantasy(_start(tournie))
    results = reduce(lambda accum, team: {**accum, **{team: {}}}, teams, {})
    for for_draw in tournie.draws:
        for team in teams:
            round_template = f"{for_draw.fn_symbol}_round_{round_number}"
            results[team][round_template] = (for_draw.for_round(round_number)
                                             .fantasy_score_template(for_draw.fn_symbol,
                                                                     trim_team_draw=team.draw(for_draw),
                                                                     add_selected=True,
                                                                     features=team.features))
    return fantasy_module, results


def atomic_points_for_all_teams(tournament_name):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    return dataframe.explain_df_builder(tournie, teams.points_details_all_teams(_apply_fantasy(_start(tournie))))


def explain_team_points(tournament_name, team_name):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    return teams.explain_points_for_team(team_name, _apply_fantasy(_start(tournie)))


def generate_graph(ttl_file):
    graph_generator.generate(ttl_file)


def player_scrap(file):
    atp_rankings.build_players_file(file)


def draw_scrap(tournament, entries_file, draws_file, results, round_number, scores_only):
    tournie = _find_tournament_by_name(tournament)
    tournie_module = _tournament_module(tournie)
    rd_results = draw_parser.build_draw(tournament=tournament,
                                        entries_file=entries_file,
                                        draws_file=draws_file,
                                        generate_results=results,
                                        for_round=round_number,
                                        scores_only=scores_only)

    return tournie_module, rd_results


def show_draw(tournament_name, team_name, round):
    tournie = _find_tournament_by_name(tournament_name)
    if not tournie:
        return
    teams.show_draw_for_team(team_name, _apply_fantasy(_start(tournie)), round)
    pass


# Helpers

def _start(tournie):
    return tournie


def _apply_fantasy(tournie):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, tournie.draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, tournie.draws)

    fantasy_module = _fantasy_module(tournie)

    if not fantasy_module:
        echo.echo(f"No fantasy selections for {tournie.name}")
        return

    return selections.apply(fantasy_module, mens_singles, womens_singles)


def _fantasy_module(tournie):
    return fantasy.fantasy_tournaments.get(tournie.name, None)


def _tournament_module(tournie):
    return tournaments.tournament_module_name(tournie.name)


def _find_tournament_by_name(for_name: str):
    """
    imports tournament modules only when being used on the CLI.
    """
    tournie = tournaments.tournament_in_fantasy(for_name)
    if not tournie:
        echo.echo(f"{for_name} does not exist as a tournament")
    return tournie
