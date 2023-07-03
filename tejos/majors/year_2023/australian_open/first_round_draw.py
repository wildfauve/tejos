from tejos.players import atp_players, wta_players


def mens_draw_round_1():
    return [(1, atp_players.Nishioka, atp_players.Khachanov),
            (2, atp_players.Hurkacz, atp_players.Korda),
            (3, atp_players.Tsitsipas, atp_players.Sinner),
            (4, atp_players.Lehecka, atp_players.Auger_Aliassime),
            (5, atp_players.Rublev, atp_players.Rune),
            (6, atp_players.De_Minaur, atp_players.Djokovic),
            (7, atp_players.Shelton, atp_players.Wolf),
            (8, atp_players.Bautista_Agut, atp_players.Paul)]


def womens_draw_round_1():
    return [(1, wta_players.Swiatek, wta_players.Rybakina),
            (2, wta_players.Ostapenko, wta_players.Gauff),
            (3, wta_players.Pegula, wta_players.Krejcikova),
            (4, wta_players.Azarenka, wta_players.Zhu),
            (5, wta_players.Pliskova, wta_players.Zhang_Shuai),
            (6, wta_players.Linette, wta_players.Garcia),
            (7, wta_players.Sabalenka, wta_players.Bencic),
            (8, wta_players.Vekic, wta_players.Fruhvirtova_Linda)]
