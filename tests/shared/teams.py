import pytest

from tejos.model import fantasy

@pytest.fixture
def fantasy_team():
    return fantasy.Team("FantasyTeam1", "Member1")

@pytest.fixture
def fantasy_team_2():
    return fantasy.Team("FantasyTeam2", "Member2")

@pytest.fixture
def fantasy_team_3():
    return fantasy.Team("FantasyTeam3", "Member3")

@pytest.fixture
def fantasy_team_4():
    return fantasy.Team("FantasyTeam4", "Member4")