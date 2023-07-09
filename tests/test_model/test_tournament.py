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

# Helpers

def create_tournies():
    model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
    model.GrandSlam.create(name="Roland Garros", subject_name="RolandGarros", perma_id="rg")
    model.GrandSlam.create(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")
    model.GrandSlam.create(name="US Open", subject_name="UsOpen", perma_id="uo")
