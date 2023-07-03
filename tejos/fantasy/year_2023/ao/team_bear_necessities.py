from tejos.fantasy.teams import *
from tejos.players.atp_players import *
from tejos.players.wta_players import *


def team_bear_necessities(mens_singles, womens_singles):
    TeamBearNecessities.draw(mens_singles).match("1.1").winner(Khachanov).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.2").winner(Korda).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("1.6").winner(De_Minaur).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.7").winner("Wolf").in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("1.8").winner("Paul").in_sets(5)

    TeamBearNecessities.draw(womens_singles).match("1.1").winner(Rybakina).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.2").winner(Ostapenko).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.3").winner(Krejcikova).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamBearNecessities.draw(womens_singles).match("1.8").winner(Vekic).in_sets(3)

    # Quarters
    TeamBearNecessities.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(5)
    TeamBearNecessities.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamBearNecessities.draw(mens_singles).match("2.4").winner(Shelton).in_sets(5)

    TeamBearNecessities.draw(womens_singles).match("2.1").winner(Rybakina).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("2.2").winner(Pegula).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(3)

    # Semis
    TeamBearNecessities.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(4)
    TeamBearNecessities.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamBearNecessities.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(2)
    TeamBearNecessities.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(2)

    # Finals
    TeamBearNecessities.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(4)

    TeamBearNecessities.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(2)

    return TeamBearNecessities
