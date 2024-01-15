from typing import Tuple, Dict, Callable
from functools import reduce, partial

from tejos.players import atp_players as players
from tejos import model
from tejos.adapter import ao_draw_parser


def results(event: model.tournament_event.TournamentEvent,
            draw_parser: Callable,
            for_round=None,
            scores_only=False):
    return _add_results(draw_parser.build_draw(event, for_round, scores_only)),



def _add_results(draws):
    results = [_match_result(draw, match_blocks) for draw, match_blocks in draws.items()]
    return results


def _match_result(draw, match_blocks):
    return [match_block.save() for match_block in match_blocks]
