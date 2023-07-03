import sys
from tejos.fantasy.teams import *
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women

this = sys.modules[__name__]

TEAM = TeamHeroHangouts


def team_hero_hangouts(mens_singles, womens_singles):
    helpers.selection_fn_caller(this, [mens_singles, womens_singles])
    return TEAM

def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles).match('1.1').winner(women).in_sets()  # (  1) Swiatek  OR  (   ) Zhu
    TEAM.draw(womens_singles).match('1.2').winner(women).in_sets()  # (   ) Trevisan  OR  (   ) Sorribes_Tormo
    TEAM.draw(womens_singles).match('1.3').winner(women).in_sets()  # (   ) Parry  OR  ( WC) Dart
    TEAM.draw(womens_singles).match('1.4').winner(women).in_sets()  # (   ) Fruhvirtova_Linda  OR  ( 30) Martic
    TEAM.draw(womens_singles).match('1.5').winner(women).in_sets()  # ( 23) Linette  OR  (   ) Teichmann
    TEAM.draw(womens_singles).match('1.6').winner(women).in_sets()  # (   ) Strycova  OR  (   ) Zanevska
    TEAM.draw(womens_singles).match('1.7').winner(women).in_sets()  # (   ) Collins  OR  (   ) Grabher
    TEAM.draw(womens_singles).match('1.8').winner(women).in_sets()  # ( WC) Swan  OR  ( 14) Bencic
    TEAM.draw(womens_singles).match('1.9').winner(women).in_sets()  # ( 11) Kasatkina  OR  (   ) Dolehide
    TEAM.draw(womens_singles).match('1.10').winner(women).in_sets()  # ( WC) Burrage  OR  (   ) Mcnally
    TEAM.draw(womens_singles).match('1.11').winner(women).in_sets()  # (   ) Podoroska  OR  (   ) Martincova
    TEAM.draw(womens_singles).match('1.12').winner(women).in_sets()  # (  Q) Yuan  OR  ( 19) Azarenka
    TEAM.draw(womens_singles).match('1.13').winner(women).in_sets()  # ( 28) Mertens  OR  (  Q) Hruncakova
    TEAM.draw(womens_singles).match('1.14').winner(women).in_sets()  # ( WC) Williams  OR  ( WC) Svitolina
    TEAM.draw(womens_singles).match('1.15').winner(women).in_sets()  # (  Q) Hunter  OR  (   ) Wang_Xinyu
    TEAM.draw(womens_singles).match('1.16').winner(women).in_sets()  # (  Q) Kenin  OR  (  7) Gauff
    TEAM.draw(womens_singles).match('1.17').winner(women).in_sets()  # (  4) Pegula  OR  (   ) Davis
    TEAM.draw(womens_singles).match('1.18').winner(women).in_sets()  # (   ) Bucsa  OR  (   ) Rakhimova
    TEAM.draw(womens_singles).match('1.19').winner(women).in_sets()  # (   ) Osorio  OR  (   ) Cocciaretto
    TEAM.draw(womens_singles).match('1.20').winner(women).in_sets()  # (   ) Masarova  OR  ( 31) Sherif
    TEAM.draw(womens_singles).match('1.21').winner(women).in_sets()  # ( 24) Zheng  OR  (   ) Siniakova
    TEAM.draw(womens_singles).match('1.22').winner(women).in_sets()  # (   ) Tsurenko  OR  (   ) Liu
    TEAM.draw(womens_singles).match('1.23').winner(women).in_sets()  # (   ) Parks  OR  (   ) Friedsam
    TEAM.draw(womens_singles).match('1.24').winner(women).in_sets()  # (   ) Bogdan  OR  ( 15) Samsonova
    TEAM.draw(womens_singles).match('1.25').winner(women).in_sets()  # ( 12) Kudermetova_Veronika  OR  (   ) Kanepi
    TEAM.draw(womens_singles).match('1.26').winner(women).in_sets()  # (   ) Vondrousova  OR  (   ) Stearns
    TEAM.draw(womens_singles).match('1.27').winner(women).in_sets()  # (   ) Stephens  OR  (   ) Peterson
    TEAM.draw(womens_singles).match('1.28').winner(women).in_sets()  # (   ) Zhang_Shuai  OR  ( 20) Vekic
    TEAM.draw(womens_singles).match('1.29').winner(women).in_sets()  # ( 32) Bouzkova  OR  (  Q) Waltert
    TEAM.draw(womens_singles).match('1.30').winner(women).in_sets()  # (   ) Kontaveit  OR  (  Q) Stefanini
    TEAM.draw(womens_singles).match('1.31').winner(women).in_sets()  # (   ) Baindl  OR  (   ) Fernandez
    TEAM.draw(womens_singles).match('1.32').winner(women).in_sets()  # (   ) Volynets  OR  (  5) Garcia
    TEAM.draw(womens_singles).match('1.33').winner(women).in_sets()  # (  6) Jabeur  OR  (   ) Frech
    TEAM.draw(womens_singles).match('1.34').winner(women).in_sets()  # (   ) Bonaventure  OR  (  Q) Bai
    TEAM.draw(womens_singles).match('1.35').winner(women).in_sets()  # (   ) Bondar  OR  (   ) Andreescu
    TEAM.draw(womens_singles).match('1.36').winner(women).in_sets()  # (  Q) Maneiro  OR  ( 26) Kalinina
    TEAM.draw(womens_singles).match('1.37').winner(women).in_sets()  # ( 18) Pliskova  OR  (  Q) Stevanovic
    TEAM.draw(womens_singles).match('1.38').winner(women).in_sets()  # (  Q) Zhao  OR  ( LL) Korpatsch
    TEAM.draw(womens_singles).match('1.39').winner(women).in_sets()  # (   ) Sasnovich  OR  (   ) Parrizas_Diaz
    TEAM.draw(womens_singles).match('1.40').winner(women).in_sets()  # (   ) Paolini  OR  (  9) Kvitova
    TEAM.draw(womens_singles).match('1.41').winner(women).in_sets()  # ( 13) Haddad_Maia  OR  (   ) Putintseva
    TEAM.draw(womens_singles).match('1.42').winner(women).in_sets()  # (   ) Cristian  OR  (   ) Bronzetti
    TEAM.draw(womens_singles).match('1.43').winner(women).in_sets()  # (   ) Cirstea  OR  (   ) Maria
    TEAM.draw(womens_singles).match('1.44').winner(women).in_sets()  # (  Q) Minnen  OR  ( 17) Ostapenko
    TEAM.draw(womens_singles).match('1.45').winner(women).in_sets()  # ( 27) Pera  OR  (   ) Tomova
    TEAM.draw(womens_singles).match('1.46').winner(women).in_sets()  # ( WC) Boulter  OR  (   ) Saville
    TEAM.draw(womens_singles).match('1.47').winner(women).in_sets()  # ( LL) Hibino  OR  (   ) Cornet
    TEAM.draw(womens_singles).match('1.48').winner(women).in_sets()  # (   ) Rogers  OR  (  3) Rybakina
    TEAM.draw(womens_singles).match('1.49').winner(women).in_sets()  # (  8) Sakkari  OR  (   ) Kostyuk
    TEAM.draw(womens_singles).match('1.50').winner(women).in_sets()  # (   ) Riske_Amritraj  OR  (   ) Badosa
    TEAM.draw(womens_singles).match('1.51').winner(women).in_sets()  # (  Q) Golubic  OR  (   ) Schmiedlova
    TEAM.draw(womens_singles).match('1.52').winner(women).in_sets()  # ( WC) Kartal  OR  ( 25) Keys
    TEAM.draw(womens_singles).match('1.53').winner(women).in_sets()  # ( 22) Potapova  OR  (  Q) Naef
    TEAM.draw(womens_singles).match('1.54').winner(women).in_sets()  # (  Q) Juvan  OR  (   ) Betova
    TEAM.draw(womens_singles).match('1.55').winner(women).in_sets()  # (  Q) Andreeva_Mirra  OR  (   ) Wang_Xiyu
    TEAM.draw(womens_singles).match('1.56').winner(women).in_sets()  # ( WC) Watson  OR  ( 10) Krejcikova
    TEAM.draw(womens_singles).match('1.57').winner(women).in_sets()  # ( 16) Muchova  OR  (   ) Niemeier
    TEAM.draw(womens_singles).match('1.58').winner(women).in_sets()  # (   ) Noskova  OR  (   ) Galfi
    TEAM.draw(womens_singles).match('1.59').winner(women).in_sets()  # (   ) Brengle  OR  (   ) Errani
    TEAM.draw(womens_singles).match('1.60').winner(women).in_sets()  # (   ) Navarro  OR  ( 21) Alexandrova
    TEAM.draw(womens_singles).match('1.61').winner(women).in_sets()  # ( 29) Begu  OR  (   ) Marino
    TEAM.draw(womens_singles).match('1.62').winner(women).in_sets()  # (  Q) Wickmayer  OR  (   ) Blinkova
    TEAM.draw(womens_singles).match('1.63').winner(women).in_sets()  # (   ) Gracheva  OR  (   ) Giorgi
    TEAM.draw(womens_singles).match('1.64').winner(women).in_sets()  # (   ) Udvardy  OR  (  2) Sabalenka


def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles).match('1.1').winner(men).in_sets()  # (  1) Alcaraz  OR  (   ) Chardy
    TEAM.draw(mens_singles).match('1.2').winner(men).in_sets()  # (   ) Muller  OR  (   ) Rinderknech
    TEAM.draw(mens_singles).match('1.3').winner(men).in_sets()  # (   ) Kubler  OR  (   ) Humbert
    TEAM.draw(mens_singles).match('1.4').winner(men).in_sets()  # (   ) Cecchinato  OR  ( 25) Jarry
    TEAM.draw(mens_singles).match('1.5').winner(men).in_sets()  # ( 19) Zverev  OR  (  Q) Brouwer
    TEAM.draw(mens_singles).match('1.6').winner(men).in_sets()  # (   ) Huesler  OR  ( LL) Watanuki
    TEAM.draw(mens_singles).match('1.7').winner(men).in_sets()  # (   ) Berrettini  OR  (   ) Sonego
    TEAM.draw(mens_singles).match('1.8').winner(men).in_sets()  # (  Q) Coppejans  OR  ( 15) De_Minaur
    TEAM.draw(mens_singles).match('1.9').winner(men).in_sets()  # ( 10) Tiafoe  OR  (   ) Wu
    TEAM.draw(mens_singles).match('1.10').winner(men).in_sets()  # (  Q) Stricker  OR  (   ) Popyrin
    TEAM.draw(mens_singles).match('1.11').winner(men).in_sets()  # (   ) Ivashka  OR  (   ) Coria
    TEAM.draw(mens_singles).match('1.12').winner(men).in_sets()  # (  Q) Shimabukuro  OR  ( 21) Dimitrov
    TEAM.draw(mens_singles).match('1.13').winner(men).in_sets()  # ( 31) Davidovich_Fokina  OR  ( WC) Fils
    TEAM.draw(mens_singles).match('1.14').winner(men).in_sets()  # (   ) Zhang_Zhizhen  OR  (   ) Van_De_Zandschulp
    TEAM.draw(mens_singles).match('1.15').winner(men).in_sets()  # (  Q) Arnaldi  OR  (   ) Carballes_Baena
    TEAM.draw(mens_singles).match('1.16').winner(men).in_sets()  # ( WC) Loffhagen  OR  (  6) Rune
    TEAM.draw(mens_singles).match('1.17').winner(men).in_sets()  # (  3) Medvedev  OR  ( WC) Fery
    TEAM.draw(mens_singles).match('1.18').winner(men).in_sets()  # (   ) Mannarino  OR  (   ) Shevchenko
    TEAM.draw(mens_singles).match('1.19').winner(men).in_sets()  # (   ) Giron  OR  (   ) Dellien
    TEAM.draw(mens_singles).match('1.20').winner(men).in_sets()  # (   ) Fucsovics  OR  ( 28) Griekspoor
    TEAM.draw(mens_singles).match('1.21').winner(men).in_sets()  # ( 18) Cerundolo_Francisco  OR  (   ) Borges
    TEAM.draw(mens_singles).match('1.22').winner(men).in_sets()  # (   ) Lehecka  OR  ( WC) Ofner
    TEAM.draw(mens_singles).match('1.23').winner(men).in_sets()  # (   ) Raonic  OR  (  Q) Novak
    TEAM.draw(mens_singles).match('1.24').winner(men).in_sets()  # (  Q) Mochizuki  OR  ( 16) Paul
    TEAM.draw(mens_singles).match('1.25').winner(men).in_sets()  # ( 12) Norrie  OR  (  Q) Machac
    TEAM.draw(mens_singles).match('1.26').winner(men).in_sets()  # (   ) Eubanks  OR  (   ) Monteiro
    TEAM.draw(mens_singles).match('1.27').winner(men).in_sets()  # (   ) OConnell  OR  (  Q) Medjedovic
    TEAM.draw(mens_singles).match('1.28').winner(men).in_sets()  # (   ) Vesely  OR  ( 22) Korda
    TEAM.draw(mens_singles).match('1.29').winner(men).in_sets()  # ( 32) Shelton  OR  ( LL) Daniel
    TEAM.draw(mens_singles).match('1.30').winner(men).in_sets()  # (   ) Cressy  OR  (   ) Djere
    TEAM.draw(mens_singles).match('1.31').winner(men).in_sets()  # ( WC) Peniston  OR  (   ) Murray_Andy
    TEAM.draw(mens_singles).match('1.32').winner(men).in_sets()  # (   ) Thiem  OR  (  5) Tsitsipas
    TEAM.draw(mens_singles).match('1.33').winner(men).in_sets()  # (  8) Sinner  OR  (   ) Cerundolo_Juan
    TEAM.draw(mens_singles).match('1.34').winner(men).in_sets()  # (   ) Kecmanovic  OR  (   ) Schwartzman
    TEAM.draw(mens_singles).match('1.35').winner(men).in_sets()  # (   ) Vukic  OR  (   ) Altmaier
    TEAM.draw(mens_singles).match('1.36').winner(men).in_sets()  # (   ) Halys  OR  ( 27) Evans
    TEAM.draw(mens_singles).match('1.37').winner(men).in_sets()  # ( 24) Nishioka  OR  (   ) Galan
    TEAM.draw(mens_singles).match('1.38').winner(men).in_sets()  # (   ) Koepfer  OR  (  Q) Otte
    TEAM.draw(mens_singles).match('1.39').winner(men).in_sets()  # (   ) Ymer_Mikael  OR  (   ) Molcan
    TEAM.draw(mens_singles).match('1.40').winner(men).in_sets()  # (   ) Hanfmann  OR  (  9) Fritz
    TEAM.draw(mens_singles).match('1.41').winner(men).in_sets()  # ( 13) Coric  OR  (   ) Pella
    TEAM.draw(mens_singles).match('1.42').winner(men).in_sets()  # (   ) Bonzi  OR  (  Q) Mayot
    TEAM.draw(mens_singles).match('1.43').winner(men).in_sets()  # (   ) Moutet  OR  (   ) Gasquet
    TEAM.draw(mens_singles).match('1.44').winner(men).in_sets()  # (   ) Safiullin  OR  ( 20) Bautista_Agut
    TEAM.draw(mens_singles).match('1.45').winner(men).in_sets()  # ( 26) Shapovalov  OR  (  Q) Albot
    TEAM.draw(mens_singles).match('1.46').winner(men).in_sets()  # (   ) Harris  OR  (   ) Barrere
    TEAM.draw(mens_singles).match('1.47').winner(men).in_sets()  # ( WC) Broady  OR  (   ) Lestienne
    TEAM.draw(mens_singles).match('1.48').winner(men).in_sets()  # (  Q) Lokoli  OR  (  4) Ruud
    TEAM.draw(mens_singles).match('1.49').winner(men).in_sets()  # (  7) Rublev  OR  (   ) Purcell
    TEAM.draw(mens_singles).match('1.50').winner(men).in_sets()  # (   ) Van_Assche  OR  (   ) Karatsev
    TEAM.draw(mens_singles).match('1.51').winner(men).in_sets()  # (   ) Baez  OR  (  Q) Vera
    TEAM.draw(mens_singles).match('1.52').winner(men).in_sets()  # ( WC) Goffin  OR  ( 30) Kyrgios
    TEAM.draw(mens_singles).match('1.53').winner(men).in_sets()  # ( 23) Bublik  OR  (   ) Mcdonald
    TEAM.draw(mens_singles).match('1.54').winner(men).in_sets()  # (   ) Wolf  OR  (  Q) Couacaud
    TEAM.draw(mens_singles).match('1.55').winner(men).in_sets()  # (  Q) Marterer  OR  (   ) Gojo
    TEAM.draw(mens_singles).match('1.56').winner(men).in_sets()  # (   ) Krajinovic  OR  ( 11) Auger_Aliassime
    TEAM.draw(mens_singles).match('1.57').winner(men).in_sets()  # ( 14) Musetti  OR  (   ) Varillas
    TEAM.draw(mens_singles).match('1.58').winner(men).in_sets()  # (   ) Isner  OR  (   ) Munar
    TEAM.draw(mens_singles).match('1.59').winner(men).in_sets()  # ( WC) Choinski  OR  (   ) Lajovic
    TEAM.draw(mens_singles).match('1.60').winner(men).in_sets()  # (   ) Ramos_Vinolas  OR  ( 17) Hurkacz
    TEAM.draw(mens_singles).match('1.61').winner(men).in_sets()  # ( 29) Etcheverry  OR  (   ) Zapata_Miralles
    TEAM.draw(mens_singles).match('1.62').winner(men).in_sets()  # (   ) Ruusuvuori  OR  (   ) Wawrinka
    TEAM.draw(mens_singles).match('1.63').winner(men).in_sets()  # (   ) Thompson  OR  (   ) Nakashima
    TEAM.draw(mens_singles).match('1.64').winner(men).in_sets()  # (   ) Cachin  OR  (  2) Djokovic