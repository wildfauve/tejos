from tejos import model
from tejos import repo
from tejos.players import atp_players


def test_create_event(configure_repo):
    create_tournies()

    event = model.TournamentEvent.create(year=2023, tournament_name="Wimbledon")

    assert event.scheduled_in_year == 2023
    assert event.is_event_of.name == "Wimbledon"

    same_event = model.TournamentEvent.get(tournament=event.is_event_of, year=2023)

    assert same_event == event


def test_make_event_from_tournament(configure_repo):
    tournie = model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")

    event = tournie.make_event(year=2023)

    assert event.scheduled_in_year == 2023
    assert event.is_event_of.name == "Wimbledon"

    exactly_the_same_event = tournie.make_event(year=2023)
    assert id(event) == id(exactly_the_same_event)


def test_get_all_events(configure_repo):
    create_tournies()
    create_events()

    results = model.TournamentEvent.get_all()

    assert len(results) == 4

    expected = {'RolandGarros2023', 'AustralianOpen2023', 'UsOpen2023', 'Wimbledon2023'}
    assert {ev.name for ev in results} == expected

    expected_tournies = {'Wimbledon', 'Roland Garros', 'Australian Open', 'US Open'}
    assert {ev.is_event_of.name for ev in results} == expected_tournies


def test_load_events_draws(configure_repo):
    create_tournie()

    wm2023 = model.TournamentEvent.get(2023, model.GrandSlam.get(name='Wimbledon'))

    assert not wm2023.draws

    wm2023.load()

    assert len(wm2023.draws) == 1

    draw = wm2023.for_draw("MensSingles")

    if len(draw.rounds) != 2:
        breakpoint()

    assert len(draw.rounds) == 2

    first_rd = draw.for_round(1)


    assert len(first_rd.matches) == 2

    match_1_1 = first_rd.for_match(1)

    assert not match_1_1.match_winner
    assert match_1_1.player1.player().klass_name == "Alcaraz"
    assert match_1_1.player2.player().klass_name == "Tsitsipas"



# Helpers


def create_draw(event):
    (event.make_draw(name="MensSingles", best_of=5, draw_size=2)
     .add_entries(entries())
     .init_draw()
     .first_round_draw(first_round_draw()))

def first_round_draw():
    return [
        (1, atp_players.Alcaraz, atp_players.Tsitsipas),
        (2, atp_players.Rublev, atp_players.Djokovic)
    ]


def entries():
    return [
        (atp_players.Alcaraz, 1),
        (atp_players.Tsitsipas, 3),
        (atp_players.Rublev, 4),
        (atp_players.Djokovic, 2)]


def create_tournie():
    wm = model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
    create_events()
    wm2023 = model.TournamentEvent.get(tournament=wm, year=2023)
    create_draw(wm2023)



def create_events():
    model.TournamentEvent.create(year=2023, tournament_name="Wimbledon")


def create_tournies():
    model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
    model.GrandSlam.create(name="Roland Garros", subject_name="RolandGarros", perma_id="rg")
    model.GrandSlam.create(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")
    model.GrandSlam.create(name="US Open", subject_name="UsOpen", perma_id="uo")


def create_events():
    model.TournamentEvent.create(year=2023, tournament_name="Wimbledon")
    model.TournamentEvent.create(year=2023, tournament_name="Roland Garros")
    model.TournamentEvent.create(year=2023, tournament_name="Australian Open")
    model.TournamentEvent.create(year=2023, tournament_name="US Open")