from tejos import model
from tejos.players import atp_players


def test_create_selection(configure_repo):
    team = create_team()

    wm2023 = make_event()
    mens_singles = wm2023.for_draw('MensSingles')

    selection1_1 = team.draw(mens_singles).match('1.1').winner(atp_players.Alcaraz).in_sets(3)

    assert selection1_1.selected_winner.player() == atp_players.Alcaraz
    assert selection1_1.in_number_sets == 3

    selection1_2 = team.draw(mens_singles, '1.2').matchup(1, atp_players.Rublev, 2, atp_players.Djokovic).select(1, 4)

    assert selection1_2.selected_winner.player() == atp_players.Rublev
    assert selection1_2.in_number_sets == 4


def test_update_selection(configure_repo):
    team = create_team()

    wm2023 = make_event()
    mens_singles = wm2023.for_draw('MensSingles')

    selection = team.draw(mens_singles).match('1.1').winner(atp_players.Alcaraz, in_sets=3)

    assert selection.selected_winner.player() == atp_players.Alcaraz
    assert selection.in_number_sets == 3

    same_selection = team.draw(mens_singles).match('1.1').winner(atp_players.Tsitsipas, in_sets=4)

    assert selection.selected_winner.player() == atp_players.Tsitsipas
    assert selection.in_number_sets == 4


def make_event():
    wm2023 = create_event()

    (wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)
     .add_entries(entries())
     .init_draw()
     .first_round_draw(first_round_draw()))
    return wm2023


def create_team():
    return model.Team.create("t1", "a, b, c")


def entries():
    return [
        (atp_players.Alcaraz, 1),
        (atp_players.Tsitsipas, 7),
        (atp_players.Rublev, 5),
        (atp_players.Djokovic, 3),
        (atp_players.Rune, 4),
        (atp_players.Berrettini, 6),
        (atp_players.Eubanks, 8),
        (atp_players.Sinner, 2),
    ]


def first_round_draw():
    return [
        (1, atp_players.Alcaraz, atp_players.Tsitsipas),
        (2, atp_players.Rublev, atp_players.Djokovic),
        (3, atp_players.Rune, atp_players.Berrettini),
        (4, atp_players.Eubanks, atp_players.Sinner),
    ]


def create_event():
    wm = model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
    return wm.make_event(2023)
