from tejos import model
from tejos import repo


def test_create_draw(configure_repo):
    wm2023 = create_event()

    draw = wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)

    assert draw.name == "MensSingles"
    assert draw.best_of == 5
    assert len(draw.rounds) == 3

    same_draw = wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)

    assert id(same_draw) == id(draw)


def test_get_draw(configure_repo):
    wm2023 = create_event()

    wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)

    draw = model.Draw.get(event=wm2023, name="MensSingles")

    assert draw.name == "MensSingles"
    assert len(draw.rounds) == 3

    same_draw = model.Draw.get(event=wm2023, name="MensSingles")

    assert same_draw == draw
    assert len(wm2023.draws) == 1


def test_add_entries_to_draw(configure_repo):
    wm2023 = create_event()

    draw = wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)

    draw.add_entries(entries())
    assert len(draw.entries) == 8

    draw_entries = {(en.player().klass_name, en.has_seed) for en in draw.entries}

    expected = {('Alcaraz', 1),
                ('Tsitsipas', 7),
                ('Rublev', 5),
                ('Djokovic', 3),
                ('Rune', 4),
                ('Berrettini', 6),
                ('Eubanks', 8),
                ('Sinner', 2)}
    assert draw_entries == expected



def test_get_entries_from_draw(configure_repo):
    wm2023 = create_event()

    wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4).add_entries(entries())

    draw = model.Draw.get(event=wm2023, name="MensSingles")

    draw_entries = {(en.player().klass_name, en.has_seed) for en in draw.entries}

    expected = {('Alcaraz', 1),
                ('Tsitsipas', 7),
                ('Rublev', 5),
                ('Djokovic', 3),
                ('Rune', 4),
                ('Berrettini', 6),
                ('Eubanks', 8),
                ('Sinner', 2)}
    assert draw_entries == expected

# Helpers


def entries():
    from tejos.players import atp_players
    return [
        (atp_players.Alcaraz, 1),
        (atp_players.Tsitsipas, 7),
        (atp_players.Rublev, 5),
        (atp_players.Djokovic, 3),
        (atp_players.Rune, 4),
        (atp_players.Berrettini, 6),
        (atp_players.Eubanks, 8),
        (atp_players.Sinner, 2),
    ]


def create_event():
    wm = model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
    return wm.make_event(2023)
