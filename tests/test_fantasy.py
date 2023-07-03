import pytest

from tests.shared import *

from tejos import fantasy
from tejos.util import error


def test_create_pick(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    selection = fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)

    assert len(fantasy_team.fantasy_draws) == 1
    assert fantasy_team.fantasy_draws[0].draw.name == "MensSingles"

    assert selection.match.match_id == "1.1"
    assert selection.selected_winner.player() == players.Hurkacz
    assert selection.in_number_sets == 3



def test_sub_string_of_player_name(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    selection = fantasy_team.draw(mens_singles).match("1.1").winner("urk").in_sets(3)

    assert selection.selected_winner.player() == players.Hurkacz


def test_create_multiple_picks(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(3)

    assert len(fantasy_team.fantasy_draws) == 1
    assert fantasy_team.fantasy_draws[0].draw.name == "MensSingles"

    assert fantasy_team.fantasy_draws[0].selection_for(1, 1).selected_winner.player() == players.Hurkacz
    assert fantasy_team.fantasy_draws[0].selection_for(1, 2).selected_winner.player() == players.Korda


def test_multiple_picks_multiple_events(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, test_tournament.draws)

    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.1").winner(players.Sabalenka).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.2").winner(players.Rybakina).in_sets(3)

    assert len(fantasy_team.fantasy_draws) == 2

    assert fantasy_team.fantasy_draws[0].draw.name == "MensSingles"
    assert fantasy_team.fantasy_draws[0].selection_for(1, 1).selected_winner.player() == players.Hurkacz
    assert fantasy_team.fantasy_draws[0].selection_for(1, 2).selected_winner.player() == players.Korda

    assert fantasy_team.fantasy_draws[1].draw.name == "WomensSingles"
    assert fantasy_team.fantasy_draws[1].selection_for(1, 1).selected_winner.player() == players.Sabalenka
    assert fantasy_team.fantasy_draws[1].selection_for(1, 2).selected_winner.player() == players.Rybakina


def test_show_event(capsys, test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, test_tournament.draws)

    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.1").winner(players.Sabalenka).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.2").winner(players.Rybakina).in_sets(3)

    fantasy_team.show_draw(mens_singles)

    captured = capsys.readouterr()

    expected_output = """Event: MensSingles
1.1  -- ( 10) H. Hurkacz 
        ( 18) K. Khachanov 
     |_ Selected Winner        : H. Hurkacz
     |_ Selected Number of Sets: 3
1.2  -- ( 29) S. Korda 
        (  3) S. Tsitsipas 
     |_ Selected Winner        : S. Korda
     |_ Selected Number of Sets: 3
"""

    assert expected_output in captured.out


def test_allocate_points(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Tsitsipas).in_sets(5)


    # Match not finished
    assert fantasy_team.total_points() == 0

    # 5 for the right winner, 2 for correct sets
    mens_singles.for_round(1).for_match(1).score(players.Hurkacz, (6, 6, 6)).score(players.Khachanov, (4, 4, 4))
    assert fantasy_team.total_points() == 7

    # 5 for the right winner
    mens_singles.for_round(1).for_match(2).score(players.Korda, (4, 4, 4)).score(players.Tsitsipas, (6, 6, 6))
    assert fantasy_team.total_points() == 12

    # adds 2 points for wrong winner but in max sets
    fantasy_team.draw(mens_singles).match("2.1").winner(players.Hurkacz).in_sets(5)
    mens_singles.for_round(2).for_match(1).score(players.Tsitsipas, (6, 5, 6, 5, 6)).score(players.Hurkacz, (4, 7, 4, 7, 5))

    assert fantasy_team.total_points() == 14


def test_explain_points(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    womens_singles = draw.find_draw_by_cls(draw.WomensSingles, test_tournament.draws)

    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Korda).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.1").winner(players.Sabalenka).in_sets(3)
    fantasy_team.draw(womens_singles).match("1.2").winner(players.Rybakina).in_sets(3)

    mens_singles.for_round(1).for_match(1).score(players.Hurkacz, (6, 6, 6)).score(players.Khachanov, (4, 4, 4))
    mens_singles.for_round(1).for_match(2).score(players.Korda, (4, 4, 4)).score(players.Tsitsipas, (6, 6, 6))

    womens_singles.for_round(1).for_match(1).score(players.Sabalenka, (6, 6)).score(players.Swiatek, (4, 4))
    womens_singles.for_round(1).for_match(2).score(players.Rybakina, (6, 6)).score(players.Azarenka, (4, 4))

    explain = fantasy_team.explain_points()
    assert len(explain) == 2

def test_round_factor(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    fantasy_team.draw(mens_singles).match("1.1").winner(players.Hurkacz).in_sets(3)
    fantasy_team.draw(mens_singles).match("1.2").winner(players.Tsitsipas).in_sets(3)

    mens_singles.for_round(1).for_match(1).score(players.Hurkacz, (6, 6, 6)).score(players.Khachanov, (4, 4, 4))
    mens_singles.for_round(1).for_match(2).score(players.Korda, (4, 4, 4)).score(players.Tsitsipas, (6, 6, 6))

    assert fantasy_team.total_points() == 14

    fantasy_team.draw(mens_singles).match("2.1").winner(players.Tsitsipas).in_sets(5)

    mens_singles.for_round(2).for_match(1).score(players.Tsitsipas, (6, 4, 6, 4, 6)).score(players.Hurkacz, (4, 6, 4, 6, 4))

    assert fantasy_team.total_points() == 28


def test_match_doesnt_exist(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    with pytest.raises(error.ConfigException):
        fantasy_team.draw(mens_singles).match("1.3").winner("Player1").in_sets(3)


def test_round_doesnt_exist(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    with pytest.raises(error.ConfigException):
        fantasy_team.draw(mens_singles).match("4.1").winner("Player1").in_sets(3)


def test_match_has_no_players(test_tournament,  fantasy_team):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    with pytest.raises(error.ConfigException):
        fantasy_team.draw(mens_singles).match("2.1").winner("Player1").in_sets(3)
