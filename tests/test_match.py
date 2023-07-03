from tests.shared import *

from tejos.model import draw


def test_create_match(test_tournament):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    assert len(mens_singles.rounds) == 2

    r1_m1, r1_m2 = mens_singles.for_round(1).matches

    assert r1_m1.number == 1
    assert r1_m1.match_id == "1.1"
    assert r1_m1.player1.player() == atp_players.Hurkacz
    assert r1_m1.player2.player() == atp_players.Khachanov
    assert r1_m2.number == 2
    assert r1_m2.match_id == "1.2"
    assert r1_m2.player1.player() == atp_players.Korda
    assert r1_m2.player2.player() == atp_players.Tsitsipas

    r2_m1, = mens_singles.rounds[1].matches

    assert r2_m1.number == 1
    assert r2_m1.match_id == "2.1"
    assert not r2_m1.player1


def test_results(test_tournament):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    (mens_singles
     .for_round(1)
     .for_match(1)
     .score(atp_players.Hurkacz, (6, 4, 6, 4, 6))
     .score(atp_players.Khachanov, (4, 6, 4, 6, 4)))

    mt1 = mens_singles.for_round(1).for_match(1)

    assert mt1.is_finished()
    assert mt1.winner().player() == atp_players.Hurkacz

    next_rd_mt = mens_singles.for_round(2).for_match(1)
    assert next_rd_mt.player1.player() == atp_players.Hurkacz
    assert not next_rd_mt.player2

    # When game not finished
    mens_singles.for_round(1).for_match(2).score(atp_players.Korda, (6, 3, 6)).score(atp_players.Tsitsipas, (4, 6, 4))

    mt2 = mens_singles.for_round(1).for_match(2)

    assert not mt2.is_finished()

    assert not next_rd_mt.player2
    assert not next_rd_mt.is_finished()


def test_results_when_not_max_sets(test_tournament):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    (mens_singles
     .for_round(1)
     .for_match(1)
     .score(atp_players.Hurkacz, (6, 6, 6))
     .score(atp_players.Khachanov, (4, 4, 4)))

    mt1 = mens_singles.for_round(1).for_match(1)

    assert mt1.is_finished()
    assert mt1.winner().player() == atp_players.Hurkacz


def test_show_round_matches(capsys, test_tournament):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)
    rd = mens_singles.for_round(1)

    rd.show()

    captured = capsys.readouterr()

    expected_output = """Round: 1
Matches:
1.1  -- ( 10) H. Hurkacz 
        ( 18) K. Khachanov 
1.2  -- ( 29) S. Korda 
        (  3) S. Tsitsipas 
"""

    assert expected_output in captured.out


def test_show_round_matches_with_scores(capsys, test_tournament):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    rd = mens_singles.for_round(1)

    rd.for_match(1).score(atp_players.Hurkacz, (6, 6, 6)).score(atp_players.Khachanov, (4, 4, 4))

    rd.show()

    captured = capsys.readouterr()

    expected_output = """Round: 1
Matches:
1.1  -- ( 10) H. Hurkacz 6 6 6  <
        ( 18) K. Khachanov 4 4 4  
1.2  -- ( 29) S. Korda 
        (  3) S. Tsitsipas 
"""
    assert expected_output in captured.out


def test_result_template(capsys, test_tournament):
    mens_singles = draw.find_draw_by_cls(draw.MensSingles, test_tournament.draws)

    results = mens_singles.for_round(1).result_template("mens_singles")

    expected = ['mens_singles.for_round(1).for_match(1).score(H. Hurkacz, ()).score(K. Khachanov, ())',
                'mens_singles.for_round(1).for_match(2).score(S. Korda, ()).score(S. Tsitsipas, ())']

    assert results == expected
