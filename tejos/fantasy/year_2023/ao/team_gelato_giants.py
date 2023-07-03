from tejos.fantasy.teams import *
from tejos.players.atp_players import *
from tejos.players.wta_players import *


def team_gelato_giants(mens_singles, womens_singles):
    TeamGelatoGiants.draw(mens_singles).match("1.1").winner(Nishioka).in_sets(4)
    TeamGelatoGiants.draw(mens_singles).match("1.2").winner(Korda).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.5").winner(Rublev).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("1.6").winner(Djokovic).in_sets(4)
    TeamGelatoGiants.draw(mens_singles).match("1.7").winner(Wolf).in_sets(3)

    TeamGelatoGiants.draw(mens_singles).match("1.8").winner(Bautista_Agut).in_sets(4)

    TeamGelatoGiants.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamGelatoGiants.draw(womens_singles).match("1.2").winner(Gauff).in_sets(2)
    TeamGelatoGiants.draw(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamGelatoGiants.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.5").winner(Pliskova).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.6").winner(Linette).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("1.8").winner(Vekic).in_sets(2)

    # Quarters
    TeamGelatoGiants.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(4)
    TeamGelatoGiants.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamGelatoGiants.draw(mens_singles).match("2.4").winner(Shelton).in_sets(4)

    TeamGelatoGiants.draw(womens_singles).match("2.1").winner(Rybakina).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("2.2").winner(Pegula).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(2)

    # Semis
    TeamGelatoGiants.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(5)
    TeamGelatoGiants.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamGelatoGiants.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(3)
    TeamGelatoGiants.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(2)

    # Finals
    TeamGelatoGiants.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(3)

    TeamGelatoGiants.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(2)

    return TeamGelatoGiants
