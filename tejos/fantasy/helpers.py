import re
from typing import Callable

from tejos.util import console


def selection_fn_caller(team_module, draws):
    for draw in draws:
        [_apply_draw(team_module, f, draw) for f in dir(team_module) if re.match(f"^{draw.fn_symbol}_", f)]

def _apply_draw(team_module, f: Callable, draw):
    console.cons.print(f"Invoke {team_module.__name__} fn: {f} with draw: {draw}")
    getattr(team_module, f)(draw)
    return None