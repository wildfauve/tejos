from tejos import model
from tejos import repo
from tejos.players import atp_players


def test_create_draw(configure_repo):
    wm2023 = create_event()

    draw = wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4).init_draw()

    assert draw.name == "MensSingles"
    assert draw.best_of == 5
    assert len(draw.rounds) == 3

    same_draw = wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)

    assert id(same_draw) == id(draw)


def test_get_draw(configure_repo):
    wm2023 = create_event()

    wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4).init_draw()

    draw = model.Draw.get(event=wm2023, name="MensSingles")

    assert draw.name == "MensSingles"
    assert len(draw.rounds) == 3

    same_draw = model.Draw.get(event=wm2023, name="MensSingles")

    assert same_draw == draw
    assert len(wm2023.draws) == 1


def test_add_entries_to_draw(configure_repo):
    wm2023 = create_event()

    draw = wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4).init_draw()

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


def test_add_first_round(configure_repo):
    wm2023 = create_event()

    draw = wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4).add_entries(entries()).init_draw()

    draw.first_round_draw(first_round_draw())

    matches_r1 = [(mt.match_block()) for mt in draw.rounds[0].matches]
    matches_r2 = [(mt.match_block()) for mt in draw.rounds[1].matches]

    expected = ['(  1) Carlos Alcaraz \n(  7) Stefanos Tsitsipas ',
                '(  5) Andrey Rublev \n(  3) Novak Djokovic ',
                '(  4) Holger Rune \n(  6) Matteo Berrettini ',
                '(  8) Christopher Eubanks \n(  2) Jannik Sinner ']

    assert matches_r1 == expected
    assert matches_r2 == ['?\n?', '?\n?']


def test_get_first_round(configure_repo):
    wm2023 = create_event()

    (wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)
     .add_entries(entries())
     .init_draw()
     .first_round_draw(first_round_draw()))

    draw = model.Draw.get(event=wm2023, name="MensSingles")

    matches_r1 = [(mt.match_block()) for mt in draw.rounds[0].matches]
    matches_r2 = [(mt.match_block()) for mt in draw.rounds[1].matches]
    matches_r3 = [(mt.match_block()) for mt in draw.rounds[2].matches]

    expected = ['(  1) Carlos Alcaraz \n(  7) Stefanos Tsitsipas ',
                '(  5) Andrey Rublev \n(  3) Novak Djokovic ',
                '(  4) Holger Rune \n(  6) Matteo Berrettini ',
                '(  8) Christopher Eubanks \n(  2) Jannik Sinner ']

    assert matches_r1 == expected
    assert matches_r2 == ['?\n?', '?\n?']
    assert matches_r3 == ['?\n?']


def test_add_match_result(configure_repo):
    from tejos.players import atp_players

    wm2023 = create_event()

    wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4).add_entries(entries()).init_draw().first_round_draw(
        first_round_draw())

    draw = model.Draw.get(event=wm2023, name="MensSingles")

    match1_1 = draw.for_round(1).for_match(1)
    match1_1.score(atp_players.Alcaraz, (6, 6, 6)).score(atp_players.Tsitsipas, (4, 4, 4))

    assert match1_1.match_winner.player() == atp_players.Alcaraz
    assert match1_1.match_block() == '(  1) Carlos Alcaraz 6 6 6   <\n(  7) Stefanos Tsitsipas 4 4 4   '

    match_2_1 = draw.for_round(2).for_match(1)

    assert match_2_1.match_block() == '(  1) Carlos Alcaraz \n?'

    match1_2 = draw.for_round(1).for_match(2)
    match1_2.score(atp_players.Rublev, (6, 6, 6)).score(atp_players.Djokovic, (4, 4, 4))

    assert match1_2.match_winner.player() == atp_players.Rublev
    assert match1_2.match_block() == '(  5) Andrey Rublev 6 6 6   <\n(  3) Novak Djokovic 4 4 4   '

    assert match_2_1.match_block() == '(  1) Carlos Alcaraz \n(  5) Andrey Rublev '


def test_get_with_results(configure_repo):
    wm2023 = create_event()

    add_results(wm2023.make_draw(name="MensSingles", best_of=5, draw_size=4)
                .add_entries(entries())
                .init_draw()
                .first_round_draw(first_round_draw()))

    draw = model.Draw.get(event=wm2023, name="MensSingles")

    match_1_1 = draw.for_round(1).for_match(1)
    match_1_2 = draw.for_round(1).for_match(2)
    match_2_1 = draw.for_round(2).for_match(1)

    assert match_1_1.match_winner.player() == atp_players.Alcaraz
    assert match_1_1.match_block() == '(  1) Carlos Alcaraz 6 6 6   <\n(  7) Stefanos Tsitsipas 4 4 4   '
    assert match_1_2.match_winner.player() == atp_players.Rublev
    assert match_1_2.match_block() == '(  5) Andrey Rublev 6 6 6   <\n(  3) Novak Djokovic 4 4 4   '
    assert not match_2_1.match_winner
    assert match_2_1.match_block() == '(  1) Carlos Alcaraz \n(  5) Andrey Rublev '



# Helpers


def add_results(draw):
    draw.for_round(1).for_match(1).score(atp_players.Alcaraz, (6, 6, 6)).score(atp_players.Tsitsipas, (4, 4, 4))
    draw.for_round(1).for_match(2).score(atp_players.Rublev, (6, 6, 6)).score(atp_players.Djokovic, (4, 4, 4))


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


def first_round_draw():
    from tejos.players import atp_players
    return [
        (1, atp_players.Alcaraz, atp_players.Tsitsipas),
        (2, atp_players.Rublev, atp_players.Djokovic),
        (3, atp_players.Rune, atp_players.Berrettini),
        (4, atp_players.Eubanks, atp_players.Sinner),
    ]


def create_event():
    wm = model.GrandSlam.create(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
    return wm.make_event(2023)
