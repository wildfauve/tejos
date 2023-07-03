from tejos.fantasy.teams import *
from tejos.players.atp_players import *
from tejos.players.wta_players import *

def team_fauve(mens_singles, womens_singles):
    TeamFauve.draw(mens_singles).match("1.1").winner("Khachanov").in_sets(3)
    TeamFauve.draw(mens_singles).match("1.2").winner("Hurkacz").in_sets(3)
    TeamFauve.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamFauve.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(4)
    TeamFauve.draw(mens_singles).match("1.5").winner("Rublev").in_sets(5)
    TeamFauve.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(3)
    TeamFauve.draw(mens_singles).match("1.7").winner("Shelton").in_sets(4)
    TeamFauve.draw(mens_singles).match("1.8").winner("Bautista Agut").in_sets(5)

    TeamFauve.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(2)
    TeamFauve.draw(womens_singles).match("1.2").winner(Ostapenko).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.3").winner(Pegula).in_sets(2)
    TeamFauve.draw(womens_singles).match("1.4").winner(Azarenka).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.5").winner(Zhang_Shuai).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.6").winner(Garcia).in_sets(2)
    TeamFauve.draw(womens_singles).match("1.7").winner(Bencic).in_sets(3)
    TeamFauve.draw(womens_singles).match("1.8").winner(Fruhvirtova_Linda).in_sets(3)

    # Quarters
    TeamFauve.draw(mens_singles).match("2.1").winner(Khachanov).in_sets(4)
    TeamFauve.draw(mens_singles).match("2.2").winner(Tsitsipas).in_sets(4)
    TeamFauve.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(3)
    TeamFauve.draw(mens_singles).match("2.4").winner(Shelton).in_sets(5)

    TeamFauve.draw(womens_singles).match("2.1").winner(Rybakina).in_sets(3)
    TeamFauve.draw(womens_singles).match("2.2").winner(Azarenka).in_sets(3)
    TeamFauve.draw(womens_singles).match("2.3").winner(Pliskova).in_sets(3)
    TeamFauve.draw(womens_singles).match("2.4").winner(Sabalenka).in_sets(2)

    # Semis
    TeamFauve.draw(mens_singles).match("3.1").winner(Tsitsipas).in_sets(4)
    TeamFauve.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(4)

    TeamFauve.draw(womens_singles).match("3.1").winner(Azarenka).in_sets(2)
    TeamFauve.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(2)

    # Finals
    TeamFauve.draw(mens_singles).match("4.1").winner(Djokovic).in_sets(3)

    TeamFauve.draw(womens_singles).match("4.1").winner(Sabalenka).in_sets(3)

    return TeamFauve

