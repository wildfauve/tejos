from tejos.model import player
from tejos import repo


def test_create_new_player(configure_repo):
    pl = player.Player.new("Carlos Alcaraz", tour_symbol="ATP", klass_name="Alcaraz", alt_names=["Carlos.Alcaraz",
                                                                                                 "C.Alcaraz"])

    assert pl.name == "Carlos Alcaraz"

    assert pl == pl.__class__.cache_hit(name=pl.name).value
    assert pl == pl.__class__.cache_hit(klass_name=pl.klass_name).value

    same_pl = player.Player.load(name="Carlos Alcaraz")

    assert same_pl == pl


def test_search_on(configure_repo):
    add_players()

    pl1_name = player.Player.load(name="Carlos Alcaraz")
    pl1_klass_name = player.Player.load(klass_name="Alcaraz")
    pl1_with_alt_name = player.Player.load(name="C.Alcaraz")
    assert pl1_name == pl1_klass_name
    assert pl1_name == pl1_with_alt_name


def test_load_all_players(configure_repo):
    from tejos.players import atp_players, wta_players
    add_players()

    player.Player.loadall()
    assert atp_players.Alcaraz.name == "Carlos Alcaraz"
    assert wta_players.Sabalenka.name == "Aryna Sabalenka"



def test_player_set_on_class_module(configure_repo):
    from tejos.players import atp_players, wta_players
    add_players()

    assert atp_players.Alcaraz.name == "Carlos Alcaraz"
    assert wta_players.Sabalenka.name == "Aryna Sabalenka"


def test_find_player_using_dot_and_sp(configure_repo):
    add_players()

    player.Player.loadall()
    pl = player.Player.load("C.Alcaraz")
    pl_same = player.Player.load("Carlos Alcaraz")

    assert pl.name == 'Carlos Alcaraz'
    assert pl == pl_same


def test_find_player_not_defined(configure_repo):
    add_players()
    player.Player.loadall()
    assert not player.Player.load("Not A Real Name")


def test_player_with_same_surname(configure_repo):
    pl1 = player.Player.load("Francisco Cerundolo")

    assert pl1.name == "Francisco Cerundolo"

    alt_name_player = player.Player.load("F.Cerundolo")

    assert alt_name_player.name == "Francisco Cerundolo"


def add_players():
    player.Player.new("Carlos Alcaraz",
                      tour_symbol="ATP",
                      klass_name="Alcaraz",
                      alt_names=["Carlos.Alcaraz", "C.Alcaraz"])
    player.Player.new("Aryna Sabalenka", tour_symbol="WTA", klass_name="Sabalenka")

    player.Player.new("Francisco Cerundolo",
                      tour_symbol="ATP",
                      klass_name="Cerundolo_Francisco",
                      alt_names=['F.Cerundolo'])

    player.Player.new("Juan Cerundolo",
                      tour_symbol="ATP",
                      klass_name="Cerundolo_Juan",
                      alt_names=['J.Cerundolo'])
