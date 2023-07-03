from tejos.players import players, atp_players

def test_find_player_using_dot_and_sp():
    player = players.search_player_by_name("C.Alcaraz", atp_players)
    player_same = players.search_player_by_name("Carlos Alcaraz", atp_players)

    assert player.name == 'Carlos Alcaraz'
    assert player == player_same


def test_find_player_not_defined():
    assert not players.search_player_by_name("Not A Real Name", atp_players)


def test_player_with_same_surname():
    player = players.search_player_by_name("Francisco Cerundolo", atp_players)

    assert player.name == "Francisco Cerundolo"

    alt_name_player = players.search_player_by_name("F.Cerundolo", atp_players)

    assert alt_name_player.name == "Francisco Cerundolo"

