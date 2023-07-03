from tejos.players import wta_players, atp_players


def mens_singles_results_r7(draw):
    return [
        (draw.for_round(7).for_match(1)
         .score(atp_players.Djokovic, (7, 6, 7))
         .score(atp_players.Ruud, (6, 3, 5))),

    ]


def womens_singles_results_r7(draw):
    return [
        (draw.for_round(7).for_match(1)
         .score(wta_players.Swiatek, (6, 5, 6))
         .score(wta_players.Muchova, (2, 7, 4))),

    ]


def mens_singles_results_r6(draw):
    return [
        (draw.for_round(6).for_match(1)
         .score(atp_players.Alcaraz, (3, 7, 1, 1))
         .score(atp_players.Djokovic, (6, 5, 6, 6))),

        (draw.for_round(6).for_match(2)
         .score(atp_players.Ruud, (6, 6, 6))
         .score(atp_players.Zverev, (3, 4, 0))),
    ]


def womens_singles_results_r6(draw):
    return [
        (draw.for_round(6).for_match(1)
         .score(wta_players.Swiatek, (6, 7))
         .score(wta_players.Haddad_Maia, (2, 6))),

        (draw.for_round(6).for_match(2)
         .score(wta_players.Muchova, (7, 6, 7))
         .score(wta_players.Sabalenka, (6, 7, 5))),

    ]


def mens_singles_results_r5(draw):
    return [
        (draw.for_round(5).for_match(1)
         .score(atp_players.Alcaraz, (6, 6, 7))
         .score(atp_players.Tsitsipas, (2, 1, 6))),

        (draw.for_round(5).for_match(2)
         .score(atp_players.Djokovic, (4, 7, 6, 6))
         .score(atp_players.Khachanov, (6, 6, 2, 4))),

        (draw.for_round(5).for_match(3)
         .score(atp_players.Rune, (1, 2, 6, 3))
         .score(atp_players.Ruud, (6, 6, 3, 6))),

        (draw.for_round(5).for_match(4)
         .score(atp_players.Zverev, (6, 3, 6, 6))
         .score(atp_players.Etcheverry, (4, 6, 3, 4))),

    ]


def womens_singles_results_r5(draw):
    return [
        (draw.for_round(5).for_match(1)
         .score(wta_players.Swiatek, (6, 6))
         .score(wta_players.Gauff, (4, 2))),

        (draw.for_round(5).for_match(2)
         .score(wta_players.Haddad_Maia, (3, 7, 6))
         .score(wta_players.Jabeur, (6, 6, 1))),

        (draw.for_round(5).for_match(3)
         .score(wta_players.Muchova, (7, 6))
         .score(wta_players.Pavlyuchenkova, (5, 2))),

        (draw.for_round(5).for_match(4)
         .score(wta_players.Svitolina, (4, 4))
         .score(wta_players.Sabalenka, (6, 6))),

    ]


def mens_singles_results_r4(draw):
    return [
        (draw.for_round(4).for_match(1)
         .score(atp_players.Alcaraz, (6, 6, 6))
         .score(atp_players.Musetti, (3, 2, 2))),

        (draw.for_round(4).for_match(2)
         .score(atp_players.Ofner, (5, 3, 0))
         .score(atp_players.Tsitsipas, (7, 6, 6))),

        (draw.for_round(4).for_match(3)
         .score(atp_players.Djokovic, (6, 6, 6))
         .score(atp_players.Varillas, (3, 2, 2))),

        (draw.for_round(4).for_match(4)
         .score(atp_players.Khachanov, (1, 6, 7, 6))
         .score(atp_players.Sonego, (6, 4, 6, 1))),

        (draw.for_round(4).for_match(5)
         .score(atp_players.Rune, (7, 3, 6, 1, 7))
         .score(atp_players.Cerundolo_Francisco, (6, 6, 4, 6, 6))),

        (draw.for_round(4).for_match(6)
         .score(atp_players.Jarry, (6, 5, 5))
         .score(atp_players.Ruud, (7, 7, 7))),

        (draw.for_round(4).for_match(7)
         .score(atp_players.Dimitrov, (1, 4, 3))
         .score(atp_players.Zverev, (6, 6, 6))),

        (draw.for_round(4).for_match(8)
         .score(atp_players.Etcheverry, (7, 6, 6))
         .score(atp_players.Nishioka, (6, 0, 1))),

    ]


def womens_singles_results_r4(draw):
    return [
        (draw.for_round(4).for_match(1)
         .score(wta_players.Swiatek, (5,))
         .score(wta_players.Tsurenko, (1,))
         .retirement(wta_players.Tsurenko)),

        (draw.for_round(4).for_match(2)
         .score(wta_players.Schmiedlova, (5, 2))
         .score(wta_players.Gauff, (7, 6))),

        (draw.for_round(4).for_match(3)
         .score(wta_players.Sorribes_Tormo, (7, 3, 5))
         .score(wta_players.Haddad_Maia, (6, 6, 7))),

        (draw.for_round(4).for_match(4)
         .score(wta_players.Pera, (3, 1))
         .score(wta_players.Jabeur, (6, 6))),

        (draw.for_round(4).for_match(5)
         .score(wta_players.Muchova, (6, 6))
         .score(wta_players.Avanesyan, (4, 3))),

        (draw.for_round(4).for_match(6)
         .score(wta_players.Pavlyuchenkova, (3, 7, 6))
         .score(wta_players.Mertens, (6, 6, 3))),

        (draw.for_round(4).for_match(7)
         .score(wta_players.Svitolina, (6, 7))
         .score(wta_players.Kasatkina, (4, 6))),

        (draw.for_round(4).for_match(8)
         .score(wta_players.Stephens, (6, 4))
         .score(wta_players.Sabalenka, (7, 6))),
    ]


def mens_singles_results_r3(draw):
    return [
        (draw.for_round(3).for_match(1)
         .score(atp_players.Alcaraz, (6, 6, 6))
         .score(atp_players.Shapovalov, (1, 4, 2))),

        (draw.for_round(3).for_match(2)
         .score(atp_players.Musetti, (6, 6, 6))
         .score(atp_players.Norrie, (1, 2, 4))),

        (draw.for_round(3).for_match(3)
         .score(atp_players.Fognini, (7, 3, 5, 6, 4))
         .score(atp_players.Ofner, (5, 6, 7, 1, 6))),

        (draw.for_round(3).for_match(4)
         .score(atp_players.Schwartzman, (2, 2, 3))
         .score(atp_players.Tsitsipas, (6, 6, 6))),

        (draw.for_round(3).for_match(5)
         .score(atp_players.Djokovic, (7, 7, 6))
         .score(atp_players.Davidovich_Fokina, (6, 6, 2))),

        (draw.for_round(3).for_match(6)
         .score(atp_players.Varillas, (3, 6, 7, 4, 6))
         .score(atp_players.Hurkacz, (6, 3, 6, 6, 2))),

        (draw.for_round(3).for_match(7)
         .score(atp_players.Khachanov, (6, 6, 3, 7))
         .score(atp_players.Kokkinakis, (4, 1, 6, 6))),

        (draw.for_round(3).for_match(8)
         .score(atp_players.Sonego, (5, 0, 6, 7, 6))
         .score(atp_players.Rublev, (7, 6, 3, 6, 3))),

        (draw.for_round(3).for_match(9)
         .score(atp_players.Rune, (6, 6, 6))
         .score(atp_players.Olivieri, (4, 1, 3))),

        (draw.for_round(3).for_match(10)
         .score(atp_players.Cerundolo_Francisco, (3, 6, 6, 7))
         .score(atp_players.Fritz, (6, 3, 4, 5))),

        (draw.for_round(3).for_match(11)
         .score(atp_players.Jarry, (6, 6, 6, 6))
         .score(atp_players.Giron, (2, 3, 7, 3))),

        (draw.for_round(3).for_match(12)
         .score(atp_players.Zhang_Zhizhen, (6, 4, 1, 4))
         .score(atp_players.Ruud, (4, 6, 6, 6))),

        (draw.for_round(3).for_match(13)
         .score(atp_players.Altmaier, (4, 3, 1))
         .score(atp_players.Dimitrov, (6, 6, 6))),

        (draw.for_round(3).for_match(14)
         .score(atp_players.Zverev, (3, 7, 6, 7))
         .score(atp_players.Tiafoe, (6, 6, 1, 6))),

        (draw.for_round(3).for_match(15)
         .score(atp_players.Coric, (3, 6, 2))
         .score(atp_players.Etcheverry, (6, 7, 6))),

        (draw.for_round(3).for_match(16)
         .score(atp_players.Nishioka, (3, 7, 2, 6, 6))
         .score(atp_players.Seyboth_Wild, (6, 6, 6, 4, 0))),

    ]


def womens_singles_results_r3(draw):
    return [
        (draw.for_round(3).for_match(1)
         .score(wta_players.Swiatek, (6, 6))
         .score(wta_players.Wang_Xinyu, (0, 0))),

        (draw.for_round(3).for_match(2)
         .score(wta_players.Andreescu, (1, 1))
         .score(wta_players.Tsurenko, (6, 6))),

        (draw.for_round(3).for_match(3)
         .score(wta_players.Schmiedlova, (6, 6))
         .score(wta_players.Day, (1, 3))),

        (draw.for_round(3).for_match(4)
         .score(wta_players.Andreeva_Mirra, (7, 1, 1))
         .score(wta_players.Gauff, (6, 6, 6))),

        (draw.for_round(3).for_match(5)
         .score(wta_players.Rybakina, ())
         .score(wta_players.Sorribes_Tormo, ())
         .withdrawal(wta_players.Rybakina)),

        (draw.for_round(3).for_match(6)
         .score(wta_players.Alexandrova, (7, 4, 5))
         .score(wta_players.Haddad_Maia, (5, 6, 7))),

        (draw.for_round(3).for_match(7)
         .score(wta_players.Cocciaretto, (4, 6))
         .score(wta_players.Pera, (6, 7))),

        (draw.for_round(3).for_match(8)
         .score(wta_players.Danilovic, (6, 4, 2))
         .score(wta_players.Jabeur, (4, 6, 6))),

        (draw.for_round(3).for_match(9)
         .score(wta_players.Muchova, (6, 6))
         .score(wta_players.Begu, (3, 2))),

        (draw.for_round(3).for_match(10)
         .score(wta_players.Tauson, (6, 1, 5))
         .score(wta_players.Avanesyan, (3, 6, 7))),

        (draw.for_round(3).for_match(11)
         .score(wta_players.Pavlyuchenkova, (4, 6, 6))
         .score(wta_players.Potapova, (6, 3, 0))),

        (draw.for_round(3).for_match(12)
         .score(wta_players.Mertens, (6, 6))
         .score(wta_players.Pegula, (1, 3))),

        (draw.for_round(3).for_match(13)
         .score(wta_players.Blinkova, (6, 2, 5))
         .score(wta_players.Svitolina, (2, 6, 7))),

        (draw.for_round(3).for_match(14)
         .score(wta_players.Stearns, (0, 1))
         .score(wta_players.Kasatkina, (6, 6))),

        (draw.for_round(3).for_match(15)
         .score(wta_players.Stephens, (6, 3, 6))
         .score(wta_players.Putintseva, (3, 6, 2))),

        (draw.for_round(3).for_match(16)
         .score(wta_players.Rakhimova, (2, 2))
         .score(wta_players.Sabalenka, (6, 6))),
    ]


def mens_singles_results_r2(draw):
    return [
        (draw.for_round(2).for_match(1)
         .score(atp_players.Alcaraz, (6, 3, 6, 6))
         .score(atp_players.Daniel, (1, 6, 1, 2))),

        (draw.for_round(2).for_match(2)
         .score(atp_players.Arnaldi, (2, 6, 3, 3))
         .score(atp_players.Shapovalov, (6, 3, 6, 6))),

        (draw.for_round(2).for_match(3)
         .score(atp_players.Musetti, (6, 6, 6))
         .score(atp_players.Shevchenko, (1, 1, 2))),

        (draw.for_round(2).for_match(4)
         .score(atp_players.Pouille, (1, 3, 3))
         .score(atp_players.Norrie, (6, 6, 6))),

        (draw.for_round(2).for_match(5)
         .score(atp_players.Fognini, (6, 7, 6))
         .score(atp_players.Kubler, (4, 6, 2))),

        (draw.for_round(2).for_match(6)
         .score(atp_players.Ofner, (6, 7, 6))
         .score(atp_players.Korda, (3, 6, 4))),

        (draw.for_round(2).for_match(7)
         .score(atp_players.Schwartzman, (7, 6, 6))
         .score(atp_players.Borges, (6, 4, 3))),

        (draw.for_round(2).for_match(8)
         .score(atp_players.Carballes_Baena, (3, 6, 2))
         .score(atp_players.Tsitsipas, (6, 7, 6))),

        (draw.for_round(2).for_match(9)
         .score(atp_players.Djokovic, (7, 6, 6))
         .score(atp_players.Fucsovics, (6, 0, 3))),

        (draw.for_round(2).for_match(10)
         .score(atp_players.Van_Assche, (4, 3, 6))
         .score(atp_players.Davidovich_Fokina, (6, 6, 7))),

        (draw.for_round(2).for_match(11)
         .score(atp_players.Bautista_Agut, (6, 6, 3, 1, 1))
         .score(atp_players.Varillas, (1, 4, 6, 6, 6))),

        (draw.for_round(2).for_match(12)
         .score(atp_players.Griekspoor, (3, 7, 7, 6, 4))
         .score(atp_players.Hurkacz, (6, 5, 6, 7, 6))),

        (draw.for_round(2).for_match(13)
         .score(atp_players.Khachanov, (6, 6, 6))
         .score(atp_players.Albot, (3, 4, 2))),

        (draw.for_round(2).for_match(14)
         .score(atp_players.Wawrinka, (6, 5, 3, 7, 3))
         .score(atp_players.Kokkinakis, (3, 7, 6, 6, 6))),

        (draw.for_round(2).for_match(15)
         .score(atp_players.Sonego, (6, 6, 7))
         .score(atp_players.Humbert, (4, 3, 6))),

        (draw.for_round(2).for_match(16)
         .score(atp_players.Moutet, (4, 2, 6, 3))
         .score(atp_players.Rublev, (6, 6, 3, 6))),

        (draw.for_round(2).for_match(17)
         .score(atp_players.Rune, ())
         .score(atp_players.Monfils, ())
         .withdrawal(atp_players.Monfils)),

        (draw.for_round(2).for_match(18)
         .score(atp_players.Olivieri, (7, 3, 6, 7))
         .score(atp_players.Vavassori, (6, 6, 4, 6))),

        (draw.for_round(2).for_match(19)
         .score(atp_players.Cerundolo_Francisco, (6, 6, 6))
         .score(atp_players.Hanfmann, (3, 3, 4))),

        (draw.for_round(2).for_match(20)
         .score(atp_players.Rinderknech, (6, 4, 3, 4))
         .score(atp_players.Fritz, (2, 6, 6, 6))),

        (draw.for_round(2).for_match(21)
         .score(atp_players.Paul, (6, 1, 4, 5))
         .score(atp_players.Jarry, (3, 6, 6, 7))),

        (draw.for_round(2).for_match(22)
         .score(atp_players.Giron, (6, 6, 6))
         .score(atp_players.Lehecka, (2, 3, 2))),

        (draw.for_round(2).for_match(23)
         .score(atp_players.Tirante, (6, 3, 4))
         .score(atp_players.Zhang_Zhizhen, (7, 6, 6))),

        (draw.for_round(2).for_match(24)
         .score(atp_players.Zeppieri, (3, 2, 6, 5))
         .score(atp_players.Ruud, (6, 6, 4, 7))),

        (draw.for_round(2).for_match(25)
         .score(atp_players.Sinner, (7, 6, 6, 6, 5))
         .score(atp_players.Altmaier, (6, 7, 1, 7, 7))),

        (draw.for_round(2).for_match(26)
         .score(atp_players.Ruusuvuori, (6, 3, 4))
         .score(atp_players.Dimitrov, (7, 6, 6))),

        (draw.for_round(2).for_match(27)
         .score(atp_players.Zverev, (6, 6, 6))
         .score(atp_players.Molcan, (4, 2, 1))),

        (draw.for_round(2).for_match(28)
         .score(atp_players.Karatsev, (6, 3, 5, 2))
         .score(atp_players.Tiafoe, (3, 6, 7, 6))),

        (draw.for_round(2).for_match(29)
         .score(atp_players.Coric, (6, 4, 4, 6, 6))
         .score(atp_players.Cachin, (3, 6, 6, 3, 4))),

        (draw.for_round(2).for_match(30)
         .score(atp_players.Etcheverry, (6, 7, 6))
         .score(atp_players.De_Minaur, (3, 6, 3))),

        (draw.for_round(2).for_match(31)
         .score(atp_players.Nishioka, (4, 6, 7, 6))
         .score(atp_players.Purcell, (6, 2, 5, 4))),

        (draw.for_round(2).for_match(32)
         .score(atp_players.Pella, (3, 6, 4, 3))
         .score(atp_players.Seyboth_Wild, (6, 3, 6, 6))),

    ]


def womens_singles_results_r2(draw):
    return [
        (draw.for_round(2).for_match(1)
         .score(wta_players.Swiatek, (6, 6))
         .score(wta_players.Liu, (4, 0))),

        (draw.for_round(2).for_match(2)
         .score(wta_players.Peterson, (6, 2))
         .score(wta_players.Wang_Xinyu, (7, 6))),

        (draw.for_round(2).for_match(3)
         .score(wta_players.Andreescu, (6, 6))
         .score(wta_players.Navarro, (1, 4))),

        (draw.for_round(2).for_match(4)
         .score(wta_players.Davis, (3, 0))
         .score(wta_players.Tsurenko, (6, 1))
         .retirement(wta_players.Davis)),

        (draw.for_round(2).for_match(5)
         .score(wta_players.Schmiedlova, (6, 6))
         .score(wta_players.Bolsova, (3, 4))),

        (draw.for_round(2).for_match(6)
         .score(wta_players.Day, (6, 4, 6))
         .score(wta_players.Keys, (2, 6, 4))),

        (draw.for_round(2).for_match(7)
         .score(wta_players.Parry, (1, 2))
         .score(wta_players.Andreeva_Mirra, (6, 6))),

        (draw.for_round(2).for_match(8)
         .score(wta_players.Grabher, (2, 3))
         .score(wta_players.Gauff, (6, 6))),

        (draw.for_round(2).for_match(9)
         .score(wta_players.Rybakina, (6, 6))
         .score(wta_players.Noskova, (3, 3))),

        (draw.for_round(2).for_match(10)
         .score(wta_players.Sorribes_Tormo, (6, 6))
         .score(wta_players.Martic, (4, 1))),

        (draw.for_round(2).for_match(11)
         .score(wta_players.Alexandrova, (6, 6))
         .score(wta_players.Friedsam, (2, 0))),

        (draw.for_round(2).for_match(12)
         .score(wta_players.Shnaider, (2, 7, 4))
         .score(wta_players.Haddad_Maia, (6, 5, 6))),

        (draw.for_round(2).for_match(13)
         .score(wta_players.Cocciaretto, (6, 6))
         .score(wta_players.Waltert, (2, 3))),

        (draw.for_round(2).for_match(14)
         .score(wta_players.Pera, (3, 6, 6))
         .score(wta_players.Vekic, (6, 4, 3))),

        (draw.for_round(2).for_match(15)
         .score(wta_players.Paolini, (2, 5))
         .score(wta_players.Danilovic, (6, 7))),

        (draw.for_round(2).for_match(16)
         .score(wta_players.Dodin, (2, 3))
         .score(wta_players.Jabeur, (6, 6))),

        (draw.for_round(2).for_match(17)
         .score(wta_players.Muchova, (6, 0, 6))
         .score(wta_players.Podoroska, (3, 6, 3))),

        (draw.for_round(2).for_match(18)
         .score(wta_players.Errani, (3, 0))
         .score(wta_players.Begu, (6, 6))),

        (draw.for_round(2).for_match(19)
         .score(wta_players.Fernandez, (3, 7, 4))
         .score(wta_players.Tauson, (6, 5, 6))),

        (draw.for_round(2).for_match(20)
         .score(wta_players.Jeanjean, (0, 5))
         .score(wta_players.Avanesyan, (6, 7))),

        (draw.for_round(2).for_match(21)
         .score(wta_players.Samsonova, (6, 5, 5))
         .score(wta_players.Pavlyuchenkova, (4, 7, 7))),

        (draw.for_round(2).for_match(22)
         .score(wta_players.Sherif, (6, 4, 1))
         .score(wta_players.Potapova, (3, 6, 6))),

        (draw.for_round(2).for_match(23)
         .score(wta_players.Mertens, (6, 7))
         .score(wta_players.Osorio, (3, 6))),

        (draw.for_round(2).for_match(24)
         .score(wta_players.Giorgi, (2, 0))
         .score(wta_players.Pegula, (6, 0))
         .retirement(wta_players.Giorgi)),

        (draw.for_round(2).for_match(25)
         .score(wta_players.Garcia, (6, 3, 5))
         .score(wta_players.Blinkova, (4, 6, 7))),

        (draw.for_round(2).for_match(26)
         .score(wta_players.Hunter, (6, 3, 1))
         .score(wta_players.Svitolina, (2, 6, 6))),

        (draw.for_round(2).for_match(27)
         .score(wta_players.Ostapenko, (3, 6, 2))
         .score(wta_players.Stearns, (6, 1, 6))),

        (draw.for_round(2).for_match(28)
         .score(wta_players.Vondrousova, (3, 4))
         .score(wta_players.Kasatkina, (6, 6))),

        (draw.for_round(2).for_match(29)
         .score(wta_players.Stephens, (6, 6))
         .score(wta_players.Gracheva, (2, 1))),

        (draw.for_round(2).for_match(30)
         .score(wta_players.Putintseva, (6, 4, 6))
         .score(wta_players.Zheng, (3, 6, 2))),

        (draw.for_round(2).for_match(31)
         .score(wta_players.Frech, (3, 4))
         .score(wta_players.Rakhimova, (6, 6))),

        (draw.for_round(2).for_match(32)
         .score(wta_players.Shymanovich, (5, 2))
         .score(wta_players.Sabalenka, (7, 6))),

    ]


def mens_singles_results_r1(draw):
    return [
        (draw.for_round(1).for_match(1)
         .score(atp_players.Alcaraz, (6, 6, 7))
         .score(atp_players.Cobolli, (0, 2, 5))),

        (draw.for_round(1).for_match(2)
         .score(atp_players.OConnell, (0, 2, 4))
         .score(atp_players.Daniel, (6, 6, 6))),

        (draw.for_round(1).for_match(3)
         .score(atp_players.Arnaldi, (2, 6, 6, 6))
         .score(atp_players.Galan, (6, 3, 0, 2))),

        (draw.for_round(1).for_match(4)
         .score(atp_players.Nakashima, (4, 5, 6, 6, 3))
         .score(atp_players.Shapovalov, (6, 7, 4, 3, 6))),

        (draw.for_round(1).for_match(5)
         .score(atp_players.Musetti, (7, 6, 6))
         .score(atp_players.Ymer_Mikael, (5, 2, 4))),

        (draw.for_round(1).for_match(6)
         .score(atp_players.Shevchenko, (7, 4, 6, 7))
         .score(atp_players.Otte, (5, 6, 1, 6))),

        (draw.for_round(1).for_match(7)
         .score(atp_players.Pouille, (6, 6, 6))
         .score(atp_players.Rodionov, (2, 4, 3))),

        (draw.for_round(1).for_match(8)
         .score(atp_players.Paire, (5, 6, 6, 1, 4))
         .score(atp_players.Norrie, (7, 4, 3, 6, 6))),

        (draw.for_round(1).for_match(9)
         .score(atp_players.Auger_Aliassime, (4, 4, 3))
         .score(atp_players.Fognini, (6, 6, 6))),

        (draw.for_round(1).for_match(10)
         .score(atp_players.Kubler, (1, 6, 6, 3, 6))
         .score(atp_players.Diaz_Acosta, (6, 3, 4, 6, 1))),

        (draw.for_round(1).for_match(11)
         .score(atp_players.Ofner, (6, 7, 6))
         .score(atp_players.Cressy, (4, 6, 2))),

        (draw.for_round(1).for_match(12)
         .score(atp_players.Mcdonald, (4, 5, 4))
         .score(atp_players.Korda, (6, 7, 6))),

        (draw.for_round(1).for_match(13)
         .score(atp_players.Zapata_Miralles, (6, 7, 2, 0, 4))
         .score(atp_players.Schwartzman, (1, 6, 6, 6, 6))),

        (draw.for_round(1).for_match(14)
         .score(atp_players.Isner, (4, 7, 6, 6, 6))
         .score(atp_players.Borges, (6, 5, 7, 4, 7))),

        (draw.for_round(1).for_match(15)
         .score(atp_players.Carballes_Baena, (7, 6, 6))
         .score(atp_players.Nava, (6, 3, 2))),

        (draw.for_round(1).for_match(16)
         .score(atp_players.Vesely, (5, 3, 6, 6))
         .score(atp_players.Tsitsipas, (7, 6, 4, 7))),

        (draw.for_round(1).for_match(17)
         .score(atp_players.Djokovic, (6, 6, 7))
         .score(atp_players.Kovacevic, (3, 2, 6))),

        (draw.for_round(1).for_match(18)
         .score(atp_players.Fucsovics, (6, 5, 6, 6))
         .score(atp_players.Grenier, (3, 7, 1, 3))),

        (draw.for_round(1).for_match(19)
         .score(atp_players.Van_Assche, (6, 6, 6))
         .score(atp_players.Cecchinato, (1, 1, 3))),

        (draw.for_round(1).for_match(20)
         .score(atp_players.Fils, (1, 6, 3, 3))
         .score(atp_players.Davidovich_Fokina, (6, 4, 6, 6))),

        (draw.for_round(1).for_match(21)
         .score(atp_players.Bautista_Agut, (7, 6, 6))
         .score(atp_players.Wu, (6, 1, 1))),

        (draw.for_round(1).for_match(22)
         .score(atp_players.Shang, (6, 6, 2, 3, 1))
         .score(atp_players.Varillas, (4, 2, 6, 6, 6))),

        (draw.for_round(1).for_match(23)
         .score(atp_players.Martinez, (4, 6, 6, 5, 3))
         .score(atp_players.Griekspoor, (6, 2, 0, 7, 6))),

        (draw.for_round(1).for_match(24)
         .score(atp_players.Goffin, (3, 7, 4, 6, 4))
         .score(atp_players.Hurkacz, (6, 5, 6, 2, 6))),

        (draw.for_round(1).for_match(25)
         .score(atp_players.Khachanov, (3, 1, 6, 6, 6))
         .score(atp_players.Lestienne, (6, 6, 2, 1, 3))),

        (draw.for_round(1).for_match(26)
         .score(atp_players.Kypson, (3, 2, 6, 1))
         .score(atp_players.Albot, (6, 6, 4, 6))),

        (draw.for_round(1).for_match(27)
         .score(atp_players.Wawrinka, (7, 6, 6, 1, 6))
         .score(atp_players.Ramos_Vinolas, (6, 4, 7, 6, 4))),

        (draw.for_round(1).for_match(28)
         .score(atp_players.Kokkinakis, (6, 6, 6))
         .score(atp_players.Evans, (4, 4, 4))),

        (draw.for_round(1).for_match(29)
         .score(atp_players.Shelton, (4, 6, 3, 3))
         .score(atp_players.Sonego, (6, 3, 6, 6))),

        (draw.for_round(1).for_match(30)
         .score(atp_players.Mannarino, (3, 3, 1))
         .score(atp_players.Humbert, (6, 6, 6))),

        (draw.for_round(1).for_match(31)
         .score(atp_players.Cazaux, (1, 3, 6, 4))
         .score(atp_players.Moutet, (6, 6, 4, 6))),

        (draw.for_round(1).for_match(32)
         .score(atp_players.Djere, (1, 6, 3, 4))
         .score(atp_players.Rublev, (6, 3, 6, 6))),

        (draw.for_round(1).for_match(33)
         .score(atp_players.Rune, (6, 3, 7, 6))
         .score(atp_players.Eubanks, (4, 6, 6, 2))),

        (draw.for_round(1).for_match(34)
         .score(atp_players.Monfils, (3, 6, 7, 1, 7))
         .score(atp_players.Baez, (6, 3, 5, 6, 5))),

        (draw.for_round(1).for_match(35)
         .score(atp_players.Mpetshi_Perricard, (6, 6, 6, 5, 1))
         .score(atp_players.Olivieri, (7, 4, 4, 7, 6))),

        (draw.for_round(1).for_match(36)
         .score(atp_players.Vavassori, (5, 2, 7, 7, 7))
         .score(atp_players.Kecmanovic, (7, 6, 6, 6, 6))),

        (draw.for_round(1).for_match(37)
         .score(atp_players.Cerundolo_Francisco, (6, 2, 7, 6))
         .score(atp_players.Munar, (1, 6, 6, 1))),

        (draw.for_round(1).for_match(38)
         .score(atp_players.Monteiro, (3, 5, 7, 7, 4))
         .score(atp_players.Hanfmann, (6, 7, 6, 6, 6))),

        (draw.for_round(1).for_match(39)
         .score(atp_players.Gasquet, (4, 6, 2, 6))
         .score(atp_players.Rinderknech, (6, 2, 6, 7))),

        (draw.for_round(1).for_match(40)
         .score(atp_players.Mmoh, (2, 1, 1))
         .score(atp_players.Fritz, (6, 6, 6))),

        (draw.for_round(1).for_match(41)
         .score(atp_players.Paul, (6, 6, 6))
         .score(atp_players.Stricker, (3, 2, 4))),

        (draw.for_round(1).for_match(42)
         .score(atp_players.Jarry, (6, 6, 6))
         .score(atp_players.Dellien, (4, 4, 2))),

        (draw.for_round(1).for_match(43)
         .score(atp_players.Medjedovic, (0, 2, 6, 0))
         .score(atp_players.Giron, (6, 6, 1, 6))),

        (draw.for_round(1).for_match(44)
         .score(atp_players.Lehecka, (7, 1, 6, 3, 6))
         .score(atp_players.Struff, (5, 6, 3, 6, 1))),

        (draw.for_round(1).for_match(45)
         .score(atp_players.Van_De_Zandschulp, (2, 6, 3, 4))
         .score(atp_players.Tirante, (6, 4, 6, 6))),

        (draw.for_round(1).for_match(46)
         .score(atp_players.Zhang_Zhizhen, (6, 4))
         .score(atp_players.Lajovic, (1, 1))
         .retirement(atp_players.Lajovic)),

        (draw.for_round(1).for_match(47)
         .score(atp_players.Bublik, (0, 6, 6, 3, 5))
         .score(atp_players.Zeppieri, (6, 4, 4, 6, 7))),

        (draw.for_round(1).for_match(48)
         .score(atp_players.Ymer_Elias, (4, 3, 2))
         .score(atp_players.Ruud, (6, 6, 6))),

        (draw.for_round(1).for_match(49)
         .score(atp_players.Sinner, (6, 6, 6))
         .score(atp_players.Muller, (1, 4, 1))),

        (draw.for_round(1).for_match(50)
         .score(atp_players.Altmaier, (6, 6, 6))
         .score(atp_players.Huesler, (3, 4, 4))),

        (draw.for_round(1).for_match(51)
         .score(atp_players.Ruusuvuori, (6, 6, 5, 6, 6))
         .score(atp_players.Barrere, (2, 7, 7, 1, 4))),

        (draw.for_round(1).for_match(52)
         .score(atp_players.Skatov, (0, 3, 2))
         .score(atp_players.Dimitrov, (6, 6, 6))),

        (draw.for_round(1).for_match(53)
         .score(atp_players.Zverev, (7, 7, 6))
         .score(atp_players.Harris, (6, 6, 1))),

        (draw.for_round(1).for_match(54)
         .score(atp_players.Gaston, (1, 6, 4))
         .score(atp_players.Molcan, (6, 7, 6))),

        (draw.for_round(1).for_match(55)
         .score(atp_players.Popyrin, (3, 7, 1, 2))
         .score(atp_players.Karatsev, (6, 6, 6, 6))),

        (draw.for_round(1).for_match(56)
         .score(atp_players.Krajinovic, (3, 4, 2))
         .score(atp_players.Tiafoe, (6, 6, 6))),

        (draw.for_round(1).for_match(57)
         .score(atp_players.Coric, (7, 6, 6, 6))
         .score(atp_players.Coria, (6, 7, 3, 3))),

        (draw.for_round(1).for_match(58)
         .score(atp_players.Thiem, (3, 2, 7, 6, 2))
         .score(atp_players.Cachin, (6, 6, 6, 4, 6))),

        (draw.for_round(1).for_match(59)
         .score(atp_players.Draper, (4, 0))
         .score(atp_players.Etcheverry, (6, 1))
         .retirement(atp_players.Draper)),

        (draw.for_round(1).for_match(60)
         .score(atp_players.Ivashka, (1, 7, 1, 3))
         .score(atp_players.De_Minaur, (6, 5, 6, 6))),

        (draw.for_round(1).for_match(61)
         .score(atp_players.Nishioka, (1, 3, 6, 6, 6))
         .score(atp_players.Wolf, (6, 6, 4, 3, 3))),

        (draw.for_round(1).for_match(62)
         .score(atp_players.Purcell, (7, 1, 6, 6))
         .score(atp_players.Thompson, (5, 6, 4, 4))),

        (draw.for_round(1).for_match(63)
         .score(atp_players.Halys, (4, 7, 6, 6, 6))
         .score(atp_players.Pella, (6, 6, 2, 7, 7))),

        (draw.for_round(1).for_match(64)
         .score(atp_players.Seyboth_Wild, (7, 6, 2, 6, 6))
         .score(atp_players.Medvedev, (6, 7, 6, 3, 4)))
    ]


def womens_singles_results_r1(draw):
    return [
        (draw.for_round(1).for_match(1)
         .score(wta_players.Swiatek, (6, 6))
         .score(wta_players.Bucsa, (4, 0))),

        (draw.for_round(1).for_match(2)
         .score(wta_players.In_Albon, (1, 4))
         .score(wta_players.Liu, (6, 6))),

        (draw.for_round(1).for_match(3)
         .score(wta_players.Peterson, (6, 6))
         .score(wta_players.Ferro, (2, 0))),

        (draw.for_round(1).for_match(4)
         .score(wta_players.Wang_Xinyu, (6, 7))
         .score(wta_players.Bouzkova, (4, 6))),

        (draw.for_round(1).for_match(5)
         .score(wta_players.Azarenka, (6, 3, 4))
         .score(wta_players.Andreescu, (2, 6, 6))),

        (draw.for_round(1).for_match(6)
         .score(wta_players.Andreeva_Erika, (2, 6, 4))
         .score(wta_players.Navarro, (6, 3, 6))),

        (draw.for_round(1).for_match(7)
         .score(wta_players.Zhu, (3, 3))
         .score(wta_players.Davis, (6, 6))),

        (draw.for_round(1).for_match(8)
         .score(wta_players.Tsurenko, (6, 6))
         .score(wta_players.Krejcikova, (2, 4))),

        (draw.for_round(1).for_match(9)
         .score(wta_players.Kudermetova_Veronika, (3, 1))
         .score(wta_players.Schmiedlova, (6, 6))),

        (draw.for_round(1).for_match(10)
         .score(wta_players.Bolsova, (6, 6))
         .score(wta_players.Kucova, (2, 1))),

        (draw.for_round(1).for_match(11)
         .score(wta_players.Day, (7, 6))
         .score(wta_players.Mladenovic, (5, 1))),

        (draw.for_round(1).for_match(12)
         .score(wta_players.Kanepi, (1, 6, 1))
         .score(wta_players.Keys, (6, 3, 6))),

        (draw.for_round(1).for_match(13)
         .score(wta_players.Kalinina, (2, 3))
         .score(wta_players.Parry, (6, 6))),

        (draw.for_round(1).for_match(14)
         .score(wta_players.Andreeva_Mirra, (6, 6))
         .score(wta_players.Riske_Amritraj, (2, 1))),

        (draw.for_round(1).for_match(15)
         .score(wta_players.Rus, (2, 3))
         .score(wta_players.Grabher, (6, 6))),

        (draw.for_round(1).for_match(16)
         .score(wta_players.Masarova, (6, 1, 2))
         .score(wta_players.Gauff, (3, 6, 6))),

        (draw.for_round(1).for_match(17)
         .score(wta_players.Rybakina, (6, 6))
         .score(wta_players.Fruhvirtova_Brenda, (4, 2))),

        (draw.for_round(1).for_match(18)
         .score(wta_players.Noskova, (6, 2))
         .score(wta_players.Kovinic, (3, 1))
         .retirement(wta_players.Kovinic)),

        (draw.for_round(1).for_match(19)
         .score(wta_players.Burel, (6, 2))
         .score(wta_players.Sorribes_Tormo, (7, 6))),

        (draw.for_round(1).for_match(20)
         .score(wta_players.Martic, (3, 6, 6))
         .score(wta_players.Rogers, (6, 3, 2))),

        (draw.for_round(1).for_match(21)
         .score(wta_players.Alexandrova, (6, 2, 6))
         .score(wta_players.Tomova, (1, 6, 1))),

        (draw.for_round(1).for_match(22)
         .score(wta_players.Hibino, (3, 6, 4))
         .score(wta_players.Friedsam, (6, 3, 6))),

        (draw.for_round(1).for_match(23)
         .score(wta_players.Marino, (3, 5))
         .score(wta_players.Shnaider, (6, 7))),

        (draw.for_round(1).for_match(24)
         .score(wta_players.Maria, (0, 1))
         .score(wta_players.Haddad_Maia, (6, 6))),

        (draw.for_round(1).for_match(25)
         .score(wta_players.Kvitova, (3, 4))
         .score(wta_players.Cocciaretto, (6, 6))),

        (draw.for_round(1).for_match(26)
         .score(wta_players.Waltert, (6, 4, 6))
         .score(wta_players.Mandlik, (1, 6, 2))),

        (draw.for_round(1).for_match(27)
         .score(wta_players.Kontaveit, (6, 2))
         .score(wta_players.Pera, (7, 6))),

        (draw.for_round(1).for_match(28)
         .score(wta_players.Yastremska, (2, 5))
         .score(wta_players.Vekic, (6, 7))),

        (draw.for_round(1).for_match(29)
         .score(wta_players.Cirstea, (5, 6, 2))
         .score(wta_players.Paolini, (7, 2, 6))),

        (draw.for_round(1).for_match(30)
         .score(wta_players.Danilovic, (6, 6))
         .score(wta_players.Baindl, (3, 2))),

        (draw.for_round(1).for_match(31)
         .score(wta_players.Janicijevic, (6, 2, 1))
         .score(wta_players.Dodin, (0, 6, 6))),

        (draw.for_round(1).for_match(32)
         .score(wta_players.Bronzetti, (4, 1))
         .score(wta_players.Jabeur, (6, 6))),

        (draw.for_round(1).for_match(33)
         .score(wta_players.Sakkari, (6, 5))
         .score(wta_players.Muchova, (7, 7))),

        (draw.for_round(1).for_match(34)
         .score(wta_players.Podoroska, (6, 6))
         .score(wta_players.Ponchet, (0, 2))),

        (draw.for_round(1).for_match(35)
         .score(wta_players.Errani, (3, 6, 6))
         .score(wta_players.Teichmann, (6, 4, 2))),

        (draw.for_round(1).for_match(36)
         .score(wta_players.Bondar, (4, 2))
         .score(wta_players.Begu, (6, 6))),

        (draw.for_round(1).for_match(37)
         .score(wta_players.Linette, (3, 6, 3))
         .score(wta_players.Fernandez, (6, 1, 6))),

        (draw.for_round(1).for_match(38)
         .score(wta_players.Tauson, (6, 6))
         .score(wta_players.Sasnovich, (2, 0))),

        (draw.for_round(1).for_match(39)
         .score(wta_players.Jeanjean, (6, 6, 6))
         .score(wta_players.Birrell, (4, 7, 3))),

        (draw.for_round(1).for_match(40)
         .score(wta_players.Avanesyan, (6, 2, 6))
         .score(wta_players.Bencic, (3, 6, 4))),

        (draw.for_round(1).for_match(41)
         .score(wta_players.Samsonova, (6, 6))
         .score(wta_players.Volynets, (0, 1))),

        (draw.for_round(1).for_match(42)
         .score(wta_players.Pavlyuchenkova, (6, 6))
         .score(wta_players.Fruhvirtova_Linda, (2, 2))),

        (draw.for_round(1).for_match(43)
         .score(wta_players.Sherif, (6, 6))
         .score(wta_players.Brengle, (3, 1))),

        (draw.for_round(1).for_match(44)
         .score(wta_players.Townsend, (1, 2))
         .score(wta_players.Potapova, (6, 6))),

        (draw.for_round(1).for_match(45)
         .score(wta_players.Mertens, (6, 6))
         .score(wta_players.Hruncakova, (1, 4))),

        (draw.for_round(1).for_match(46)
         .score(wta_players.Osorio, (3, 6, 7))
         .score(wta_players.Bogdan, (6, 3, 5))),

        (draw.for_round(1).for_match(47)
         .score(wta_players.Cornet, (3, 4))
         .score(wta_players.Giorgi, (6, 6))),

        (draw.for_round(1).for_match(48)
         .score(wta_players.Collins, (4, 2))
         .score(wta_players.Pegula, (6, 6))),

        (draw.for_round(1).for_match(49)
         .score(wta_players.Garcia, (7, 4, 6))
         .score(wta_players.Wang_Xinyu, (6, 6, 4))),

        (draw.for_round(1).for_match(50)
         .score(wta_players.Blinkova, (6, 6))
         .score(wta_players.Bonaventure, (2, 0))),

        (draw.for_round(1).for_match(51)
         .score(wta_players.Parrizas_Diaz, (6, 2, 4))
         .score(wta_players.Hunter, (4, 6, 6))),

        (draw.for_round(1).for_match(52)
         .score(wta_players.Svitolina, (6, 6))
         .score(wta_players.Trevisan, (2, 2))),

        (draw.for_round(1).for_match(53)
         .score(wta_players.Ostapenko, (6, 7))
         .score(wta_players.Martincova, (3, 5))),

        (draw.for_round(1).for_match(54)
         .score(wta_players.Stearns, (7, 6))
         .score(wta_players.Siniakova, (6, 2))),

        (draw.for_round(1).for_match(55)
         .score(wta_players.Vondrousova, (6, 6))
         .score(wta_players.Parks, (4, 0))),

        (draw.for_round(1).for_match(56)
         .score(wta_players.Niemeier, (3, 4))
         .score(wta_players.Kasatkina, (6, 6))),

        (draw.for_round(1).for_match(57)
         .score(wta_players.Pliskova, (0, 4))
         .score(wta_players.Stephens, (6, 6))),

        (draw.for_round(1).for_match(58)
         .score(wta_players.Gracheva, (6, 2, 6))
         .score(wta_players.Galfi, (4, 6, 1))),

        (draw.for_round(1).for_match(59)
         .score(wta_players.Putintseva, (7, 7))
         .score(wta_players.Zanevska, (5, 6))),

        (draw.for_round(1).for_match(60)
         .score(wta_players.Zidansek, (3, 1))
         .score(wta_players.Zheng, (6, 6))),

        (draw.for_round(1).for_match(61)
         .score(wta_players.Zhang_Shuai, (1, 1))
         .score(wta_players.Frech, (6, 6))),

        (draw.for_round(1).for_match(62)
         .score(wta_players.Bejlek, (0, 3))
         .score(wta_players.Rakhimova, (6, 6))),

        (draw.for_round(1).for_match(63)
         .score(wta_players.Udvardy, (7, 3, 1))
         .score(wta_players.Shymanovich, (6, 6, 6))),

        (draw.for_round(1).for_match(64)
         .score(wta_players.Kostyuk, (3, 2))
         .score(wta_players.Sabalenka, (6, 6)))
    ]
