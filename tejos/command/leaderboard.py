from typing import Dict
from functools import reduce, partial
from itertools import accumulate
from enum import Enum
from rich.console import Console
from rich.table import Table
from rich import box
import polars as pl

from tejos import dataframe, presenter, plot
from tejos.util import fn

console = Console()


def current_leaderboard(tournie,
                        fantasy_teams,
                        round_number=None,
                        accum: bool = True) -> pl.DataFrame:
    return _team_scores_df(tournie, fantasy_teams, accum=accum, up_to_rd=round_number)


def scores_plot(file: str, tournie, fantasy_teams, ranking_plot: bool = False, round_number=None):
    df = _team_scores_df(tournie, fantasy_teams, accum=True, up_to_rd=round_number)

    if ranking_plot:
        return plot.rank_plot(file, tournie, df)
    return plot.total_score_plot(file, tournie, df)


def _team_scores_df(tournie, fantasy_teams, accum: bool, up_to_rd: int = None):
    scores = _format_team_scores(tournie, accum, teams_points_per_round(fantasy_teams, accum, up_to_rd))

    return dataframe.build_df(scores)


def _show_df(df):
    presenter.event_team_scores_table(df)


def _show_old(fantasy_teams, round_number=None):
    table = Table(title=f"Leaderboard For Round {round_number if round_number else 'All'}", box=box.ROUNDED)

    table.add_column("Score", justify="center", style="cyan", no_wrap=True)
    table.add_column("Team", justify="left", style="magenta")

    rankings = sorted_teams(fantasy_teams, round_number)
    breakpoint()

    for team, score in rankings:
        table.add_row(f"{str(score)}", team.name)
    console.print(table)


def find_team_on_board(team, board):
    return fn.find(partial(_team_board_predicate, team), board)


def _team_board_predicate(team, team_on_board):
    return team == team_on_board[0]


def teams_points_per_round(fantasy_teams, accum, up_to_rd):
    if not fantasy_teams:
        return []
    return [(team, _accumulate(_fill(team.points_per_round(up_to_rd), up_to_rd), accum)) for team in fantasy_teams]


def _fill(scores, up_to_rd):
    if not up_to_rd:
        return scores
    [scores.append(0) for _i in range(len(scores), up_to_rd)]
    return scores


def _accumulate(scores, accum: bool):
    if not accum:
        return scores
    return list(accumulate(scores))


def sorted_teams(fantasy_teams, round_number):
    return sorted([(team, team.total_points(round_number)) for team in fantasy_teams], key=lambda t: t[1], reverse=True)


def sorted_f1_teams(fantasy_teams):
    return sorted([team for team in fantasy_teams], key=lambda t: t[1], reverse=True)


def _format_team_scores(tournie, accum: bool, scores):
    # lets remove any teams without scores
    only_teams_with_selections = fn.remove(lambda x: not x[1], scores)
    rd_scores = reduce(partial(_scores_dict, tournie, accum), _transpose_scores(only_teams_with_selections), {})
    return {**{"teams": [team.name for team, _ in only_teams_with_selections]}, **rd_scores}


def _scores_dict(tournie, accum: bool, acc, score_column):
    rd, scores = score_column
    schedule = tournie.fantasy_points_schedule(rd + 1, accum)
    pts_allocation = tournie.fantasy_points_allocation(rd + 1)
    return {**acc, **{f"Round-{rd + 1}\n({schedule[rd]})\n({pts_allocation})": list(scores)}}


def _transpose_scores(scores):
    return enumerate(list(zip(*[points for _, points in scores])))
