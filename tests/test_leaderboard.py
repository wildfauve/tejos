from tejos.command import leaderboard
from tests.shared import *

def test_allocate_points(capsys, test_tournament,  fantasy_team, fantasy_team_2):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, test_tournament.draws)


    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.1").winner(players.Sabalenka).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.2").winner(players.Rybakina).in_sets(3)

    fantasy_team_2.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(5)
    fantasy_team_2.draw(mens_singles).match("1.2").winner(players.Tsitsipas).in_sets(3)
    fantasy_team_2.draw(womens_singles).match("1.1").winner(players.Sabalenka).in_sets(3)
    fantasy_team_2.draw(womens_singles).match("1.2").winner(players.Azarenka).in_sets(3)

    mens_singles.for_round(1).for_match(1).score(players.Hurkacz, (6, 6, 6)).score(players.Khachanov, (4, 4, 4))
    mens_singles.for_round(1).for_match(2).score(players.Korda, (6, 6, 6)).score(players.Tsitsipas, (4, 4, 4))
    womens_singles.for_round(1).for_match(1).score(players.Sabalenka, (6, 6)).score(players.Swiatek, (4, 4))
    womens_singles.for_round(1).for_match(2).score(players.Rybakina, (6, 6)).score(players.Azarenka, (4, 4))

    leaderboard.current_leaderboard([fantasy_team, fantasy_team_2], leaderboard.BoardType.FANTASY)

    captured = capsys.readouterr()

    expected = """Leaderboard:
------------
24  FantasyTeam1
10  FantasyTeam2
"""
    assert expected in captured.out


def test_f1_fantasy(capsys, test_tournament, fantasy_team, fantasy_team_2, fantasy_team_3, fantasy_team_4):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)


    mens_singles.for_round(1).for_match(1).score(players.Hurkacz, (6, 6, 6)).score(players.Khachanov, (4, 4, 4))
    mens_singles.for_round(1).for_match(2).score(players.Korda, (4, 4, 4)).score(players.Tsitsipas, (6, 6, 6))
    mens_singles.for_round(2).for_match(1).score(players.Tsitsipas, (6, 5, 6, 5, 6)).score(players.Hurkacz,
                                                                                           (4, 7, 4, 7, 5))
    
    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(3)
    fantasy_team.draw(mens_singles).match("2.1").winner(players.Hurkacz).in_sets(5)

    fantasy_team_2.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(5)
    fantasy_team_2.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(5)
    fantasy_team_2.draw(mens_singles).match("2.1").winner(players.Hurkacz).in_sets(3)

    fantasy_team_3.draw(mens_singles).match("1.1").winner(players.Khachanov).in_sets(3)
    fantasy_team_3.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(3)
    fantasy_team_3.draw(mens_singles).match("2.1").winner(players.Tsitsipas).in_sets(5)

    fantasy_team_4.draw(mens_singles).match("1.1").winner(players.Khachanov).in_sets(3)
    fantasy_team_4.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(4)
    fantasy_team_4.draw(mens_singles).match("2.1").winner(players.Hurkacz).in_sets(4)

    leaderboard.current_leaderboard([fantasy_team, fantasy_team_2, fantasy_team_3, fantasy_team_4], "f1")

    captured = capsys.readouterr()


    expected = """F1 Leaderboard:
---------------
15  FantasyTeam3
10  FantasyTeam1
8   FantasyTeam2
5   FantasyTeam4
"""

    assert expected in captured.out

