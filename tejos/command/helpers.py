from typing import Tuple

from tejos import repo, model

def save(val: Tuple = None) -> Tuple:
    repo.save()
    return val


def graph():
    return repo.graph()
