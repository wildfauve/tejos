from typing import Tuple
import csv

from tejos import model
from tejos.util import monad
from tejos.players import atp_players, wta_players

from . import helpers, commanda


@commanda.command(graph_names=['players'])
def add_new_players(missing_player_file):
    with open(missing_player_file, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for player_name, tour in reader:
            player = model.Player.create(player_name, tour)
    breakpoint()
    return monad.Right(None)

