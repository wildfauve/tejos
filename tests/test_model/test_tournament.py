from tejos import model
from tejos import repo


def test_create_tournament(configure_repo):
    tournie = model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")

    assert tournie.name == "Wimbledon"

    same_tournie = model.GrandSlam.get(name="Wimbledon")

    assert same_tournie == tournie


def test_get_all_tournies(configure_repo):
    create_tournies()

    results = model.GrandSlam.get_all()

    assert len(results) == 4
    expected = {'Wimbledon', 'Roland Garros', 'Australian Open', 'US Open'}
    assert {t.name for t in results} == expected

def test_get_all_with_events(configure_repo):
    create_tournies()
    create_events()
    finder = model.tournament.tournaments()

    wm = finder.slam("Wimbledon")
    assert wm.name == "Wimbledon"

    wm, wm2023 = finder.slam_year("Wimbledon", 2023)
    assert wm.name == "Wimbledon"
    assert wm2023.name == "Wimbledon2023"

    assert not wm2023.draws

    wm, wm2023 = finder.slam_year("Wimbledon", 2023, load=True)

    assert wm2023.draws




# Helpers

def create_tournies():
    model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
    model.GrandSlam.create(name="Roland Garros", subject_name="RolandGarros", perma_id="rg")
    model.GrandSlam.create(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")
    model.GrandSlam.create(name="US Open", subject_name="UsOpen", perma_id="uo")


def create_events():
    wm2023 = model.TournamentEvent.create(year=2023, tournament_name="Wimbledon")
    create_draw(wm2023)
    model.TournamentEvent.create(year=2023, tournament_name="Roland Garros")
    model.TournamentEvent.create(year=2023, tournament_name="Australian Open")
    model.TournamentEvent.create(year=2023, tournament_name="US Open")


def create_draw(event):
    (event.make_draw(name="MensSingles", best_of=5, draw_size=2).init_draw())
