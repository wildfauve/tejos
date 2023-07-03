from tejos.fantasy.teams import *
from tejos.players.atp_players import *
from tejos.players.wta_players import *


def team_hero_hangouts(mens_singles, womens_singles):
    TeamHeroHangouts.draw(mens_singles).match("1.1").winner(Khachanov).in_sets(4)
    TeamHeroHangouts.draw(mens_singles).match("1.2").winner(Hurkacz).in_sets(4)
    TeamHeroHangouts.draw(mens_singles).match("1.3").winner(Tsitsipas).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.4").winner(Auger_Aliassime).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.5").winner("Rune").in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.6").winner("Djokovic").in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("1.7").winner("Wolf").in_sets(4)
    TeamHeroHangouts.draw(mens_singles).match("1.8").winner(Bautista_Agut).in_sets(5)

    TeamHeroHangouts.draw(womens_singles).match("1.1").winner(Swiatek).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.2").winner(Gauff).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.3").winner(Krejcikova).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.4").winner(Zhu).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.5").winner(Zhang_Shuai).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.6").winner(Linette).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.7").winner(Sabalenka).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("1.8").winner(Fruhvirtova_Linda).in_sets(3)

    # Quarters
    TeamHeroHangouts.draw(mens_singles).match("2.1").winner(Korda).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("2.2").winner(Lehecka).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("2.3").winner(Djokovic).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("2.4").winner(Paul).in_sets(5)

    TeamHeroHangouts.draw(womens_singles).match("2.1").winner(Ostapenko).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("2.2").winner(Azarenka).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("2.3").winner(Linette).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("2.4").winner(Vekic).in_sets(3)

    # Semis
    TeamHeroHangouts.draw(mens_singles).match("3.1").winner(Khachanov).in_sets(5)
    TeamHeroHangouts.draw(mens_singles).match("3.2").winner(Djokovic).in_sets(3)

    TeamHeroHangouts.draw(womens_singles).match("3.1").winner(Rybakina).in_sets(3)
    TeamHeroHangouts.draw(womens_singles).match("3.2").winner(Sabalenka).in_sets(3)

    # Finals
    TeamHeroHangouts.draw(mens_singles).match("4.1").winner(Tsitsipas).in_sets(4)

    TeamHeroHangouts.draw(womens_singles).match("4.1").winner(Rybakina).in_sets(2)

    return TeamHeroHangouts
