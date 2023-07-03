from tejos.fantasy.teams import *
from tejos.players.atp_players import *
from tejos.players.wta_players import *


def team_musical_bears(mens_singles, womens_singles):
    TeamMusicalBears.draw(mens_singles).match("1.1").winner(Khachanov).in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.2").winner(Korda).in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.4").winner("Lehecka").in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.5").winner("Rublev").in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamMusicalBears.draw(mens_singles).match("1.7").winner("Wolf").in_sets(4)
    TeamMusicalBears.draw(mens_singles).match("1.8").winner("Paul").in_sets(4)

    TeamMusicalBears.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("1.2").winner(Ostapenko).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.3").winner(Pegula).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.5").winner(Zhang_Shuai).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.6").winner(Garcia).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("1.7").winner(Bencic).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("1.8").winner(Fruhvirtova_Linda).in_sets(2)

    # Quarters
    TeamMusicalBears.draw(mens_singles).match("2.1").winner(Korda).in_sets(5)
    TeamMusicalBears.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(3)
    TeamMusicalBears.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamMusicalBears.draw(mens_singles).match("2.4").winner(Paul).in_sets(5)

    TeamMusicalBears.draw(womens_singles).match("2.1").winner(Ostapenko).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("2.2").winner(Pegula).in_sets(2)
    TeamMusicalBears.draw(womens_singles).match("2.3").winner(Linette).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("2.4").winner(Vekic).in_sets(3)

    # Semis
    TeamMusicalBears.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(5)
    TeamMusicalBears.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamMusicalBears.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(3)
    TeamMusicalBears.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(3)

    # Finals
    TeamMusicalBears.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(4)

    TeamMusicalBears.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(3)

    return TeamMusicalBears

