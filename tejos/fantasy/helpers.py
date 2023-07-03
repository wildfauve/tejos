import re

def selection_fn_caller(team_module, draws):
    for draw in draws:
        [getattr(team_module, f)(draw) for f in dir(team_module) if  re.match(f"^{draw.fn_symbol}_", f)]