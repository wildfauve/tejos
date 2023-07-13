from typing import Tuple, Dict
from functools import reduce, partial

from tejos.players import atp_players as players
from tejos import model
from tejos.adapter import wm_draw_parser


def results(event: model.tournament_event.TournamentEvent,
            for_round=None,
            scores_only=False):
    return _add_results(wm_draw_parser.build_draw(event, for_round, scores_only)),



def _add_results(draws):
    results = [_match_result(draw, match_blocks) for draw, match_blocks in draws.items()]
    return results


def _match_result(draw, match_blocks):
    return [match_block.save() for match_block in match_blocks]


def _entry_predicate(bracket_number, entry):
    return int(entry[0]) == bracket_number


def _player_entry(py, match):
    return py + match.entry_format()


def _player_definition(entry: Tuple[str, str, str]):
    if not entry:
        return f"players.NOT-FOUND"
    return f"players.{entry[1].klass_name}"


def _entry_function(py, name):
    return py + f"""
def {'womens_singles_entries()' if "WomensSingles" in name else "mens_singles_entries()"}:
    return [
"""


def _match_function(py, name):
    return py + f"""
def {'womens_draw_round_1()' if "WomensSingles" in name else "mens_draw_round_1()"}:
    return [
"""


def _result_function(name, for_round):
    return [
        f"def womens_singles_results_r{for_round}(draw):" if "WomensSingles" in name else f"def mens_singles_results_r{for_round}(draw):",
        "  return ["
    ]


def _write_file(file_name, klasses):
    with open(f"{file_name}", 'w') as f:
        f.write(klasses)
