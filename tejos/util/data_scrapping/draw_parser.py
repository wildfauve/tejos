from typing import Tuple, Dict
from functools import reduce, partial

from tejos.players import atp_players as players
from tejos import model
from .event_web_parser import wm_parser


def build_draw(tournament: model.tournament_event.TournamentEvent,
               entries_file=None,
               draws_file=None,
               generate_results=False,
               for_round=None,
               scores_only=False):
    return (_format_results(
        _format_brackets(
            _format_entries(
                _parser_for_event(tournament).build_draw(for_round, scores_only),
                entries_file),
            draws_file),
        generate_results,
        for_round,
        tournament))


def results(event: model.tournament_event.TournamentEvent,
            for_round=None,
            scores_only=False):
    _format_results(_parser_for_event(event).build_draw(for_round, scores_only), True, for_round, event),


def _parser_for_event(_tournament):
    return wm_parser


def _format_entries(draws: Dict, entries_file):
    if not entries_file:
        return draws
    py = reduce(_entry_def, draws.items(), _entry_imports_hdr())
    _write_file(entries_file, py)
    return draws


def _format_brackets(draws, draws_file):
    if not draws_file:
        return draws
    py = reduce(_bracket_def, draws.items(), _first_round_draw_def())
    _write_file(draws_file, py)
    return draws


def _format_results(draws, generate_results, for_round, tournament):
    breakpoint()
    if not generate_results:
        return draws
    py = reduce(partial(_results_def, for_round, tournament), draws.items(), {})  # _results_mod_def())
    return py


def _entry_imports_hdr():
    return """from typing import Tuple, List, Optional
from tejos import model
from tejos.players import wta_players, atp_players
"""


def _first_round_draw_def():
    return """from typing import Tuple, List
from tejos.players import wta_players, atp_players
from tejos import model"""


def _results_mod_def():
    return ""


def _entry_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_player_entry, matches, _entry_function(py, draw_name)) + f"\n{']':>4}"


def _bracket_def(py, draw_tuple):
    draw_name, matches = draw_tuple
    return reduce(_players_bracket, matches, _match_function(py, draw_name)) + f"\n{']':>4}"


def _results_def(for_round, tournament, accum, draw_tuple):
    draw_name, matches = draw_tuple
    draw_rd_key = f"{draw_name}_r{for_round}"
    scores = reduce(partial(_match_result, tournament), matches, _result_function(draw_name, for_round))
    scores.append(f"\n{']':>4}")
    accum[draw_rd_key] = scores
    return accum


def _players_bracket(acc, match):
    return acc + match.match_format()


def _match_result(tournament, accum, match):
    match.save(tournament)
    accum.append(match.results_format(f"{'':>8}"))
    return accum


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
