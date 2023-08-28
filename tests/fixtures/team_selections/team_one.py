import sys
from tejos import model
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women
from tejos.players.wta_players import *
from tejos.players.atp_players import *

"""
A suggested change to the API:

TEAM.draw(mens_singles, '3.16').matchup(1, men.Wawrinka, 2, men.Djokovic).select(2).in_sets(3)
"""

this = sys.modules[__name__]

TEAM = None

def team():
    this.TEAM = model.Team.get('Team One')


def team_one(mens_singles, womens_singles):
    team()
    helpers.selection_fn_caller(this, [mens_singles, womens_singles])
    return TEAM


def womens_singles_round_1(_draw):
    return None

def mens_singles_round_1(draw):
    TEAM.draw(draw).match('1.1').winner(Alcaraz).in_sets(3)
    TEAM.draw(draw, '1.2').matchup(1, Rublev, 2, Djokovic).select(1, 4)

