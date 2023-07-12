from typing import Tuple

from tejos import repo, model

def save(val: Tuple = None) -> Tuple:
    repo.save()
    return val


def graph():
    return repo.graph()

def tournie(name):
    return model.GrandSlam.get(name=name)


def event(tournie, year):
    return model.TournamentEvent.get(tournament=tournie, year=year)
