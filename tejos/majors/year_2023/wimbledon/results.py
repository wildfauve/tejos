from tejos.players import wta_players, atp_players


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
         .score(wta_players.Martic, (7, 6, 4))),

        (draw.for_round(1).for_match(5)
         .score(wta_players.Linette, (6, 6))
         .score(wta_players.Teichmann, (3, 2))),

        (draw.for_round(1).for_match(6)
         .score(wta_players.Strycova, (6, 7))
         .score(wta_players.Zanevska, (1, 5))),

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

        (draw.for_round(1).for_match(29)
         .score(wta_players.Bouzkova, (6, 6))
         .score(wta_players.Waltert, (1, 4))),

        (draw.for_round(1).for_match(31)
         .score(wta_players.Baindl, (4, 6, 4))
         .score(wta_players.Fernandez, (6, 4, 6))),

        (draw.for_round(1).for_match(32)
         .score(wta_players.Volynets, (4, 3))
         .score(wta_players.Garcia, (6, 6))),

    ]


def mens_singles_results_r1(draw):
    return [
        (draw.for_round(1).for_match(34)
         .score(atp_players.Kecmanovic, (0, 3, 4))
         .score(atp_players.Schwartzman, (6, 6, 6))),

        (draw.for_round(1).for_match(35)
         .score(atp_players.Vukic, (6, 7, 3, 7))
         .score(atp_players.Altmaier, (3, 6, 6, 5))),

        (draw.for_round(1).for_match(37)
         .score(atp_players.Nishioka, (4, 3, 3))
         .score(atp_players.Galan, (6, 6, 6))),

        (draw.for_round(1).for_match(38)
         .score(atp_players.Koepfer, (5, 3, 6))
         .score(atp_players.Otte, (7, 6, 7))),

        (draw.for_round(1).for_match(39)
         .score(atp_players.Ymer_Mikael, (6, 6, 6))
         .score(atp_players.Molcan, (3, 3, 4))),

        (draw.for_round(1).for_match(43)
         .score(atp_players.Moutet, (6, 7, 7))
         .score(atp_players.Gasquet, (3, 5, 5))),

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
