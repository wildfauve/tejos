from tejos import model
from tejos import repo


def test_create_event(configure_repo):
    create_tournies()

    event = model.TournamentEvent.create(year=2023, tournament_name="Wimbledon")

    assert event.scheduled_in_year == 2023
    assert event.is_event_of.name == "Wimbledon"

    same_event = model.TournamentEvent.get(tournament=event.is_event_of, year=2023)

    assert same_event == event


def test_get_all_events(configure_repo):
    create_tournies()
    create_events()

    results = model.TournamentEvent.get_all()

    assert len(results) == 4

    expected = {'RolandGarros2023', 'AustralianOpen2023', 'UsOpen2023', 'Wimbledon2023'}
    assert {ev.name for ev in results} == expected

    expected_tournies = {'Wimbledon', 'Roland Garros', 'Australian Open', 'US Open'}
    assert {ev.is_event_of.name for ev in results} == expected_tournies




# Helpers

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