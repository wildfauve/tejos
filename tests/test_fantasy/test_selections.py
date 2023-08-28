from pathlib import Path

from tejos import model

from tejos.players import atp_players


def test_create_selection_using_python_api(configure_repo):
    team = create_team()

    wm2023 = make_event()
    mens_singles = wm2023.for_draw('MensSingles')

    selection1_1 = team.draw(mens_singles).match('1.1').winner(atp_players.Alcaraz).in_sets(3)

    assert selection1_1.selected_winner.player() == atp_players.Alcaraz
    assert selection1_1.in_number_sets == 3

    selection1_2 = team.draw(mens_singles, '1.2').matchup(1, atp_players.Rublev, 2, atp_players.Djokovic).select(1, 4)

    assert selection1_2.selected_winner.player() == atp_players.Rublev
    assert selection1_2.in_number_sets == 4

def test_create_selection_from_calling_python_function(configure_repo):
    team = create_team()

    wm2023 = make_event()
    mens_singles = wm2023.for_draw('MensSingles')
    womens_singles = wm2023.for_draw('WomensSingles')

    from tejos.fantasy import selections
    from tests.fixtures import team_selections

    selections.apply(team_selections, mens_singles, womens_singles)

    sel = team.load_all_selections(wm2023)
    assert len(sel) == 2

    assert {s.selected_winner.player().klass_name for s in sel} == {"Alcaraz", "Rublev"}

    # lets just make sure of idempotency
    selections.apply(team_selections, mens_singles, womens_singles)

    sel = team.load_all_selections(wm2023)
    assert len(sel) == 2

    assert {s.selected_winner.player().klass_name for s in sel} == {"Alcaraz", "Rublev"}






def test_create_selection_using_python_dict(configure_repo):
    team = create_team()
    wm2023 = make_event()

    selection = team.make_selection(selection_dict(wm2023))

    assert selection.selected_winner.player() == atp_players.Alcaraz
    assert selection.in_number_sets == 3


def test_create_selection_from_selection_file(configure_repo):
    team = create_team()
    wm2023 = make_event()

    assert not team.fantasy_draws

    team.apply_new_selections(wm2023, 1, Path("tests/fixtures/"))

    selection = team.fantasy_draws[0].match("1.1")

    assert selection.selected_winner.player() == atp_players.Alcaraz
    assert selection.in_number_sets == 3


def test_load_team_selections(configure_repo):
    team = create_team()
    wm2023 = make_event()
    team.make_selection(selection_dict(wm2023))

    same_team = model.Team.get("Team One")

    assert same_team == team
    assert not same_team.fantasy_draws
    selections = same_team.load_all_selections(wm2023)
    assert len(same_team.fantasy_draws) == 1

    breakpoint()

    assert len(selections) == 1
    selection = selections[0]
    assert selection.selected_winner.player() == atp_players.Alcaraz
    assert selection.in_number_sets == 3

    in_fantasy_draw_selection = same_team.fantasy_draws[0].match_selections[1][1]
    assert in_fantasy_draw_selection == selection


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


# Helpers

def selection_dict(event):
    matchup = {1: 'Alcaraz', 2: 'Tsitsipas'}

    return {'event': event,
            'draw': "MensSingles",
            'match': '1.1',
            'matchup': matchup,
            'winner': 'Alcaraz',
            'in_sets': 3}


def make_event():
    wm2023 = create_event()

    (wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)
     .add_entries(entries())
     .init_draw()
     .first_round_draw(first_round_draw()))

    (wm2023.make_draw(name="WomensSingles", best_of=3, draw_size=4)
     .add_entries(entries())
     .init_draw()
     .first_round_draw(first_round_draw()))

    return wm2023


def create_team():
    return model.Team.create("Team One", "a, b, c")


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
