import pytest
from pathlib import Path

from tejos import repo, model

TOURNAMENT_PATH = (Path(__file__).parent.parent / "fixtures" / "tournament_test.ttl")
PLAYERS_PATH = (Path(__file__).parent.parent / "fixtures" / "players_test.ttl")
FANTASY_PATH = (Path(__file__).parent.parent / "fixtures" / "fantasy_test.ttl")
EMPTY_PLAYERS_PATH = (Path(__file__).parent.parent / "fixtures" / "empty_players_test.ttl")


@pytest.fixture
def configure_repo():
    repo.RepoContext().configure(triples_location=TOURNAMENT_PATH,
                                 players_triples_location=PLAYERS_PATH,
                                 fantasy_triples_location=FANTASY_PATH)
    repo.init()
    yield repo
    repo.drop()

@pytest.fixture
def configure_repo_empty_players():
    repo.RepoContext().configure(triples_location=TOURNAMENT_PATH,
                                 players_triples_location=EMPTY_PLAYERS_PATH,
                                 fantasy_triples_location=FANTASY_PATH)
    repo.init()
    yield repo
    repo.drop()


@pytest.fixture
def empty_graph():
    return repo.triples.graph()

