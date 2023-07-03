import re


def apply(fantasy_module, mens_singles, womens_singles):
    return [_apply_selections(fantasy_module, team_fn, mens_singles, womens_singles) for team_fn in
            _apply_functions_for_teams(fantasy_module)]


def _apply_functions_for_teams(fantasy_module):
    return [f for f in dir(fantasy_module) if re.match("^team_", f)]


def _apply_selections(fantasy_module, team_fn, mens_singles, womens_singles):
    return getattr(fantasy_module, team_fn)(mens_singles, womens_singles)
