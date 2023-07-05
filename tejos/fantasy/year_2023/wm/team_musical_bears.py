import sys

from tejos.fantasy.teams import *
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women

this = sys.modules[__name__]

TEAM = TeamMusicalBears


def team_musical_bears(mens_singles, womens_singles):
    helpers.selection_fn_caller(this, [mens_singles, womens_singles])
    return TEAM

def womens_singles_round_2(womens_singles):
    TEAM.draw(womens_singles).match('2.1').winner(women.Swiatek).in_sets(2)  # (  1) Swiatek  OR  (   ) Sorribes_Tormo
    TEAM.draw(womens_singles).match('2.2').winner(women.Martic).in_sets(3)  # (   ) Parry  OR  ( 30) Martic
    TEAM.draw(womens_singles).match('2.3').winner(women.Linette).in_sets(2)  # ( 23) Linette  OR  (   ) Strycova
    TEAM.draw(womens_singles).match('2.4').winner(women).in_sets()  # ( 14) Bencic  OR  TBD
    TEAM.draw(womens_singles).match('2.5').winner(women.Kasatkina).in_sets(3)  # ( 11) Kasatkina  OR  ( WC) Burrage
    TEAM.draw(womens_singles).match('2.6').winner(women.Azarenka).in_sets(2)  # (   ) Podoroska  OR  ( 19) Azarenka
    TEAM.draw(womens_singles).match('2.7').winner(women.Mertens).in_sets(3)  # ( 28) Mertens  OR  ( WC) Svitolina
    TEAM.draw(womens_singles).match('2.8').winner(women.Wang_Xinyu).in_sets(3)  # (   ) Wang_Xinyu  OR  (  Q) Kenin
    TEAM.draw(womens_singles).match('2.9').winner(women.Pegula).in_sets(2)  # (  4) Pegula  OR  (   ) Bucsa
    TEAM.draw(womens_singles).match('2.10').winner(women).in_sets()  # (   ) Masarova  OR  TBD
    TEAM.draw(womens_singles).match('2.11').winner(women.Siniakova).in_sets(3)  # (   ) Siniakova  OR  (   ) Tsurenko
    TEAM.draw(womens_singles).match('2.12').winner(women.Parks).in_sets(2)  # (   ) Parks  OR  (   ) Bogdan
    TEAM.draw(womens_singles).match('2.13').winner(women.Kudermetova_Veronika).in_sets(2)  # ( 12) Kudermetova_Veronika  OR  (   ) Vondrousova
    TEAM.draw(womens_singles).match('2.14').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.15').winner(women).in_sets()  # ( 32) Bouzkova  OR  TBD
    TEAM.draw(womens_singles).match('2.16').winner(women.Garcia).in_sets(2)  # (   ) Fernandez  OR  (  5) Garcia
    TEAM.draw(womens_singles).match('2.17').winner(women).in_sets()  # (  6) Jabeur  OR  TBD
    TEAM.draw(womens_singles).match('2.18').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.19').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.20').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.21').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.22').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.23').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.24').winner(women).in_sets()  # (  3) Rybakina  OR  TBD
    TEAM.draw(womens_singles).match('2.25').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.26').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.27').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.28').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.29').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.30').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.31').winner(women).in_sets()  # TBD  OR  TBD
    TEAM.draw(womens_singles).match('2.32').winner(women).in_sets()  # (  2) Sabalenka  OR  TBD



def mens_singles_round_2(mens_singles):
    TEAM.draw(mens_singles).match('2.1').winner(men).in_sets()  # (  1) Alcaraz  OR  TBD
    TEAM.draw(mens_singles).match('2.2').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.3').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.4').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.5').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.6').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.7').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.8').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.9').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.10').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.11').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.12').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.13').winner(men).in_sets()  # ( 12) Norrie  OR  TBD
    TEAM.draw(mens_singles).match('2.14').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.15').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.16').winner(men).in_sets()  # (   ) Murray_Andy  OR  TBD
    TEAM.draw(mens_singles).match('2.17').winner(men.Sinner).in_sets(3)  # (  8) Sinner  OR  (   ) Schwartzman
    TEAM.draw(mens_singles).match('2.18').winner(men.Halys).in_sets(4)  # (   ) Vukic  OR  (   ) Halys
    TEAM.draw(mens_singles).match('2.19').winner(men.Galan).in_sets(3)  # (   ) Galan  OR  (  Q) Otte
    TEAM.draw(mens_singles).match('2.20').winner(men).in_sets()  # (   ) Ymer_Mikael  OR  TBD
    TEAM.draw(mens_singles).match('2.21').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.22').winner(men).in_sets()  # (   ) Moutet  OR  TBD
    TEAM.draw(mens_singles).match('2.23').winner(men).in_sets()  # TBD  OR  TBD
    TEAM.draw(mens_singles).match('2.24').winner(men.Ruud).in_sets(3)  # ( WC) Broady  OR  (  4) Ruud
    TEAM.draw(mens_singles).match('2.25').winner(men.Rublev).in_sets(4)  # (  7) Rublev  OR  (   ) Karatsev
    TEAM.draw(mens_singles).match('2.26').winner(men.Goffin).in_sets(4)  # (  Q) Vera  OR  ( WC) Goffin
    TEAM.draw(mens_singles).match('2.27').winner(men.Bublik).in_sets(3)  # ( 23) Bublik  OR  (   ) Wolf
    TEAM.draw(mens_singles).match('2.28').winner(men.Mmoh).in_sets(4)  # (  Q) Marterer  OR  (   ) Mmoh
    TEAM.draw(mens_singles).match('2.29').winner(men.Musetti).in_sets(4)  # ( 14) Musetti  OR  (   ) Munar
    TEAM.draw(mens_singles).match('2.30').winner(men.Hurkacz).in_sets(4)  # ( WC) Choinski  OR  ( 17) Hurkacz
    TEAM.draw(mens_singles).match('2.31').winner(men.Wawrinka).in_sets(4)  # ( 29) Etcheverry  OR  (   ) Wawrinka
    TEAM.draw(mens_singles).match('2.32').winner(men.Djokovic).in_sets(3)  # (   ) Thompson  OR  (  2) Djokovic


def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles).match('1.1').winner(women.Swiatek).in_sets(2)  # (  1) Swiatek  OR  (   ) Zhu
    TEAM.draw(womens_singles).match('1.2').winner(women.Trevisan).in_sets(2)  # (   ) Trevisan  OR  (   ) Sorribes_Tormo
    TEAM.draw(womens_singles).match('1.3').winner(women.Parry).in_sets(3)  # (   ) Parry  OR  ( WC) Dart
    TEAM.draw(womens_singles).match('1.4').winner(women.Fruhvirtova_Linda).in_sets(3)  # (   ) Fruhvirtova_Linda  OR  ( 30) Martic
    TEAM.draw(womens_singles).match('1.5').winner(women.Linette).in_sets(2)  # ( 23) Linette  OR  (   ) Teichmann
    TEAM.draw(womens_singles).match('1.6').winner(women.Strycova).in_sets(2)  # (   ) Strycova  OR  (   ) Zanevska
    TEAM.draw(womens_singles).match('1.7').winner(women.Collins).in_sets(3)  # (   ) Collins  OR  (   ) Grabher
    TEAM.draw(womens_singles).match('1.8').winner(women.Bencic).in_sets(2)  # ( WC) Swan  OR  ( 14) Bencic
    TEAM.draw(womens_singles).match('1.9').winner(women.Kasatkina).in_sets(2)  # ( 11) Kasatkina  OR  (   ) Dolehide
    TEAM.draw(womens_singles).match('1.10').winner(women.Mcnally).in_sets(2)  # ( WC) Burrage  OR  (   ) Mcnally
    TEAM.draw(womens_singles).match('1.11').winner(women.Martincova).in_sets(2)  # (   ) Podoroska  OR  (   ) Martincova
    TEAM.draw(womens_singles).match('1.12').winner(women.Yuan).in_sets(3)  # (  Q) Yuan  OR  ( 19) Azarenka
    TEAM.draw(womens_singles).match('1.13').winner(women.Mertens).in_sets(2)  # ( 28) Mertens  OR  (  Q) Hruncakova
    TEAM.draw(womens_singles).match('1.14').winner(women.Williams).in_sets(2)  # ( WC) Williams  OR  ( WC) Svitolina
    TEAM.draw(womens_singles).match('1.15').winner(women.Wang_Xinyu).in_sets(3)  # (  Q) Hunter  OR  (   ) Wang_Xinyu
    TEAM.draw(womens_singles).match('1.16').winner(women.Gauff).in_sets(2)  # (  Q) Kenin  OR  (  7) Gauff
    TEAM.draw(womens_singles).match('1.17').winner(women.Pegula).in_sets(2)  # (  4) Pegula  OR  (   ) Davis
    TEAM.draw(womens_singles).match('1.18').winner(women.Bucsa).in_sets(3)  # (   ) Bucsa  OR  (   ) Rakhimova
    TEAM.draw(womens_singles).match('1.19').winner(women.Cocciaretto).in_sets(2)  # (   ) Osorio  OR  (   ) Cocciaretto
    TEAM.draw(womens_singles).match('1.20').winner(women.Sherif).in_sets(2)  # (   ) Masarova  OR  ( 31) Sherif
    TEAM.draw(womens_singles).match('1.21').winner(women.Zheng).in_sets(2)  # ( 24) Zheng  OR  (   ) Siniakova
    TEAM.draw(womens_singles).match('1.22').winner(women.Liu).in_sets(3)  # (   ) Tsurenko  OR  (   ) Liu
    TEAM.draw(womens_singles).match('1.23').winner(women.Friedsam).in_sets(2)  # (   ) Parks  OR  (   ) Friedsam
    TEAM.draw(womens_singles).match('1.24').winner(women.Samsonova).in_sets(2)  # (   ) Bogdan  OR  ( 15) Samsonova
    TEAM.draw(womens_singles).match('1.25').winner(women.Kudermetova_Veronika).in_sets(3)  # ( 12) Kudermetova_Veronika  OR  (   ) Kanepi
    TEAM.draw(womens_singles).match('1.26').winner(women.Vondrousova).in_sets(2)  # (   ) Vondrousova  OR  (   ) Stearns
    TEAM.draw(womens_singles).match('1.27').winner(women.Peterson).in_sets(3)  # (   ) Stephens  OR  (   ) Peterson
    TEAM.draw(womens_singles).match('1.28').winner(women.Vekic).in_sets(2)  # (   ) Zhang_Shuai  OR  ( 20) Vekic
    TEAM.draw(womens_singles).match('1.29').winner(women.Bouzkova).in_sets(2)  # ( 32) Bouzkova  OR  (  Q) Waltert
    TEAM.draw(womens_singles).match('1.30').winner(women.Kontaveit).in_sets(2)  # (   ) Kontaveit  OR  (  Q) Stefanini
    TEAM.draw(womens_singles).match('1.31').winner(women.Baindl).in_sets(3)  # (   ) Baindl  OR  (   ) Fernandez
    TEAM.draw(womens_singles).match('1.32').winner(women.Garcia).in_sets(2)  # (   ) Volynets  OR  (  5) Garcia
    TEAM.draw(womens_singles).match('1.33').winner(women.Jabeur).in_sets(2)  # (  6) Jabeur  OR  (   ) Frech
    TEAM.draw(womens_singles).match('1.34').winner(women.Bonaventure).in_sets(2)  # (   ) Bonaventure  OR  (  Q) Bai
    TEAM.draw(womens_singles).match('1.35').winner(women.Andreescu).in_sets(2)  # (   ) Bondar  OR  (   ) Andreescu
    TEAM.draw(womens_singles).match('1.36').winner(women.Kalinina).in_sets(2)  # (  Q) Maneiro  OR  ( 26) Kalinina
    TEAM.draw(womens_singles).match('1.37').winner(women.Pliskova).in_sets(2)  # ( 18) Pliskova  OR  (  Q) Stevanovic
    TEAM.draw(womens_singles).match('1.38').winner(women.Zhao).in_sets(2)  # (  Q) Zhao  OR  ( LL) Korpatsch
    TEAM.draw(womens_singles).match('1.39').winner(women.Parrizas_Diaz).in_sets(3)  # (   ) Sasnovich  OR  (   ) Parrizas_Diaz
    TEAM.draw(womens_singles).match('1.40').winner(women.Kvitova).in_sets(2)  # (   ) Paolini  OR  (  9) Kvitova
    TEAM.draw(womens_singles).match('1.41').winner(women.Haddad_Maia).in_sets(2)  # ( 13) Haddad_Maia  OR  (   ) Putintseva
    TEAM.draw(womens_singles).match('1.42').winner(women.Bronzetti).in_sets(3)  # (   ) Cristian  OR  (   ) Bronzetti
    TEAM.draw(womens_singles).match('1.43').winner(women.Cirstea).in_sets(3)  # (   ) Cirstea  OR  (   ) Maria
    TEAM.draw(womens_singles).match('1.44').winner(women.Ostapenko).in_sets(2)  # (  Q) Minnen  OR  ( 17) Ostapenko
    TEAM.draw(womens_singles).match('1.45').winner(women.Pera).in_sets(2)  # ( 27) Pera  OR  (   ) Tomova
    TEAM.draw(womens_singles).match('1.46').winner(women.Saville).in_sets(2)  # ( WC) Boulter  OR  (   ) Saville
    TEAM.draw(womens_singles).match('1.47').winner(women.Cornet).in_sets(3)  # ( LL) Hibino  OR  (   ) Cornet
    TEAM.draw(womens_singles).match('1.48').winner(women.Rybakina).in_sets(2)  # (   ) Rogers  OR  (  3) Rybakina
    TEAM.draw(womens_singles).match('1.49').winner(women.Sakkari).in_sets(2)  # (  8) Sakkari  OR  (   ) Kostyuk
    TEAM.draw(womens_singles).match('1.50').winner(women.Riske_Amritraj).in_sets(3)  # (   ) Riske_Amritraj  OR  (   ) Badosa
    TEAM.draw(womens_singles).match('1.51').winner(women.Schmiedlova).in_sets(2)  # (  Q) Golubic  OR  (   ) Schmiedlova
    TEAM.draw(womens_singles).match('1.52').winner(women.Keys).in_sets(2)  # ( WC) Kartal  OR  ( 25) Keys
    TEAM.draw(womens_singles).match('1.53').winner(women.Potapova).in_sets(2)  # ( 22) Potapova  OR  (  Q) Naef
    TEAM.draw(womens_singles).match('1.54').winner(women.Betova).in_sets(2)  # (  Q) Juvan  OR  (   ) Betova
    TEAM.draw(womens_singles).match('1.55').winner(women.Wang_Xiyu).in_sets(2)  # (  Q) Andreeva_Mirra  OR  (   ) Wang_Xiyu
    TEAM.draw(womens_singles).match('1.56').winner(women.Krejcikova).in_sets(2)  # ( WC) Watson  OR  ( 10) Krejcikova
    TEAM.draw(womens_singles).match('1.57').winner(women.Muchova).in_sets(2)  # ( 16) Muchova  OR  (   ) Niemeier
    TEAM.draw(womens_singles).match('1.58').winner(women.Noskova).in_sets(3)  # (   ) Noskova  OR  (   ) Galfi
    TEAM.draw(womens_singles).match('1.59').winner(women.Errani).in_sets(2)  # (   ) Brengle  OR  (   ) Errani
    TEAM.draw(womens_singles).match('1.60').winner(women.Alexandrova).in_sets(2)  # (   ) Navarro  OR  ( 21) Alexandrova
    TEAM.draw(womens_singles).match('1.61').winner(women.Begu).in_sets(3)  # ( 29) Begu  OR  (   ) Marino
    TEAM.draw(womens_singles).match('1.62').winner(women.Blinkova).in_sets(2)  # (  Q) Wickmayer  OR  (   ) Blinkova
    TEAM.draw(womens_singles).match('1.63').winner(women.Giorgi).in_sets(3)  # (   ) Gracheva  OR  (   ) Giorgi
    TEAM.draw(womens_singles).match('1.64').winner(women.Sabalenka).in_sets(2)  # (   ) Udvardy  OR  (  2) Sabalenka



def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles).match('1.1').winner(men.Alcaraz).in_sets(3)  # (  1) Alcaraz  OR  (   ) Chardy
    TEAM.draw(mens_singles).match('1.2').winner(men.Rinderknech).in_sets(4)  # (   ) Muller  OR  (   ) Rinderknech
    TEAM.draw(mens_singles).match('1.3').winner(men.Kubler).in_sets(5)  # (   ) Kubler  OR  (   ) Humbert
    TEAM.draw(mens_singles).match('1.4').winner(men.Jarry).in_sets(4)  # (   ) Cecchinato  OR  ( 25) Jarry
    TEAM.draw(mens_singles).match('1.5').winner(men.Zverev).in_sets(3)  # ( 19) Zverev  OR  (  Q) Brouwer
    TEAM.draw(mens_singles).match('1.6').winner(men.Huesler).in_sets(3)  # (   ) Huesler  OR  ( LL) Watanuki
    TEAM.draw(mens_singles).match('1.7').winner(men.Sonego).in_sets(4)  # (   ) Berrettini  OR  (   ) Sonego
    TEAM.draw(mens_singles).match('1.8').winner(men.De_Minaur).in_sets(3)  # (  Q) Coppejans  OR  ( 15) De_Minaur
    TEAM.draw(mens_singles).match('1.9').winner(men.Tiafoe).in_sets(3)  # ( 10) Tiafoe  OR  (   ) Wu
    TEAM.draw(mens_singles).match('1.10').winner(men.Popyrin).in_sets(4)  # (  Q) Stricker  OR  (   ) Popyrin
    TEAM.draw(mens_singles).match('1.11').winner(men.Ivashka).in_sets(4)  # (   ) Ivashka  OR  (   ) Coria
    TEAM.draw(mens_singles).match('1.12').winner(men.Dimitrov).in_sets(3)  # (  Q) Shimabukuro  OR  ( 21) Dimitrov
    TEAM.draw(mens_singles).match('1.13').winner(men.Davidovich_Fokina).in_sets(3)  # ( 31) Davidovich_Fokina  OR  ( WC) Fils
    TEAM.draw(mens_singles).match('1.14').winner(men.Zhang_Zhizhen).in_sets(4)  # (   ) Zhang_Zhizhen  OR  (   ) Van_De_Zandschulp
    TEAM.draw(mens_singles).match('1.15').winner(men.Carballes_Baena).in_sets(3)  # (  Q) Arnaldi  OR  (   ) Carballes_Baena
    TEAM.draw(mens_singles).match('1.16').winner(men.Rune).in_sets(3)  # ( WC) Loffhagen  OR  (  6) Rune
    TEAM.draw(mens_singles).match('1.17').winner(men.Medvedev).in_sets(3)  # (  3) Medvedev  OR  ( WC) Fery
    TEAM.draw(mens_singles).match('1.18').winner(men.Shevchenko).in_sets(3)  # (   ) Mannarino  OR  (   ) Shevchenko
    TEAM.draw(mens_singles).match('1.19').winner(men.Dellien).in_sets(4)  # (   ) Giron  OR  (   ) Dellien
    TEAM.draw(mens_singles).match('1.20').winner(men.Griekspoor).in_sets(4)  # (   ) Fucsovics  OR  ( 28) Griekspoor
    TEAM.draw(mens_singles).match('1.21').winner(men.Cerundolo_Francisco).in_sets(3)  # ( 18) Cerundolo_Francisco  OR  (   ) Borges
    TEAM.draw(mens_singles).match('1.22').winner(men.Lehecka).in_sets(3)  # (   ) Lehecka  OR  ( WC) Ofner
    TEAM.draw(mens_singles).match('1.23').winner(men.Raonic).in_sets(3)  # (   ) Raonic  OR  (  Q) Novak
    TEAM.draw(mens_singles).match('1.24').winner(men.Paul).in_sets(3)  # (  Q) Mochizuki  OR  ( 16) Paul
    TEAM.draw(mens_singles).match('1.25').winner(men.Norrie).in_sets(3)  # ( 12) Norrie  OR  (  Q) Machac
    TEAM.draw(mens_singles).match('1.26').winner(men.Monteiro).in_sets(4)  # (   ) Eubanks  OR  (   ) Monteiro
    TEAM.draw(mens_singles).match('1.27').winner(men.OConnell).in_sets(4)  # (   ) OConnell  OR  (  Q) Medjedovic
    TEAM.draw(mens_singles).match('1.28').winner(men.Korda).in_sets(3)  # (   ) Vesely  OR  ( 22) Korda
    TEAM.draw(mens_singles).match('1.29').winner(men.Shelton).in_sets(3)  # ( 32) Shelton  OR  ( LL) Daniel
    TEAM.draw(mens_singles).match('1.30').winner(men.Cressy).in_sets(4)  # (   ) Cressy  OR  (   ) Djere
    TEAM.draw(mens_singles).match('1.31').winner(men.Murray_Andy).in_sets(4)  # ( WC) Peniston  OR  (   ) Murray_Andy
    TEAM.draw(mens_singles).match('1.32').winner(men.Tsitsipas).in_sets(3)  # (   ) Thiem  OR  (  5) Tsitsipas
    TEAM.draw(mens_singles).match('1.33').winner(men.Sinner).in_sets(3)  # (  8) Sinner  OR  (   ) Cerundolo_Juan
    TEAM.draw(mens_singles).match('1.34').winner(men.Schwartzman).in_sets(4)  # (   ) Kecmanovic  OR  (   ) Schwartzman
    TEAM.draw(mens_singles).match('1.35').winner(men.Vukic).in_sets(4)  # (   ) Vukic  OR  (   ) Altmaier
    TEAM.draw(mens_singles).match('1.36').winner(men.Evans).in_sets(3)  # (   ) Halys  OR  ( 27) Evans
    TEAM.draw(mens_singles).match('1.37').winner(men.Nishioka).in_sets(3)  # ( 24) Nishioka  OR  (   ) Galan
    TEAM.draw(mens_singles).match('1.38').winner(men.Koepfer).in_sets(4)  # (   ) Koepfer  OR  (  Q) Otte
    TEAM.draw(mens_singles).match('1.39').winner(men.Ymer_Mikael).in_sets(4)  # (   ) Ymer_Mikael  OR  (   ) Molcan
    TEAM.draw(mens_singles).match('1.40').winner(men.Fritz).in_sets(3)  # (   ) Hanfmann  OR  (  9) Fritz
    TEAM.draw(mens_singles).match('1.41').winner(men.Coric).in_sets(3)  # ( 13) Coric  OR  (   ) Pella
    TEAM.draw(mens_singles).match('1.42').winner(men.Bonzi).in_sets(4)  # (   ) Bonzi  OR  (  Q) Mayot
    TEAM.draw(mens_singles).match('1.43').winner(men.Moutet).in_sets(4)  # (   ) Moutet  OR  (   ) Gasquet
    TEAM.draw(mens_singles).match('1.44').winner(men.Bautista_Agut).in_sets(3)  # (   ) Safiullin  OR  ( 20) Bautista_Agut
    TEAM.draw(mens_singles).match('1.45').winner(men.Shapovalov).in_sets(4)  # ( 26) Shapovalov  OR  (  Q) Albot
    TEAM.draw(mens_singles).match('1.46').winner(men.Harris).in_sets(4)  # (   ) Harris  OR  (   ) Barrere
    TEAM.draw(mens_singles).match('1.47').winner(men.Lestienne).in_sets(3)  # ( WC) Broady  OR  (   ) Lestienne
    TEAM.draw(mens_singles).match('1.48').winner(men.Ruud).in_sets(3)  # (  Q) Lokoli  OR  (  4) Ruud
    TEAM.draw(mens_singles).match('1.49').winner(men.Rublev).in_sets(3)  # (  7) Rublev  OR  (   ) Purcell
    TEAM.draw(mens_singles).match('1.50').winner(men.Van_Assche).in_sets(3)  # (   ) Van_Assche  OR  (   ) Karatsev
    TEAM.draw(mens_singles).match('1.51').winner(men.Baez).in_sets(3)  # (   ) Baez  OR  (  Q) Vera
    TEAM.draw(mens_singles).match('1.52').winner(men.Goffin).in_sets(3)  # ( WC) Goffin  OR  ( 30) Marozan
    TEAM.draw(mens_singles).match('1.53').winner(men.Bublik).in_sets(4)  # ( 23) Bublik  OR  (   ) Mcdonald
    TEAM.draw(mens_singles).match('1.54').winner(men.Wolf).in_sets(3)  # (   ) Wolf  OR  (  Q) Couacaud
    TEAM.draw(mens_singles).match('1.55').winner(men.Gojo).in_sets(3)  # (  Q) Marterer  OR  (   ) Gojo
    TEAM.draw(mens_singles).match('1.56').winner(men.Auger_Aliassime).in_sets(3)  # (   ) Krajinovic  OR  ( 11) Auger_Aliassime
    TEAM.draw(mens_singles).match('1.57').winner(men.Musetti).in_sets(4)  # ( 14) Musetti  OR  (   ) Varillas
    TEAM.draw(mens_singles).match('1.58').winner(men.Isner).in_sets(5)  # (   ) Isner  OR  (   ) Munar
    TEAM.draw(mens_singles).match('1.59').winner(men.Lajovic).in_sets(4)  # ( WC) Choinski  OR  (   ) Lajovic
    TEAM.draw(mens_singles).match('1.60').winner(men.Hurkacz).in_sets(3)  # (   ) Ramos_Vinolas  OR  ( 17) Hurkacz
    TEAM.draw(mens_singles).match('1.61').winner(men.Etcheverry).in_sets(3)  # ( 29) Etcheverry  OR  (   ) Zapata_Miralles
    TEAM.draw(mens_singles).match('1.62').winner(men.Wawrinka).in_sets(4)  # (   ) Ruusuvuori  OR  (   ) Wawrinka
    TEAM.draw(mens_singles).match('1.63').winner(men.Nakashima).in_sets(4)  # (   ) Thompson  OR  (   ) Nakashima
    TEAM.draw(mens_singles).match('1.64').winner(men.Djokovic).in_sets(3)  # (   ) Cachin  OR  (  2) Djokovic
