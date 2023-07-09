from tejos.players import wta_players, atp_players


# WM2023WomensSingles_r7:START

# WM2023WomensSingles_r7:END


# WM2023MensSingles_r7:START

# WM2023MensSingles_r7:END


# WM2023WomensSingles_r6:START

# WM2023WomensSingles_r6:END


# WM2023MensSingles_r6:START

# WM2023MensSingles_r6:END


# WM2023WomensSingles_r5:START

# WM2023WomensSingles_r5:END


# WM2023MensSingles_r5:START

# WM2023MensSingles_r5:END


# WM2023WomensSingles_r4:START
def womens_singles_results_r4(draw):
  return [

   ]
# WM2023WomensSingles_r4:END


# WM2023MensSingles_r4:START
def mens_singles_results_r4(draw):
  return [

   ]
# WM2023MensSingles_r4:END


# WM2023WomensSingles_r3:START
def womens_singles_results_r3(draw):
  return [
        (draw.for_round(3).for_match(1)
        .score(wta_players.Swiatek, (6, 7))
        .score(wta_players.Martic, (2, 5))),


        (draw.for_round(3).for_match(2)
        .score(wta_players.Linette, (3, 1))
        .score(wta_players.Bencic, (6, 6))),


        (draw.for_round(3).for_match(3)
        .score(wta_players.Kasatkina, (2, 4))
        .score(wta_players.Azarenka, (6, 6))),


        (draw.for_round(3).for_match(4)
        .score(wta_players.Svitolina, (7, 6))
        .score(wta_players.Kenin, (6, 2))),


        (draw.for_round(3).for_match(5)
        .score(wta_players.Pegula, (6, 6))
        .score(wta_players.Cocciaretto, (4, 0))),


        (draw.for_round(3).for_match(6)
        .score(wta_players.Tsurenko, (4, 6, 7))
        .score(wta_players.Bogdan, (6, 3, 6))),


        (draw.for_round(3).for_match(7)
        .score(wta_players.Vondrousova, (6, 7))
        .score(wta_players.Vekic, (1, 5))),


        (draw.for_round(3).for_match(8)
        .score(wta_players.Bouzkova, (7, 4, 7))
        .score(wta_players.Garcia, (6, 6, 5))),


        (draw.for_round(3).for_match(9)
        .score(wta_players.Jabeur, (3, 6, 6))
        .score(wta_players.Andreescu, (6, 3, 4))),


        (draw.for_round(3).for_match(10)
        .score(wta_players.Stevanovic, (3, 5))
        .score(wta_players.Kvitova, (6, 7))),


        (draw.for_round(3).for_match(11)
        .score(wta_players.Haddad_Maia, (6, 6))
        .score(wta_players.Cirstea, (2, 2))),


        (draw.for_round(3).for_match(12)
        .score(wta_players.Boulter, (1, 1))
        .score(wta_players.Rybakina, (6, 6))),


        (draw.for_round(3).for_match(13)
        .score(wta_players.Kostyuk, (4, 1))
        .score(wta_players.Keys, (6, 6))),


        (draw.for_round(3).for_match(14)
        .score(wta_players.Potapova, (2, 5))
        .score(wta_players.Andreeva_Mirra, (6, 7))),


        (draw.for_round(3).for_match(15)
        .score(wta_players.Galfi, (0, 4))
        .score(wta_players.Alexandrova, (6, 6))),


        (draw.for_round(3).for_match(16)
        .score(wta_players.Blinkova, (2, 3))
        .score(wta_players.Sabalenka, (6, 6))),



   ]
# WM2023WomensSingles_r3:END


# WM2023MensSingles_r3:START
def mens_singles_results_r3(draw):
  return [
        (draw.for_round(3).for_match(1)
        .score(atp_players.Alcaraz, (6, 6, 6, 7))
        .score(atp_players.Jarry, (3, 7, 3, 5))),


        (draw.for_round(3).for_match(2)
        .score(atp_players.Zverev, (3, 6, 6))
        .score(atp_players.Berrettini, (6, 7, 7))),


        (draw.for_round(3).for_match(3)
        .score(atp_players.Tiafoe, (2, 3, 2))
        .score(atp_players.Dimitrov, (6, 6, 6))),


        (draw.for_round(3).for_match(4)
        .score(atp_players.Davidovich_Fokina, (3, 6, 6, 4, 6))
        .score(atp_players.Rune, (6, 4, 3, 6, 7))),


        (draw.for_round(3).for_match(5)
        .score(atp_players.Medvedev, (4, 6, 6, 6))
        .score(atp_players.Fucsovics, (6, 3, 4, 4))),


        (draw.for_round(3).for_match(6)
        .score(atp_players.Lehecka, (6, 7, 6, 6, 6))
        .score(atp_players.Paul, (2, 6, 7, 7, 2))),


        (draw.for_round(3).for_match(7)
        .score(atp_players.Eubanks, (7, 7, 7))
        .score(atp_players.OConnell, (6, 6, 6))),


        (draw.for_round(3).for_match(8)
        .score(atp_players.Djere, (4, 6, 4))
        .score(atp_players.Tsitsipas, (6, 7, 6))),


        (draw.for_round(3).for_match(9)
        .score(atp_players.Sinner, (3, 6, 6, 6))
        .score(atp_players.Halys, (6, 2, 3, 4))),


        (draw.for_round(3).for_match(10)
        .score(atp_players.Galan, (6, 6, 7, 3, 6))
        .score(atp_players.Ymer_Mikael, (2, 7, 6, 6, 1))),


        (draw.for_round(3).for_match(11)
        .score(atp_players.Pella, (6, 4, 0))
        .score(atp_players.Safiullin, (7, 6, 6))),


        (draw.for_round(3).for_match(12)
        .score(atp_players.Shapovalov, (4, 6, 7, 7))
        .score(atp_players.Broady, (6, 2, 5, 5))),


        (draw.for_round(3).for_match(13)
        .score(atp_players.Rublev, (6, 6, 7, 6))
        .score(atp_players.Goffin, (3, 7, 6, 2))),


        (draw.for_round(3).for_match(14)
        .score(atp_players.Bublik, (6, 6, 7))
        .score(atp_players.Marterer, (4, 1, 6))),


        (draw.for_round(3).for_match(15)
        .score(atp_players.Musetti, (6, 4, 4))
        .score(atp_players.Hurkacz, (7, 6, 6))),


        (draw.for_round(3).for_match(16)
        .score(atp_players.Wawrinka, (3, 1, 6))
        .score(atp_players.Djokovic, (6, 6, 7))),



   ]
# WM2023MensSingles_r3:END


# WM2023WomensSingles_r2:START
def womens_singles_results_r2(draw):
    return [
        (draw.for_round(2).for_match(1)
         .score(wta_players.Swiatek, (6, 6))
         .score(wta_players.Sorribes_Tormo, (2, 0))),

        (draw.for_round(2).for_match(2)
         .score(wta_players.Parry, (6, 3, 3))
         .score(wta_players.Martic, (4, 6, 6))),

        (draw.for_round(2).for_match(3)
         .score(wta_players.Linette, (6, 6, 6))
         .score(wta_players.Strycova, (4, 7, 3))),

        (draw.for_round(2).for_match(4)
         .score(wta_players.Collins, (6, 4, 6))
         .score(wta_players.Bencic, (3, 6, 7))),

        (draw.for_round(2).for_match(5)
         .score(wta_players.Kasatkina, (6, 6))
         .score(wta_players.Burrage, (0, 2))),

        (draw.for_round(2).for_match(6)
         .score(wta_players.Podoroska, (3, 0))
         .score(wta_players.Azarenka, (6, 6))),

        (draw.for_round(2).for_match(7)
         .score(wta_players.Mertens, (1, 6, 1))
         .score(wta_players.Svitolina, (6, 1, 6))),

        (draw.for_round(2).for_match(8)
         .score(wta_players.Wang_Xinyu, (4, 3))
         .score(wta_players.Kenin, (6, 6))),

        (draw.for_round(2).for_match(9)
         .score(wta_players.Pegula, (6, 6))
         .score(wta_players.Bucsa, (1, 4))),

        (draw.for_round(2).for_match(10)
         .score(wta_players.Cocciaretto, (6, 6))
         .score(wta_players.Masarova, (3, 1))),

        (draw.for_round(2).for_match(11)
         .score(wta_players.Siniakova, (4, 1))
         .score(wta_players.Tsurenko, (6, 6))),

        (draw.for_round(2).for_match(12)
         .score(wta_players.Parks, (6, 3, 2))
         .score(wta_players.Bogdan, (1, 6, 6))),

        (draw.for_round(2).for_match(13)
         .score(wta_players.Kudermetova_Veronika, (3, 3))
         .score(wta_players.Vondrousova, (6, 6))),

        (draw.for_round(2).for_match(14)
         .score(wta_players.Stephens, (6, 5, 4))
         .score(wta_players.Vekic, (4, 7, 6))),

        (draw.for_round(2).for_match(15)
         .score(wta_players.Bouzkova, (6, 6))
         .score(wta_players.Kontaveit, (1, 2))),

        (draw.for_round(2).for_match(16)
         .score(wta_players.Fernandez, (6, 4, 6))
         .score(wta_players.Garcia, (3, 6, 7))),

        (draw.for_round(2).for_match(17)
         .score(wta_players.Jabeur, (6, 6))
         .score(wta_players.Bai, (1, 1))),

        (draw.for_round(2).for_match(18)
         .score(wta_players.Andreescu, (6, 4, 7))
         .score(wta_players.Kalinina, (2, 6, 6))),

        (draw.for_round(2).for_match(19)
         .score(wta_players.Stevanovic, (7, 7))
         .score(wta_players.Korpatsch, (5, 5))),

        (draw.for_round(2).for_match(20)
         .score(wta_players.Sasnovich, (2, 2))
         .score(wta_players.Kvitova, (6, 6))),

        (draw.for_round(2).for_match(21)
         .score(wta_players.Haddad_Maia, (4, 6, 6))
         .score(wta_players.Cristian, (6, 2, 4))),

        (draw.for_round(2).for_match(22)
         .score(wta_players.Cirstea, (4, 7, 6))
         .score(wta_players.Ostapenko, (6, 6, 4))),

        (draw.for_round(2).for_match(23)
         .score(wta_players.Tomova, (0, 6, 3))
         .score(wta_players.Boulter, (6, 3, 6))),

        (draw.for_round(2).for_match(24)
         .score(wta_players.Cornet, (2, 6))
         .score(wta_players.Rybakina, (6, 7))),

        (draw.for_round(2).for_match(25)
         .score(wta_players.Kostyuk, (6, 1))
         .score(wta_players.Badosa, (2, 0))
         .retirement(wta_players.Badosa)),

        (draw.for_round(2).for_match(26)
         .score(wta_players.Golubic, (5, 3))
         .score(wta_players.Keys, (7, 6))),

        (draw.for_round(2).for_match(27)
         .score(wta_players.Potapova, (6, 7))
         .score(wta_players.Juvan, (3, 5))),

        (draw.for_round(2).for_match(28)
         .score(wta_players.Andreeva_Mirra, (6, 4))
         .score(wta_players.Krejcikova, (3, 0))
         .retirement(wta_players.Krejcikova)),

        (draw.for_round(2).for_match(29)
         .score(wta_players.Niemeier, (6, 6, 1))
         .score(wta_players.Galfi, (4, 7, 6))),

        (draw.for_round(2).for_match(30)
         .score(wta_players.Brengle, (7, 6, 6))
         .score(wta_players.Alexandrova, (6, 7, 7))),

        (draw.for_round(2).for_match(31)
         .score(wta_players.Begu, (5, 3))
         .score(wta_players.Blinkova, (7, 6))),

        (draw.for_round(2).for_match(32)
         .score(wta_players.Gracheva, (6, 5, 2))
         .score(wta_players.Sabalenka, (2, 7, 6))),

    ]


# WM2023WomensSingles_r2:END


# WM2023MensSingles_r2:START
def mens_singles_results_r2(draw):
    return [
        (draw.for_round(2).for_match(1)
         .score(atp_players.Alcaraz, (6, 7, 6))
         .score(atp_players.Muller, (4, 6, 3))),

        (draw.for_round(2).for_match(2)
         .score(atp_players.Kubler, (5, 7, 3, 4))
         .score(atp_players.Jarry, (7, 5, 6, 6))),

        (draw.for_round(2).for_match(3)
         .score(atp_players.Zverev, (6, 5, 6, 6))
         .score(atp_players.Watanuki, (4, 7, 2, 2))),

        (draw.for_round(2).for_match(4)
         .score(atp_players.Berrettini, (6, 6, 6))
         .score(atp_players.De_Minaur, (3, 4, 4))),

        (draw.for_round(2).for_match(5)
         .score(atp_players.Tiafoe, (7, 6, 6))
         .score(atp_players.Stricker, (6, 4, 2))),

        (draw.for_round(2).for_match(6)
         .score(atp_players.Ivashka, (3, 4, 4))
         .score(atp_players.Dimitrov, (6, 6, 6))),

        (draw.for_round(2).for_match(7)
         .score(atp_players.Davidovich_Fokina, (6, 2, 6, 6))
         .score(atp_players.Van_De_Zandschulp, (1, 6, 4, 3))),

        (draw.for_round(2).for_match(8)
         .score(atp_players.Carballes_Baena, (3, 6, 4))
         .score(atp_players.Rune, (6, 7, 6))),

        (draw.for_round(2).for_match(9)
         .score(atp_players.Medvedev, (6, 6, 7))
         .score(atp_players.Mannarino, (3, 3, 6))),

        (draw.for_round(2).for_match(10)
         .score(atp_players.Giron, (6, 3, 6, 4))
         .score(atp_players.Fucsovics, (7, 6, 4, 6))),

        (draw.for_round(2).for_match(11)
         .score(atp_players.Cerundolo_Francisco, (2, 2, 2))
         .score(atp_players.Lehecka, (6, 6, 6))),

        (draw.for_round(2).for_match(12)
         .score(atp_players.Raonic, (4, 6, 7, 4))
         .score(atp_players.Paul, (6, 7, 6, 6))),

        (draw.for_round(2).for_match(13)
         .score(atp_players.Norrie, (3, 6, 2, 6))
         .score(atp_players.Eubanks, (6, 3, 6, 7))),

        (draw.for_round(2).for_match(14)
         .score(atp_players.OConnell, (6, 7, 6))
         .score(atp_players.Vesely, (3, 5, 4))),

        (draw.for_round(2).for_match(15)
         .score(atp_players.Shelton, (6, 3, 6, 3))
         .score(atp_players.Djere, (3, 6, 7, 6))),

        (draw.for_round(2).for_match(16)
         .score(atp_players.Murray_Andy, (6, 7, 6, 6, 4))
         .score(atp_players.Tsitsipas, (7, 6, 4, 7, 6))),

        (draw.for_round(2).for_match(17)
         .score(atp_players.Sinner, (7, 6, 6))
         .score(atp_players.Schwartzman, (5, 1, 2))),

        (draw.for_round(2).for_match(18)
         .score(atp_players.Vukic, (3, 1, 4))
         .score(atp_players.Halys, (6, 6, 6))),

        (draw.for_round(2).for_match(19)
         .score(atp_players.Galan, (6, 3, 6, 7))
         .score(atp_players.Otte, (3, 6, 3, 6))),

        (draw.for_round(2).for_match(20)
         .score(atp_players.Ymer_Mikael, (3, 2, 6, 6, 6))
         .score(atp_players.Fritz, (6, 6, 3, 4, 2))),

        (draw.for_round(2).for_match(21)
         .score(atp_players.Pella, (2, 6, 7, 7))
         .score(atp_players.Mayot, (6, 3, 6, 5))),

        (draw.for_round(2).for_match(22)
         .score(atp_players.Moutet, (5, 3, 6))
         .score(atp_players.Safiullin, (7, 6, 7))),

        (draw.for_round(2).for_match(23)
         .score(atp_players.Shapovalov, (6, 6, 7))
         .score(atp_players.Barrere, (3, 4, 6))),

        (draw.for_round(2).for_match(24)
         .score(atp_players.Broady, (6, 3, 4, 6, 6))
         .score(atp_players.Ruud, (4, 6, 6, 3, 0))),

        (draw.for_round(2).for_match(25)
         .score(atp_players.Rublev, (6, 6, 6, 7))
         .score(atp_players.Karatsev, (7, 3, 4, 5))),

        (draw.for_round(2).for_match(26)
         .score(atp_players.Vera, (6, 7, 2, 0))
         .score(atp_players.Goffin, (7, 5, 6, 6))),

        (draw.for_round(2).for_match(27)
         .score(atp_players.Bublik, (6, 7, 6))
         .score(atp_players.Wolf, (3, 6, 0))),

        (draw.for_round(2).for_match(28)
         .score(atp_players.Marterer, (7, 7, 6))
         .score(atp_players.Mmoh, (5, 6, 4))),

        (draw.for_round(2).for_match(29)
         .score(atp_players.Musetti, (6, 6, 6))
         .score(atp_players.Munar, (4, 3, 1))),

        (draw.for_round(2).for_match(30)
         .score(atp_players.Choinski, (4, 4, 6))
         .score(atp_players.Hurkacz, (6, 6, 7))),

        (draw.for_round(2).for_match(31)
         .score(atp_players.Etcheverry, (3, 6, 4, 2))
         .score(atp_players.Wawrinka, (6, 4, 6, 6))),

        (draw.for_round(2).for_match(32)
         .score(atp_players.Thompson, (3, 6, 5))
         .score(atp_players.Djokovic, (6, 7, 7))),

    ]


# WM2023MensSingles_r2:END


def womens_singles_results_r1(draw):
    return [
        (draw.for_round(1).for_match(1)
         .score(wta_players.Swiatek, (6, 6))
         .score(wta_players.Zhu, (1, 3))),

        (draw.for_round(1).for_match(2)
         .score(wta_players.Trevisan, (3, 1))
         .score(wta_players.Sorribes_Tormo, (6, 6))),

        (draw.for_round(1).for_match(3)
         .score(wta_players.Parry, (6, 6, 6))
         .score(wta_players.Dart, (7, 0, 4))),

        (draw.for_round(1).for_match(4)
         .score(wta_players.Fruhvirtova_Linda, (5, 7, 1))
         .score(wta_players.Martic, (7, 6, 4))
         .retirement(wta_players.Fruhvirtova_Linda)),

        (draw.for_round(1).for_match(5)
         .score(wta_players.Linette, (6, 6))
         .score(wta_players.Teichmann, (3, 2))),

        (draw.for_round(1).for_match(6)
         .score(wta_players.Strycova, (6, 7))
         .score(wta_players.Zanevska, (1, 5))),

        (draw.for_round(1).for_match(7)
         .score(wta_players.Collins, (6, 6))
         .score(wta_players.Grabher, (4, 4))),

        (draw.for_round(1).for_match(8)
         .score(wta_players.Swan, (5, 2))
         .score(wta_players.Bencic, (7, 6))),

        (draw.for_round(1).for_match(9)
         .score(wta_players.Kasatkina, (6, 6))
         .score(wta_players.Dolehide, (1, 4))),

        (draw.for_round(1).for_match(10)
         .score(wta_players.Burrage, (6, 6))
         .score(wta_players.Mcnally, (1, 3))),

        (draw.for_round(1).for_match(11)
         .score(wta_players.Podoroska, (3, 7, 6))
         .score(wta_players.Martincova, (6, 6, 4))),

        (draw.for_round(1).for_match(12)
         .score(wta_players.Yuan, (4, 7, 4))
         .score(wta_players.Azarenka, (6, 5, 6))),

        (draw.for_round(1).for_match(13)
         .score(wta_players.Mertens, (7, 6))
         .score(wta_players.Hruncakova, (6, 2))),

        (draw.for_round(1).for_match(14)
         .score(wta_players.Williams, (4, 3))
         .score(wta_players.Svitolina, (6, 6))),

        (draw.for_round(1).for_match(15)
         .score(wta_players.Hunter, (3, 1))
         .score(wta_players.Wang_Xinyu, (6, 6))),

        (draw.for_round(1).for_match(16)
         .score(wta_players.Kenin, (6, 4, 6))
         .score(wta_players.Gauff, (4, 6, 2))),

        (draw.for_round(1).for_match(17)
         .score(wta_players.Pegula, (6, 6, 6))
         .score(wta_players.Davis, (2, 7, 3))),

        (draw.for_round(1).for_match(18)
         .score(wta_players.Bucsa, (6, 4, 7))
         .score(wta_players.Rakhimova, (3, 6, 6))),

        (draw.for_round(1).for_match(19)
         .score(wta_players.Osorio, (3, 4))
         .score(wta_players.Cocciaretto, (6, 6))),

        (draw.for_round(1).for_match(20)
         .score(wta_players.Masarova, (7, 3, 7))
         .score(wta_players.Sherif, (5, 6, 6))),

        (draw.for_round(1).for_match(21)
         .score(wta_players.Zheng, (3, 5))
         .score(wta_players.Siniakova, (6, 7))),

        (draw.for_round(1).for_match(22)
         .score(wta_players.Tsurenko, (6, 3, 6))
         .score(wta_players.Liu, (3, 6, 4))),

        (draw.for_round(1).for_match(23)
         .score(wta_players.Parks, (6, 6))
         .score(wta_players.Friedsam, (4, 3))),

        (draw.for_round(1).for_match(24)
         .score(wta_players.Bogdan, (7, 7))
         .score(wta_players.Samsonova, (6, 6))),

        (draw.for_round(1).for_match(25)
         .score(wta_players.Kudermetova_Veronika, (7, 6))
         .score(wta_players.Kanepi, (6, 4))),

        (draw.for_round(1).for_match(26)
         .score(wta_players.Vondrousova, (6, 7))
         .score(wta_players.Stearns, (2, 5))),

        (draw.for_round(1).for_match(27)
         .score(wta_players.Stephens, (6, 6))
         .score(wta_players.Peterson, (2, 3))),

        (draw.for_round(1).for_match(28)
         .score(wta_players.Zhang_Shuai, (2, 3))
         .score(wta_players.Vekic, (6, 6))),

        (draw.for_round(1).for_match(29)
         .score(wta_players.Bouzkova, (6, 6))
         .score(wta_players.Waltert, (1, 4))),

        (draw.for_round(1).for_match(30)
         .score(wta_players.Kontaveit, (6, 6))
         .score(wta_players.Stefanini, (4, 4))),

        (draw.for_round(1).for_match(31)
         .score(wta_players.Baindl, (4, 6, 4))
         .score(wta_players.Fernandez, (6, 4, 6))),

        (draw.for_round(1).for_match(32)
         .score(wta_players.Volynets, (4, 3))
         .score(wta_players.Garcia, (6, 6))),

        (draw.for_round(1).for_match(33)
         .score(wta_players.Jabeur, (6, 6))
         .score(wta_players.Frech, (3, 3))),

        (draw.for_round(1).for_match(34)
         .score(wta_players.Bonaventure, (6, 1))
         .score(wta_players.Bai, (7, 6))),

        (draw.for_round(1).for_match(35)
         .score(wta_players.Bondar, (3, 6, 2))
         .score(wta_players.Andreescu, (6, 3, 6))),

        (draw.for_round(1).for_match(36)
         .score(wta_players.Maneiro, (4, 3))
         .score(wta_players.Kalinina, (6, 6))),

        (draw.for_round(1).for_match(37)
         .score(wta_players.Pliskova, (2, 3))
         .score(wta_players.Stevanovic, (6, 6))),

        (draw.for_round(1).for_match(38)
         .score(wta_players.Zhao, (6, 4, 2))
         .score(wta_players.Korpatsch, (1, 6, 6))),

        (draw.for_round(1).for_match(39)
         .score(wta_players.Sasnovich, (6, 6))
         .score(wta_players.Parrizas_Diaz, (2, 1))),

        (draw.for_round(1).for_match(40)
         .score(wta_players.Paolini, (4, 7, 1))
         .score(wta_players.Kvitova, (6, 6, 6))),

        (draw.for_round(1).for_match(41)
         .score(wta_players.Haddad_Maia, (3, 6, 6))
         .score(wta_players.Putintseva, (6, 0, 4))),

        (draw.for_round(1).for_match(42)
         .score(wta_players.Cristian, (6, 6))
         .score(wta_players.Bronzetti, (3, 4))),

        (draw.for_round(1).for_match(43)
         .score(wta_players.Cirstea, (6, 2, 6))
         .score(wta_players.Maria, (1, 6, 3))),

        (draw.for_round(1).for_match(44)
         .score(wta_players.Minnen, (1, 2))
         .score(wta_players.Ostapenko, (6, 6))),

        (draw.for_round(1).for_match(45)
         .score(wta_players.Pera, (7, 3, 3))
         .score(wta_players.Tomova, (6, 6, 6))),

        (draw.for_round(1).for_match(46)
         .score(wta_players.Boulter, (7, 6))
         .score(wta_players.Saville, (6, 2))),

        (draw.for_round(1).for_match(47)
         .score(wta_players.Hibino, (2, 2))
         .score(wta_players.Cornet, (6, 6))),

        (draw.for_round(1).for_match(48)
         .score(wta_players.Rogers, (6, 1, 2))
         .score(wta_players.Rybakina, (4, 6, 6))),

        (draw.for_round(1).for_match(49)
         .score(wta_players.Sakkari, (6, 5, 2))
         .score(wta_players.Kostyuk, (0, 7, 6))),

        (draw.for_round(1).for_match(50)
         .score(wta_players.Riske_Amritraj, (3, 3))
         .score(wta_players.Badosa, (6, 6))),

        (draw.for_round(1).for_match(51)
         .score(wta_players.Golubic, (6, 7))
         .score(wta_players.Schmiedlova, (3, 6))),

        (draw.for_round(1).for_match(52)
         .score(wta_players.Kartal, (0, 3))
         .score(wta_players.Keys, (6, 6))),

        (draw.for_round(1).for_match(53)
         .score(wta_players.Potapova, (6, 6))
         .score(wta_players.Naef, (3, 3))),

        (draw.for_round(1).for_match(54)
         .score(wta_players.Juvan, (6, 6))
         .score(wta_players.Betova, (0, 3))),

        (draw.for_round(1).for_match(55)
         .score(wta_players.Andreeva_Mirra, (6, 3, 7))
         .score(wta_players.Wang_Xiyu, (4, 6, 5))),

        (draw.for_round(1).for_match(56)
         .score(wta_players.Watson, (2, 5))
         .score(wta_players.Krejcikova, (6, 7))),

        (draw.for_round(1).for_match(57)
         .score(wta_players.Muchova, (4, 7, 1))
         .score(wta_players.Niemeier, (6, 5, 6))),

        (draw.for_round(1).for_match(58)
         .score(wta_players.Noskova, (7, 2, 2))
         .score(wta_players.Galfi, (6, 6, 6))),

        (draw.for_round(1).for_match(59)
         .score(wta_players.Brengle, (6, 6))
         .score(wta_players.Errani, (3, 1))),

        (draw.for_round(1).for_match(60)
         .score(wta_players.Navarro, (4, 3))
         .score(wta_players.Alexandrova, (6, 6))),

        (draw.for_round(1).for_match(61)
         .score(wta_players.Begu, (6, 3, 6))
         .score(wta_players.Marino, (2, 6, 2))),

        (draw.for_round(1).for_match(62)
         .score(wta_players.Wickmayer, (2, 6, 3))
         .score(wta_players.Blinkova, (6, 4, 6))),

        (draw.for_round(1).for_match(63)
         .score(wta_players.Gracheva, (6, 6))
         .score(wta_players.Giorgi, (2, 4))),

        (draw.for_round(1).for_match(64)
         .score(wta_players.Udvardy, (3, 1))
         .score(wta_players.Sabalenka, (6, 6))),

    ]


def mens_singles_results_r1(draw):
    return [
        (draw.for_round(1).for_match(1)
         .score(atp_players.Alcaraz, (6, 6, 7))
         .score(atp_players.Chardy, (0, 2, 5))),

        (draw.for_round(1).for_match(2)
         .score(atp_players.Muller, (7, 1, 6, 6))
         .score(atp_players.Rinderknech, (6, 6, 3, 4))),

        (draw.for_round(1).for_match(3)
         .score(atp_players.Kubler, (6, 4, 6, 3, 6))
         .score(atp_players.Humbert, (4, 6, 2, 6, 3))),

        (draw.for_round(1).for_match(4)
         .score(atp_players.Cecchinato, (6, 2, 4, 1))
         .score(atp_players.Jarry, (4, 6, 6, 6))),

        (draw.for_round(1).for_match(5)
         .score(atp_players.Zverev, (6, 7, 7))
         .score(atp_players.Brouwer, (4, 6, 6))),

        (draw.for_round(1).for_match(6)
         .score(atp_players.Huesler, (7, 7, 6, 6, 3))
         .score(atp_players.Watanuki, (6, 5, 7, 7, 6))),

        (draw.for_round(1).for_match(7)
         .score(atp_players.Berrettini, (6, 6, 7, 6))
         .score(atp_players.Sonego, (7, 3, 6, 3))),

        (draw.for_round(1).for_match(8)
         .score(atp_players.Coppejans, (7, 3, 3, 6))
         .score(atp_players.De_Minaur, (6, 6, 6, 7))),

        (draw.for_round(1).for_match(9)
         .score(atp_players.Tiafoe, (7, 6, 6))
         .score(atp_players.Wu, (6, 3, 4))),

        (draw.for_round(1).for_match(10)
         .score(atp_players.Stricker, (3, 6, 6, 4, 7))
         .score(atp_players.Popyrin, (6, 3, 2, 6, 5))),

        (draw.for_round(1).for_match(11)
         .score(atp_players.Ivashka, (4, 6, 6, 6))
         .score(atp_players.Coria, (6, 4, 3, 0))),

        (draw.for_round(1).for_match(12)
         .score(atp_players.Shimabukuro, (1, 2, 1))
         .score(atp_players.Dimitrov, (6, 6, 6))),

        (draw.for_round(1).for_match(13)
         .score(atp_players.Davidovich_Fokina, (7, 6, 6))
         .score(atp_players.Fils, (6, 1, 2))),

        (draw.for_round(1).for_match(14)
         .score(atp_players.Zhang_Zhizhen, (6, 6, 6, 6, 2))
         .score(atp_players.Van_De_Zandschulp, (2, 7, 7, 3, 6))),

        (draw.for_round(1).for_match(15)
         .score(atp_players.Arnaldi, (7, 3, 4, 4))
         .score(atp_players.Carballes_Baena, (6, 6, 6, 6))),

        (draw.for_round(1).for_match(16)
         .score(atp_players.Loffhagen, (6, 3, 2))
         .score(atp_players.Rune, (7, 6, 6))),

        (draw.for_round(1).for_match(17)
         .score(atp_players.Medvedev, (7, 6, 6))
         .score(atp_players.Fery, (5, 4, 3))),

        (draw.for_round(1).for_match(18)
         .score(atp_players.Mannarino, (6, 6, 6))
         .score(atp_players.Shevchenko, (3, 3, 2))),

        (draw.for_round(1).for_match(19)
         .score(atp_players.Giron, (7, 6, 6))
         .score(atp_players.Dellien, (6, 4, 4))),

        (draw.for_round(1).for_match(20)
         .score(atp_players.Fucsovics, (6, 6, 6))
         .score(atp_players.Griekspoor, (4, 2, 4))),

        (draw.for_round(1).for_match(21)
         .score(atp_players.Cerundolo_Francisco, (5, 6, 6, 6))
         .score(atp_players.Borges, (7, 3, 3, 4))),

        (draw.for_round(1).for_match(22)
         .score(atp_players.Lehecka, (6, 6, 6))
         .score(atp_players.Ofner, (4, 4, 4))),

        (draw.for_round(1).for_match(23)
         .score(atp_players.Raonic, (6, 6, 7, 6))
         .score(atp_players.Novak, (7, 4, 6, 1))),

        (draw.for_round(1).for_match(24)
         .score(atp_players.Mochizuki, (5, 3, 1))
         .score(atp_players.Paul, (7, 6, 6))),

        (draw.for_round(1).for_match(25)
         .score(atp_players.Norrie, (6, 4, 6, 6))
         .score(atp_players.Machac, (3, 6, 1, 4))),

        (draw.for_round(1).for_match(26)
         .score(atp_players.Eubanks, (4, 7, 7, 6))
         .score(atp_players.Monteiro, (6, 5, 5, 3))),

        (draw.for_round(1).for_match(27)
         .score(atp_players.OConnell, (7, 6, 4, 6))
         .score(atp_players.Medjedovic, (5, 4, 6, 4))),

        (draw.for_round(1).for_match(28)
         .score(atp_players.Vesely, (7, 4, 6, 6))
         .score(atp_players.Korda, (6, 6, 2, 3))),

        (draw.for_round(1).for_match(29)
         .score(atp_players.Shelton, (6, 6, 3, 4, 6))
         .score(atp_players.Daniel, (4, 3, 6, 6, 3))),

        (draw.for_round(1).for_match(30)
         .score(atp_players.Cressy, (7, 6, 6, 6))
         .score(atp_players.Djere, (6, 7, 7, 7))),

        (draw.for_round(1).for_match(31)
         .score(atp_players.Peniston, (3, 0, 1))
         .score(atp_players.Murray_Andy, (6, 6, 6))),

        (draw.for_round(1).for_match(32)
         .score(atp_players.Thiem, (6, 6, 2, 7, 6))
         .score(atp_players.Tsitsipas, (3, 7, 6, 6, 7))),

        (draw.for_round(1).for_match(33)
         .score(atp_players.Sinner, (6, 6, 6))
         .score(atp_players.Cerundolo_Juan, (2, 2, 2))),

        (draw.for_round(1).for_match(34)
         .score(atp_players.Kecmanovic, (0, 3, 4))
         .score(atp_players.Schwartzman, (6, 6, 6))),

        (draw.for_round(1).for_match(35)
         .score(atp_players.Vukic, (6, 7, 3, 7))
         .score(atp_players.Altmaier, (3, 6, 6, 5))),

        (draw.for_round(1).for_match(36)
         .score(atp_players.Halys, (6, 6, 6, 6))
         .score(atp_players.Evans, (2, 3, 7, 4))),

        (draw.for_round(1).for_match(37)
         .score(atp_players.Nishioka, (4, 3, 3))
         .score(atp_players.Galan, (6, 6, 6))),

        (draw.for_round(1).for_match(38)
         .score(atp_players.Koepfer, (5, 3, 6))
         .score(atp_players.Otte, (7, 6, 7))),

        (draw.for_round(1).for_match(39)
         .score(atp_players.Ymer_Mikael, (6, 6, 6))
         .score(atp_players.Molcan, (3, 3, 4))),

        (draw.for_round(1).for_match(40)
         .score(atp_players.Hanfmann, (4, 6, 6, 5, 3))
         .score(atp_players.Fritz, (6, 2, 4, 7, 6))),

        (draw.for_round(1).for_match(41)
         .score(atp_players.Coric, (3, 5, 6, 6, 1))
         .score(atp_players.Pella, (6, 7, 4, 3, 6))),

        (draw.for_round(1).for_match(42)
         .score(atp_players.Bonzi, (3, 4, 5))
         .score(atp_players.Mayot, (6, 6, 7))),

        (draw.for_round(1).for_match(43)
         .score(atp_players.Moutet, (6, 7, 7))
         .score(atp_players.Gasquet, (3, 5, 5))),

        (draw.for_round(1).for_match(44)
         .score(atp_players.Safiullin, (2, 7, 6, 6, 7))
         .score(atp_players.Bautista_Agut, (6, 6, 7, 4, 5))),

        (draw.for_round(1).for_match(45)
         .score(atp_players.Shapovalov, (5, 6, 6, 6))
         .score(atp_players.Albot, (7, 4, 2, 2))),

        (draw.for_round(1).for_match(46)
         .score(atp_players.Harris, (5, 7, 5, 3))
         .score(atp_players.Barrere, (7, 6, 7, 6))),

        (draw.for_round(1).for_match(47)
         .score(atp_players.Broady, (6, 6, 7))
         .score(atp_players.Lestienne, (1, 3, 5))),

        (draw.for_round(1).for_match(48)
         .score(atp_players.Lokoli, (1, 7, 4, 3))
         .score(atp_players.Ruud, (6, 5, 6, 6))),

        (draw.for_round(1).for_match(49)
         .score(atp_players.Rublev, (6, 7, 6))
         .score(atp_players.Purcell, (3, 5, 4))),

        (draw.for_round(1).for_match(50)
         .score(atp_players.Van_Assche, (7, 4, 2, 4))
         .score(atp_players.Karatsev, (6, 6, 6, 6))),

        (draw.for_round(1).for_match(51)
         .score(atp_players.Baez, (6, 6, 3, 6))
         .score(atp_players.Vera, (7, 3, 6, 7))),

        (draw.for_round(1).for_match(52)
         .score(atp_players.Goffin, (6, 5, 6, 6))
         .score(atp_players.Marozsan, (2, 7, 2, 0))),

        (draw.for_round(1).for_match(53)
         .score(atp_players.Bublik, (6, 6, 6, 6))
         .score(atp_players.Mcdonald, (7, 4, 4, 4))),

        (draw.for_round(1).for_match(54)
         .score(atp_players.Wolf, (7, 6, 7))
         .score(atp_players.Couacaud, (5, 3, 6))),

        (draw.for_round(1).for_match(55)
         .score(atp_players.Marterer, (7, 6, 6, 6))
         .score(atp_players.Gojo, (5, 7, 3, 4))),

        (draw.for_round(1).for_match(56)
         .score(atp_players.Mmoh, (7, 6, 7, 6))
         .score(atp_players.Auger_Aliassime, (6, 7, 6, 4))),

        (draw.for_round(1).for_match(57)
         .score(atp_players.Musetti, (6, 6, 7))
         .score(atp_players.Varillas, (3, 1, 5))),

        (draw.for_round(1).for_match(58)
         .score(atp_players.Isner, (6, 3, 4, 4))
         .score(atp_players.Munar, (4, 6, 6, 6))),

        (draw.for_round(1).for_match(59)
         .score(atp_players.Choinski, (5, 7, 6, 6))
         .score(atp_players.Lajovic, (7, 6, 2, 2))),

        (draw.for_round(1).for_match(60)
         .score(atp_players.Ramos_Vinolas, (1, 4, 4))
         .score(atp_players.Hurkacz, (6, 6, 6))),

        (draw.for_round(1).for_match(61)
         .score(atp_players.Etcheverry, (6, 5, 6, 6, 7))
         .score(atp_players.Zapata_Miralles, (7, 7, 3, 4, 5))),

        (draw.for_round(1).for_match(62)
         .score(atp_players.Ruusuvuori, (5, 5, 4))
         .score(atp_players.Wawrinka, (7, 7, 6))),

        (draw.for_round(1).for_match(63)
         .score(atp_players.Thompson, (2, 2, 6, 7, 6))
         .score(atp_players.Nakashima, (6, 6, 4, 6, 3))),

        (draw.for_round(1).for_match(64)
         .score(atp_players.Cachin, (3, 3, 6))
         .score(atp_players.Djokovic, (6, 6, 7))),

    ]


















