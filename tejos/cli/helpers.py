from tejos import model

Tournaments = model.tournament.tournaments()
def tournament_names():
    return Tournaments.slam_symbols()


def to_tournament(name):
    return Tournaments.slam(name)
