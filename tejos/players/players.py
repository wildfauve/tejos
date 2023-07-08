from functools import partial

from tejos import model
from tejos.util import fn

from . import wta_players, atp_players

player_cache = {'atp_players': [], 'wta_players': []}


def search_player_by_name(name, player_module):
    print(f"finding...{name}")
    result = list(fn.select(partial(_player_finder, name), _player_cache(player_module)))
    if len(result) == 1:
        return result[0]
    if not result:
        return None
    breakpoint()


def _player_finder(name, player):
    return player.search_by_name(name)



def _player_cache(player_module):
    if player_cache[_cache(player_module)]:
        return player_cache[_cache(player_module)]
    attrs = [getattr(player_module, attr) for attr in dir(player_module) if "__" not in attr]
    player_cache[_cache(player_module)] = [attr for attr in attrs if isinstance(attr, model.Player)]
    return player_cache[_cache(player_module)]


def _cache(player_module):
    return player_module.__name__.split(".")[-1]
