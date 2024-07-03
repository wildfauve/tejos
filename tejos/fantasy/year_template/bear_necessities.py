import sys
from tejos.fantasy.teams import *
from tejos import model
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women
from tejos.players.wta_players import *
from tejos.players.atp_players import *

this = sys.modules[__name__]

TEAM = None

def team():
    this.TEAM = model.Team.get('Bear Necessities')


def team_bear_necessities(mens_singles, womens_singles):
    team()
    helpers.selection_fn_caller(this, [mens_singles, womens_singles])
    return TEAM


# womens_singles_round_7:START

# womens_singles_round_7:END


# mens_singles_round_7:START

# mens_singles_round_7:END

# womens_singles_round_6:START


# womens_singles_round_6:END


# mens_singles_round_6:START

# mens_singles_round_6:END


#womens_singles_round_5:START

#womens_singles_round_5:END

#mens_singles_round_5:START

#mens_singles_round_5:END


# womens_singles_round_4:START

# womens_singles_round_4:END


# mens_singles_round_4:START

# mens_singles_round_4:END


# womens_singles_round_3:START

# womens_singles_round_3:END


# mens_singles_round_3:START

# mens_singles_round_3:END


# womens_singles_round_2:START

# womens_singles_round_2:END


# mens_singles_round_2:START

# mens_singles_round_2:END




# womens_singles_round_1:START

# womens_singles_round_1:END


# mens_singles_round_1:START

# mens_singles_round_1:END

