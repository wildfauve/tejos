from tejos.fantasy.teams import *
from tejos.players.atp_players import *
from tejos.players.wta_players import *


def team_polar_precision(mens_singles, womens_singles):
    TeamPolarPrecision.draw(mens_singles).match("1.1").winner(Nishioka).in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("1.2").winner(Korda).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("1.6").winner(De_Minaur).in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("1.7").winner("Shelton").in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("1.8").winner(Bautista_Agut).in_sets(5)

    TeamPolarPrecision.draw(womens_singles).match("1.1").winner(Rybakina).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.4").winner(Zhu).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.5").winner(Zhang_Shuai).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.7").winner(Bencic).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("1.8").winner(Vekic).in_sets(3)

    # Quarters
    TeamPolarPrecision.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(5)
    TeamPolarPrecision.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("2.4").winner(Shelton).in_sets(5)

    TeamPolarPrecision.draw(womens_singles).match("2.1").winner(Ostapenko).in_sets(2)
    TeamPolarPrecision.draw(womens_singles).match("2.2").winner(Azarenka).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("2.3").winner(Linette).in_sets(3)
    TeamPolarPrecision.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(3)

    # Semis
    TeamPolarPrecision.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(4)
    TeamPolarPrecision.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(4)

    TeamPolarPrecision.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(2)
    TeamPolarPrecision.draw(womens_singles).match("3.2").winner(Linette).in_sets(3)

    # Finals
    TeamPolarPrecision.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(5)

    TeamPolarPrecision.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(3)

    return TeamPolarPrecision

