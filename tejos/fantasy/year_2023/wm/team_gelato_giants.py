import sys
from tejos.fantasy.teams import *
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women
from tejos.players.wta_players import *
from tejos.players.atp_players import *

this = sys.modules[__name__]

TEAM = TeamGelatoGiants


def team_gelato_giants(mens_singles, womens_singles):
    helpers.selection_fn_caller(this, [mens_singles, womens_singles])
    return TEAM


# womens_singles_round_7:START

# womens_singles_round_7:END


# mens_singles_round_7:START

# mens_singles_round_7:END



# womens_singles_round_6:START

# womens_singles_round_6:END


# mens_singles_round_6:START

# mens_singles_round_6:END



# womens_singles_round_5:START

# womens_singles_round_5:END


# mens_singles_round_5:START

# mens_singles_round_5:END



# womens_singles_round_4:START
def womens_singles_round_4(womens_singles):
    TEAM.draw(womens_singles).match('4.1').winner(women).in_sets()  # (  1) Swiatek  OR  ( 14) Bencic
    TEAM.draw(womens_singles).match('4.2').winner(women).in_sets()  # ( 19) Azarenka  OR  ( WC) Svitolina
    TEAM.draw(womens_singles).match('4.3').winner(women).in_sets()  # (  4) Pegula  OR  (   ) Tsurenko
    TEAM.draw(womens_singles).match('4.4').winner(women).in_sets()  # (   ) Vondrousova  OR  ( 32) Bouzkova
    TEAM.draw(womens_singles).match('4.5').winner(women).in_sets()  # (  6) Jabeur  OR  (  9) Kvitova
    TEAM.draw(womens_singles).match('4.6').winner(women).in_sets()  # ( 13) Haddad_Maia  OR  (  3) Rybakina
    TEAM.draw(womens_singles).match('4.7').winner(women).in_sets()  # ( 25) Keys  OR  TBD
    TEAM.draw(womens_singles).match('4.8').winner(women).in_sets()  # ( 21) Alexandrova  OR  (  2) Sabalenka
# womens_singles_round_4:END


# mens_singles_round_4:START
def mens_singles_round_4(mens_singles):
    TEAM.draw(mens_singles).match('4.1').winner(men).in_sets()  # (  1) Alcaraz  OR  (   ) Berrettini
    TEAM.draw(mens_singles).match('4.2').winner(men).in_sets()  # (  6) Rune  OR  TBD
    TEAM.draw(mens_singles).match('4.3').winner(men).in_sets()  # (  3) Medvedev  OR  (   ) Lehecka
    TEAM.draw(mens_singles).match('4.4').winner(men).in_sets()  # (   ) Eubanks  OR  (  5) Tsitsipas
    TEAM.draw(mens_singles).match('4.5').winner(men).in_sets()  # (  8) Sinner  OR  (   ) Galan
    TEAM.draw(mens_singles).match('4.6').winner(men).in_sets()  # (   ) Safiullin  OR  ( 26) Shapovalov
    TEAM.draw(mens_singles).match('4.7').winner(men).in_sets()  # (  7) Rublev  OR  ( 23) Bublik
    TEAM.draw(mens_singles).match('4.8').winner(men).in_sets()  # ( 17) Hurkacz  OR  (  2) Djokovic
# mens_singles_round_4:END



# womens_singles_round_3:START
def womens_singles_round_3(womens_singles):
    TEAM.draw(womens_singles).match('3.1').winner(women.Swiatek).in_sets(2)  # (  1) Iga Swiatek  OR  ( 30) Petra Martic
    TEAM.draw(womens_singles).match('3.2').winner(women.Bencic).in_sets(3)  # ( 23) Magda Linette  OR  ( 14) Belinda Bencic
    TEAM.draw(womens_singles).match('3.3').winner(women.Azarenka).in_sets(3)  # ( 11) Daria Kasatkina  OR  ( 19) Victoria Azarenka
    TEAM.draw(womens_singles).match('3.4').winner(women.Svitolina).in_sets(3)  # ( WC) Svitolina  OR  (  Q) Sofia Kenin
    TEAM.draw(womens_singles).match('3.5').winner(women.Cocciaretto).in_sets(3)  # (  4) Jessica Pegula  OR  (   ) Elisabetta Cocciaretto
    TEAM.draw(womens_singles).match('3.6').winner(women.Bogdan).in_sets(2)  # (   ) Lesia Tsurenko  OR  (   ) Ana Bogdan
    TEAM.draw(womens_singles).match('3.7').winner(women.Vekic).in_sets(3)  # (   ) Marketa Vondrousova  OR  ( 20) Donna Vekic
    TEAM.draw(womens_singles).match('3.8').winner(women.Garcia).in_sets(3)  # ( 32) Marie Bouzkova  OR  (  5) Caroline Garcia
    TEAM.draw(womens_singles).match('3.9').winner(women).in_sets()  # (  6) Jabeur  OR  (   ) Andreescu
    TEAM.draw(womens_singles).match('3.10').winner(women).in_sets()  # (  Q) Stevanovic  OR  (  9) Kvitova
    TEAM.draw(womens_singles).match('3.11').winner(women.Haddad_Maia).in_sets(2)  # ( 13) Beatriz Haddad Maia  OR  (   ) Sorana Cirstea
    TEAM.draw(womens_singles).match('3.12').winner(women.Boulter).in_sets(3)  # ( WC) Katie Boulter  OR  (  3) Elena Rybakina
    TEAM.draw(womens_singles).match('3.13').winner(women).in_sets()  # (   ) Kostyuk  OR  ( 25) Keys
    TEAM.draw(womens_singles).match('3.14').winner(women.Andreeva_Mirra).in_sets(3)  # ( 22) Anastasia Potapova  OR  (  Q) Mirra Andreeva
    TEAM.draw(womens_singles).match('3.15').winner(women).in_sets()  # (   ) Galfi  OR  ( 21) Alexandrova
    TEAM.draw(womens_singles).match('3.16').winner(women).in_sets()  # (   ) Blinkova  OR  (  2) Sabalenka
# womens_singles_round_3:END


# mens_singles_round_3:START
def mens_singles_round_3(mens_singles):
    TEAM.draw(mens_singles).match('3.1').winner(men).in_sets()  # (  1) Alcaraz  OR  ( 25) Jarry
    TEAM.draw(mens_singles).match('3.2').winner(men).in_sets()  # ( 19) Zverev  OR  (   ) Berrettini
    TEAM.draw(mens_singles).match('3.3').winner(men.Tiafoe).in_sets(4)  # ( 10) Frances Tiafoe  OR  ( 21) Grigor Dimitrov
    TEAM.draw(mens_singles).match('3.4').winner(men).in_sets()  # ( 31) Davidovich_Fokina  OR  (  6) Rune
    TEAM.draw(mens_singles).match('3.5').winner(men).in_sets()  # (  3) Medvedev  OR  (   ) Fucsovics
    TEAM.draw(mens_singles).match('3.6').winner(men.Paul).in_sets(4)  # (   ) Jiri Lehecka  OR  ( 16) Tommy Paul
    TEAM.draw(mens_singles).match('3.7').winner(men).in_sets()  # (   ) Eubanks  OR  (   ) OConnell
    TEAM.draw(mens_singles).match('3.8').winner(men).in_sets()  # (   ) Djere  OR  (  5) Tsitsipas
    TEAM.draw(mens_singles).match('3.9').winner(men.Sinner).in_sets(4)  # (  8) Jannik Sinner  OR  (   ) Quentin Halys
    TEAM.draw(mens_singles).match('3.10').winner(men.Galan).in_sets(5)  # (   ) Daniel Elahi Galan  OR  (   ) Mikael Ymer
    TEAM.draw(mens_singles).match('3.11').winner(men.Pella).in_sets(5)  # (   ) Guido Pella  OR  (   ) Roman Safiullin
    TEAM.draw(mens_singles).match('3.12').winner(men.Broady).in_sets(5)  # ( 26) Denis Shapovalov  OR  ( WC) Liam Broady
    TEAM.draw(mens_singles).match('3.13').winner(men.Goffin).in_sets(4)  # (  7) Andrey Rublev  OR  ( WC) David Goffin
    TEAM.draw(mens_singles).match('3.14').winner(men.Marterer).in_sets(5)  # ( 23) Alexander Bublik  OR  (  Q) Maximilian Marterer
    TEAM.draw(mens_singles).match('3.15').winner(men.Musetti).in_sets(4)  # ( 14) Lorenzo Musetti  OR  ( 17) Hubert Hurkacz
    TEAM.draw(mens_singles).match('3.16').winner(men.Wawrinka).in_sets(5)  # (   ) Stan Wawrinka  OR  (  2) Novak Djokovic
# mens_singles_round_3:END


# womens_singles_round_2:START
def womens_singles_round_2(womens_singles):
    TEAM.draw(womens_singles).match('2.1').winner(women.Swiatek).in_sets(2)  # (  1) Iga Swiatek  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles).match('2.2').winner(women.Martic).in_sets(3)  # (   ) Diane Parry  OR  ( 30) Petra Martic
    TEAM.draw(womens_singles).match('2.3').winner(women.Linette).in_sets(3)  # ( 23) Magda Linette  OR  (   ) Barbora Strycova
    TEAM.draw(womens_singles).match('2.4').winner(women.Bencic).in_sets(2)  # (   ) Danielle Collins  OR  ( 14) Belinda Bencic
    TEAM.draw(womens_singles).match('2.5').winner(women.Kasatkina).in_sets(2)  # ( 11) Daria Kasatkina  OR  ( WC) Jodie Burrage
    TEAM.draw(womens_singles).match('2.6').winner(women.Azarenka).in_sets(3)  # (   ) Nadia Podoroska  OR  ( 19) Victoria Azarenka
    TEAM.draw(womens_singles).match('2.7').winner(women.Svitolina).in_sets(3)  # ( 28) Elise Mertens  OR  ( WC) Svitolina
    TEAM.draw(womens_singles).match('2.8').winner(women.Wang_Xinyu).in_sets(3)  # (   ) Xinyu Wang  OR  (  Q) Sofia Kenin
    TEAM.draw(womens_singles).match('2.9').winner(women.Pegula).in_sets(3)  # (  4) Jessica Pegula  OR  (   ) Cristina Bucsa
    TEAM.draw(womens_singles).match('2.10').winner(women.Cocciaretto).in_sets(3)  # (   ) Elisabetta Cocciaretto  OR  (   ) Rebeka Masarova
    TEAM.draw(womens_singles).match('2.11').winner(women.Siniakova).in_sets(3)  # (   ) Katerina Siniakova  OR  (   ) Lesia Tsurenko
    TEAM.draw(womens_singles).match('2.12').winner(women.Parks).in_sets(3)  # (   ) Alycia Parks  OR  (   ) Ana Bogdan
    TEAM.draw(womens_singles).match('2.13').winner(women.Kudermetova_Veronika).in_sets(3)  # ( 12) Veronika Kudermetova  OR  (   ) Marketa Vondrousova
    TEAM.draw(womens_singles).match('2.14').winner(women.Vekic).in_sets(3)  # (   ) Sloane Stephens  OR  ( 20) Donna Vekic
    TEAM.draw(womens_singles).match('2.15').winner(women.Bouzkova).in_sets(3)  # ( 32) Marie Bouzkova  OR  (   ) Anett Kontaveit
    TEAM.draw(womens_singles).match('2.16').winner(women.Garcia).in_sets(3)  # (   ) Leylah Fernandez  OR  (  5) Caroline Garcia
    TEAM.draw(womens_singles).match('2.17').winner(women.Jabeur).in_sets(2)  # (  6) Ons Jabeur  OR  (  Q) Zhuoxuan Bai
    TEAM.draw(womens_singles).match('2.18').winner(women.Kalinina).in_sets(3)  # (   ) Andreescu  OR  ( 26) Kalinina
    TEAM.draw(womens_singles).match('2.19').winner(women.Stevanovic).in_sets(3)  # (  Q) Natalija Stevanovic  OR  ( LL) Tamara Korpatsch
    TEAM.draw(womens_singles).match('2.20').winner(women.Kvitova).in_sets(2)  # (   ) Sasnovich  OR  (  9) Kvitova
    TEAM.draw(womens_singles).match('2.21').winner(women.Haddad_Maia).in_sets(2)  # ( 13) Beatriz Haddad Maia  OR  (   ) Jaqueline Cristian
    TEAM.draw(womens_singles).match('2.22').winner(women.Ostapenko).in_sets(3)  # (   ) Sorana Cirstea  OR  ( 17) Jelena Ostapenko
    TEAM.draw(womens_singles).match('2.23').winner(women.Tomova).in_sets(2)  # (   ) Viktoriya Tomova  OR  ( WC) Katie Boulter
    TEAM.draw(womens_singles).match('2.24').winner(women.Rybakina).in_sets(2)  # (   ) Alize Cornet  OR  (  3) Elena Rybakina
    TEAM.draw(womens_singles).match('2.25').winner(women.Badosa).in_sets(2)  # (   ) Marta Kostyuk  OR  (   ) Paula Badosa
    TEAM.draw(womens_singles).match('2.26').winner(women.Keys).in_sets(2)  # (  Q) Golubic  OR  ( 25) Keys
    TEAM.draw(womens_singles).match('2.27').winner(women.Potapova).in_sets(2)  # ( 22) Anastasia Potapova  OR  (  Q) Kaja Juvan
    TEAM.draw(womens_singles).match('2.28').winner(women.Andreeva_Mirra).in_sets(3)  # (  Q) Mirra Andreeva  OR  ( 10) Barbora Krejcikova
    TEAM.draw(womens_singles).match('2.29').winner(women.Galfi).in_sets(3)  # (   ) Niemeier  OR  (   ) Galfi
    TEAM.draw(womens_singles).match('2.30').winner(women.Alexandrova).in_sets(3)  # (   ) Madison Brengle  OR  ( 21) Ekaterina Alexandrova
    TEAM.draw(womens_singles).match('2.31').winner(women.Begu).in_sets(3)  # ( 29) Begu  OR  (   ) Blinkova
    TEAM.draw(womens_singles).match('2.32').winner(women.Sabalenka).in_sets(2)  # (   ) Varvara Gracheva  OR  (  2) Aryna Sabalenka
# womens_singles_round_2:END


# mens_singles_round_2:START
def mens_singles_round_2(mens_singles):
    TEAM.draw(mens_singles).match('2.1').winner(men.Alcaraz).in_sets(3)  # (  1) Carlos Alcaraz  OR  (   ) Alexandre Muller
    TEAM.draw(mens_singles).match('2.2').winner(men.Kubler).in_sets(4)  # (   ) Kubler  OR  ( 25) Jarry
    TEAM.draw(mens_singles).match('2.3').winner(men.Zverev).in_sets(4)  # ( 19) Zverev  OR  ( LL) Watanuki
    TEAM.draw(mens_singles).match('2.4').winner(men.Berrettini).in_sets(5)  # (   ) Berrettini  OR  ( 15) De_Minaur
    TEAM.draw(mens_singles).match('2.5').winner(men.Tiafoe).in_sets(4)  # ( 10) Frances Tiafoe  OR  (  Q) D.Stricker
    TEAM.draw(mens_singles).match('2.6').winner(men.Dimitrov).in_sets(4)  # (   ) Ilya Ivashka  OR  ( 21) Grigor Dimitrov
    TEAM.draw(mens_singles).match('2.7').winner(men.Van_De_Zandschulp).in_sets(5)  # ( 31) Davidovich_Fokina  OR  (   ) Van_De_Zandschulp
    TEAM.draw(mens_singles).match('2.8').winner(men.Carballes_Baena).in_sets(5)  # (   ) Carballes_Baena  OR  (  6) Rune
    TEAM.draw(mens_singles).match('2.9').winner(men.Medvedev).in_sets(3)  # (  3) Daniil Medvedev  OR  (   ) Adrian Mannarino
    TEAM.draw(mens_singles).match('2.10').winner(men.Fucsovics).in_sets(4)  # (   ) Marcos Giron  OR  (   ) Marton Fucsovics
    TEAM.draw(mens_singles).match('2.11').winner(men.Cerundolo_Francisco).in_sets(4)  # ( 18) Francisco Cerundolo  OR  (   ) Jiri Lehecka
    TEAM.draw(mens_singles).match('2.12').winner(men.Paul).in_sets(4)  # (   ) Milos Raonic  OR  ( 16) Tommy Paul
    TEAM.draw(mens_singles).match('2.13').winner(men.Norrie).in_sets(3)  # ( 12) Cameron Norrie  OR  (   ) Christopher Eubanks
    TEAM.draw(mens_singles).match('2.14').winner(men.OConnell).in_sets(5)  # (   ) OConnell  OR  (   ) Vesely
    TEAM.draw(mens_singles).match('2.15').winner(men.Shelton).in_sets(4)  # ( 32) Shelton  OR  (   ) Djere
    TEAM.draw(mens_singles).match('2.16').winner(men.Murray_Andy).in_sets(5)  # (   ) Murray_Andy  OR  (  5) Tsitsipas
    TEAM.draw(mens_singles).match('2.17').winner(men.Sinner).in_sets(4)  # (  8) Jannik Sinner  OR  (   ) Diego Schwartzman
    TEAM.draw(mens_singles).match('2.18').winner(men.Halys).in_sets(4)  # (   ) Aleksandar Vukic  OR  (   ) Quentin Halys
    TEAM.draw(mens_singles).match('2.19').winner(men.Otte).in_sets(5)  # (   ) Daniel Elahi Galan  OR  (  Q) Oscar Otte
    TEAM.draw(mens_singles).match('2.20').winner(men.Fritz).in_sets(4)  # (   ) Mikael Ymer  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles).match('2.21').winner(men.Mayot).in_sets(4)  # (   ) Guido Pella  OR  (  Q) Harold Mayot
    TEAM.draw(mens_singles).match('2.22').winner(men.Moutet).in_sets(4)  # (   ) Corentin Moutet  OR  (   ) Roman Safiullin
    TEAM.draw(mens_singles).match('2.23').winner(men.Barrere).in_sets(4)  # ( 26) Denis Shapovalov  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles).match('2.24').winner(men.Broady).in_sets(5)  # ( WC) Liam Broady  OR  (  4) Casper Ruud
    TEAM.draw(mens_singles).match('2.25').winner(men.Rublev).in_sets(4)  # (  7) Andrey Rublev  OR  (   ) Aslan Karatsev
    TEAM.draw(mens_singles).match('2.26').winner(men.Vera).in_sets(4)  # (  Q) Tomas Barrios Vera  OR  ( WC) David Goffin
    TEAM.draw(mens_singles).match('2.27').winner(men.Wolf).in_sets(5)  # ( 23) Alexander Bublik  OR  (   ) J.J. Wolf
    TEAM.draw(mens_singles).match('2.28').winner(men.Marterer).in_sets(5)  # (  Q) Maximilian Marterer  OR  (   ) Michael Mmoh
    TEAM.draw(mens_singles).match('2.29').winner(men.Musetti).in_sets(4)  # ( 14) Lorenzo Musetti  OR  (   ) Jaume Munar
    TEAM.draw(mens_singles).match('2.30').winner(men.Choinski).in_sets(5)  # ( WC) Jan Choinski  OR  ( 17) Hubert Hurkacz
    TEAM.draw(mens_singles).match('2.31').winner(men.Wawrinka).in_sets(4)  # ( 29) Tomas Martin Etcheverry  OR  (   ) Stan Wawrinka
    TEAM.draw(mens_singles).match('2.32').winner(men.Djokovic).in_sets(4)  # (   ) Jordan Thompson  OR  (  2) Novak Djokovic
# mens_singles_round_2:END


def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles).match('1.1').winner(women.Swiatek).in_sets(2)  # (  1) Swiatek  OR  (   ) Zhu
    TEAM.draw(womens_singles).match('1.2').winner(women.Sorribes_Tormo).in_sets(3)  # (   ) Trevisan  OR  (   ) Sorribes_Tormo
    TEAM.draw(womens_singles).match('1.3').winner(women.Dart).in_sets(3)  # (   ) Parry  OR  ( WC) Dart
    TEAM.draw(womens_singles).match('1.4').winner(women.Martic).in_sets(2)  # (   ) Fruhvirtova_Linda  OR  ( 30) Martic
    TEAM.draw(womens_singles).match('1.5').winner(women.Linette).in_sets(2)  # ( 23) Linette  OR  (   ) Teichmann
    TEAM.draw(womens_singles).match('1.6').winner(women.Strycova).in_sets(2)  # (   ) Strycova  OR  (   ) Zanevska
    TEAM.draw(womens_singles).match('1.7').winner(women.Collins).in_sets(3)  # (   ) Collins  OR  (   ) Grabher
    TEAM.draw(womens_singles).match('1.8').winner(women.Bencic).in_sets(2)  # ( WC) Swan  OR  ( 14) Bencic
    TEAM.draw(womens_singles).match('1.9').winner(women.Kasatkina).in_sets(2)  # ( 11) Kasatkina  OR  (   ) Dolehide
    TEAM.draw(womens_singles).match('1.10').winner(women.Burrage).in_sets(3)  # ( WC) Burrage  OR  (   ) Mcnally
    TEAM.draw(womens_singles).match('1.11').winner(women.Podoroska).in_sets(2)  # (   ) Podoroska  OR  (   ) Martincova
    TEAM.draw(womens_singles).match('1.12').winner(women.Azarenka).in_sets(2)  # (  Q) Yuan  OR  ( 19) Azarenka
    TEAM.draw(womens_singles).match('1.13').winner(women.Mertens).in_sets(2)  # ( 28) Mertens  OR  (  Q) Hruncakova
    TEAM.draw(womens_singles).match('1.14').winner(women.Williams).in_sets(3)  # ( WC) Williams  OR  ( WC) Svitolina
    TEAM.draw(womens_singles).match('1.15').winner(women.Wang_Xinyu).in_sets(3)  # (  Q) Hunter  OR  (   ) Wang_Xinyu
    TEAM.draw(womens_singles).match('1.16').winner(women.Gauff).in_sets(2)  # (  Q) Kenin  OR  (  7) Gauff
    TEAM.draw(womens_singles).match('1.17').winner(women.Pegula).in_sets()  # (  4) Pegula  OR  (   ) Davis
    TEAM.draw(womens_singles).match('1.18').winner(women.Bucsa).in_sets(3)  # (   ) Bucsa  OR  (   ) Rakhimova
    TEAM.draw(womens_singles).match('1.19').winner(women.Cocciaretto).in_sets(3)  # (   ) Osorio  OR  (   ) Cocciaretto
    TEAM.draw(womens_singles).match('1.20').winner(women.Sherif).in_sets(2)  # (   ) Masarova  OR  ( 31) Sherif
    TEAM.draw(womens_singles).match('1.21').winner(women.Zheng).in_sets(2)  # ( 24) Zheng  OR  (   ) Siniakova
    TEAM.draw(womens_singles).match('1.22').winner(women.Liu).in_sets(3)  # (   ) Tsurenko  OR  (   ) Liu
    TEAM.draw(womens_singles).match('1.23').winner(women.Parks).in_sets(3)  # (   ) Parks  OR  (   ) Friedsam
    TEAM.draw(womens_singles).match('1.24').winner(women.Samsonova).in_sets(2)  # (   ) Bogdan  OR  ( 15) Samsonova
    TEAM.draw(womens_singles).match('1.25').winner(women.Kudermetova_Veronika).in_sets(2)  # ( 12) Kudermetova_Veronika  OR  (   ) Kanepi
    TEAM.draw(womens_singles).match('1.26').winner(women.Stearns).in_sets(2)  # (   ) Vondrousova  OR  (   ) Stearns
    TEAM.draw(womens_singles).match('1.27').winner(women.Stephens).in_sets(2)  # (   ) Stephens  OR  (   ) Peterson
    TEAM.draw(womens_singles).match('1.28').winner(women.Vekic).in_sets(2)  # (   ) Zhang_Shuai  OR  ( 20) Vekic
    TEAM.draw(womens_singles).match('1.29').winner(women.Bouzkova).in_sets(2)  # ( 32) Bouzkova  OR  (  Q) Waltert
    TEAM.draw(womens_singles).match('1.30').winner(women.Stefanini).in_sets(3)  # (   ) Kontaveit  OR  (  Q) Stefanini
    TEAM.draw(womens_singles).match('1.31').winner(women.Fernandez).in_sets(3)  # (   ) Baindl  OR  (   ) Fernandez
    TEAM.draw(womens_singles).match('1.32').winner(women.Garcia).in_sets(2)  # (   ) Volynets  OR  (  5) Garcia
    TEAM.draw(womens_singles).match('1.33').winner(women.Jabeur).in_sets(2)  # (  6) Jabeur  OR  (   ) Frech
    TEAM.draw(womens_singles).match('1.34').winner(women.Bonaventure).in_sets(2)  # (   ) Bonaventure  OR  (  Q) Bai
    TEAM.draw(womens_singles).match('1.35').winner(women.Andreescu).in_sets(3)  # (   ) Bondar  OR  (   ) Andreescu
    TEAM.draw(womens_singles).match('1.36').winner(women.Kalinina).in_sets(2)  # (  Q) Maneiro  OR  ( 26) Kalinina
    TEAM.draw(womens_singles).match('1.37').winner(women.Pliskova).in_sets(2)  # ( 18) Pliskova  OR  (  Q) Stevanovic
    TEAM.draw(womens_singles).match('1.38').winner(women.Zhao).in_sets(3)  # (  Q) Zhao  OR  ( LL) Korpatsch
    TEAM.draw(womens_singles).match('1.39').winner(women.Parrizas_Diaz).in_sets(3)  # (   ) Sasnovich  OR  (   ) Parrizas_Diaz
    TEAM.draw(womens_singles).match('1.40').winner(women.Kvitova).in_sets(2)  # (   ) Paolini  OR  (  9) Kvitova
    TEAM.draw(womens_singles).match('1.41').winner(women.Haddad_Maia).in_sets(2)  # ( 13) Haddad_Maia  OR  (   ) Putintseva
    TEAM.draw(womens_singles).match('1.42').winner(women.Bronzetti).in_sets(3)  # (   ) Cristian  OR  (   ) Bronzetti
    TEAM.draw(womens_singles).match('1.43').winner(women.Maria).in_sets(3)  # (   ) Cirstea  OR  (   ) Maria
    TEAM.draw(womens_singles).match('1.44').winner(women.Ostapenko).in_sets(2)  # (  Q) Minnen  OR  ( 17) Ostapenko
    TEAM.draw(womens_singles).match('1.45').winner(women.Pera).in_sets(2)  # ( 27) Pera  OR  (   ) Tomova
    TEAM.draw(womens_singles).match('1.46').winner(women.Saville).in_sets(3)  # ( WC) Boulter  OR  (   ) Saville
    TEAM.draw(womens_singles).match('1.47').winner(women.Cornet).in_sets(3)  # ( LL) Hibino  OR  (   ) Cornet
    TEAM.draw(womens_singles).match('1.48').winner(women.Rybakina).in_sets(2)  # (   ) Rogers  OR  (  3) Rybakina
    TEAM.draw(womens_singles).match('1.49').winner(women.Sakkari).in_sets(2)  # (  8) Sakkari  OR  (   ) Kostyuk
    TEAM.draw(womens_singles).match('1.50').winner(women.Badosa).in_sets(3)  # (   ) Riske_Amritraj  OR  (   ) Badosa
    TEAM.draw(womens_singles).match('1.51').winner(women.Golubic).in_sets(3)  # (  Q) Golubic  OR  (   ) Schmiedlova
    TEAM.draw(womens_singles).match('1.52').winner(women.Keys).in_sets(2)  # ( WC) Kartal  OR  ( 25) Keys
    TEAM.draw(womens_singles).match('1.53').winner(women.Potapova).in_sets(2)  # ( 22) Potapova  OR  (  Q) Naef
    TEAM.draw(womens_singles).match('1.54').winner(women.Betova).in_sets(2)  # (  Q) Juvan  OR  (   ) Betova
    TEAM.draw(womens_singles).match('1.55').winner(women.Andreeva_Mirra).in_sets(3)  # (  Q) Andreeva_Mirra  OR  (   ) Wang_Xiyu
    TEAM.draw(womens_singles).match('1.56').winner(women.Krejcikova).in_sets(2)  # ( WC) Watson  OR  ( 10) Krejcikova
    TEAM.draw(womens_singles).match('1.57').winner(women.Muchova).in_sets(2)  # ( 16) Muchova  OR  (   ) Niemeier
    TEAM.draw(womens_singles).match('1.58').winner(women.Galfi).in_sets(3)  # (   ) Noskova  OR  (   ) Galfi
    TEAM.draw(womens_singles).match('1.59').winner(women.Errani).in_sets(3)  # (   ) Brengle  OR  (   ) Errani
    TEAM.draw(womens_singles).match('1.60').winner(women.Alexandrova).in_sets(2)  # (   ) Navarro  OR  ( 21) Alexandrova
    TEAM.draw(womens_singles).match('1.61').winner(women.Begu).in_sets(2)  # ( 29) Begu  OR  (   ) Marino
    TEAM.draw(womens_singles).match('1.62').winner(women.Blinkova).in_sets(2)  # (  Q) Wickmayer  OR  (   ) Blinkova
    TEAM.draw(womens_singles).match('1.63').winner(women.Giorgi).in_sets(2)  # (   ) Gracheva  OR  (   ) Giorgi
    TEAM.draw(womens_singles).match('1.64').winner(women.Sabalenka).in_sets(2)  # (   ) Udvardy  OR  (  2) Sabalenka


def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles).match('1.1').winner(men.Alcaraz).in_sets(3)  # (  1) Alcaraz  OR  (   ) Chardy
    TEAM.draw(mens_singles).match('1.2').winner(men.Muller).in_sets(3)  # (   ) Muller  OR  (   ) Rinderknech
    TEAM.draw(mens_singles).match('1.3').winner(men.Kubler).in_sets(4)  # (   ) Kubler  OR  (   ) Humbert
    TEAM.draw(mens_singles).match('1.4').winner(men.Jarry).in_sets(3)  # (   ) Cecchinato  OR  ( 25) Jarry
    TEAM.draw(mens_singles).match('1.5').winner(men.Zverev).in_sets(3)  # ( 19) Zverev  OR  (  Q) Brouwer
    TEAM.draw(mens_singles).match('1.6').winner(men.Huesler).in_sets(5)  # (   ) Huesler  OR  ( LL) Watanuki
    TEAM.draw(mens_singles).match('1.7').winner(men.Berrettini).in_sets(4)  # (   ) Berrettini  OR  (   ) Sonego
    TEAM.draw(mens_singles).match('1.8').winner(men.De_Minaur).in_sets(3)  # (  Q) Coppejans  OR  ( 15) De_Minaur
    TEAM.draw(mens_singles).match('1.9').winner(men.Tiafoe).in_sets(3)  # ( 10) Tiafoe  OR  (   ) Wu
    TEAM.draw(mens_singles).match('1.10').winner(men.Stricker).in_sets(4)  # (  Q) Stricker  OR  (   ) Popyrin
    TEAM.draw(mens_singles).match('1.11').winner(men.Coria).in_sets(4)  # (   ) Ivashka  OR  (   ) Coria
    TEAM.draw(mens_singles).match('1.12').winner(men.Dimitrov).in_sets(3)  # (  Q) Shimabukuro  OR  ( 21) Dimitrov
    TEAM.draw(mens_singles).match('1.13').winner(men.Fils).in_sets(4)  # ( 31) Davidovich_Fokina  OR  ( WC) Fils
    TEAM.draw(mens_singles).match('1.14').winner(men.Van_De_Zandschulp).in_sets(4)  # (   ) Zhang_Zhizhen  OR  (   ) Van_De_Zandschulp
    TEAM.draw(mens_singles).match('1.15').winner(men.Arnaldi).in_sets(5)  # (  Q) Arnaldi  OR  (   ) Carballes_Baena
    TEAM.draw(mens_singles).match('1.16').winner(men.Rune).in_sets(3)  # ( WC) Loffhagen  OR  (  6) Rune
    TEAM.draw(mens_singles).match('1.17').winner(men.Medvedev).in_sets(3)  # (  3) Medvedev  OR  ( WC) Fery
    TEAM.draw(mens_singles).match('1.18').winner(men.Mannarino).in_sets(4)  # (   ) Mannarino  OR  (   ) Shevchenko
    TEAM.draw(mens_singles).match('1.19').winner(men.Giron).in_sets(4)  # (   ) Giron  OR  (   ) Dellien
    TEAM.draw(mens_singles).match('1.20').winner(men.Griekspoor).in_sets(3)  # (   ) Fucsovics  OR  ( 28) Griekspoor
    TEAM.draw(mens_singles).match('1.21').winner(men.Cerundolo_Francisco).in_sets(3)  # ( 18) Cerundolo_Francisco  OR  (   ) Borges
    TEAM.draw(mens_singles).match('1.22').winner(men.Lehecka).in_sets(3)  # (   ) Lehecka  OR  ( WC) Ofner
    TEAM.draw(mens_singles).match('1.23').winner(men.Novak).in_sets(5)  # (   ) Raonic  OR  (  Q) Novak
    TEAM.draw(mens_singles).match('1.24').winner(men.Paul).in_sets(3)  # (  Q) Mochizuki  OR  ( 16) Paul
    TEAM.draw(mens_singles).match('1.25').winner(men.Norrie).in_sets(3)  # ( 12) Norrie  OR  (  Q) Machac
    TEAM.draw(mens_singles).match('1.26').winner(men.Monteiro).in_sets(4)  # (   ) Eubanks  OR  (   ) Monteiro
    TEAM.draw(mens_singles).match('1.27').winner(men.OConnell).in_sets(4)  # (   ) OConnell  OR  (  Q) Medjedovic
    TEAM.draw(mens_singles).match('1.28').winner(men.Korda).in_sets(3)  # (   ) Vesely  OR  ( 22) Korda
    TEAM.draw(mens_singles).match('1.29').winner(men.Shelton).in_sets(4)  # ( 32) Shelton  OR  ( LL) Daniel
    TEAM.draw(mens_singles).match('1.30').winner(men.Cressy).in_sets(4)  # (   ) Cressy  OR  (   ) Djere
    TEAM.draw(mens_singles).match('1.31').winner(men.Murray_Andy).in_sets(4)  # ( WC) Peniston  OR  (   ) Murray_Andy
    TEAM.draw(mens_singles).match('1.32').winner(men.Tsitsipas).in_sets(4)  # (   ) Thiem  OR  (  5) Tsitsipas
    TEAM.draw(mens_singles).match('1.33').winner(men.Sinner).in_sets(4)  # (  8) Sinner  OR  (   ) Cerundolo_Juan
    TEAM.draw(mens_singles).match('1.34').winner(men.Kecmanovic).in_sets(5)  # (   ) Kecmanovic  OR  (   ) Schwartzman
    TEAM.draw(mens_singles).match('1.35').winner(men.Altmaier).in_sets(4)  # (   ) Vukic  OR  (   ) Altmaier
    TEAM.draw(mens_singles).match('1.36').winner(men.Evans).in_sets(3)  # (   ) Halys  OR  ( 27) Evans
    TEAM.draw(mens_singles).match('1.37').winner(men.Nishioka).in_sets(3)  # ( 24) Nishioka  OR  (   ) Galan
    TEAM.draw(mens_singles).match('1.38').winner(men.Otte).in_sets(5)  # (   ) Koepfer  OR  (  Q) Otte
    TEAM.draw(mens_singles).match('1.39').winner(men.Molcan).in_sets(4)  # (   ) Ymer_Mikael  OR  (   ) Molcan
    TEAM.draw(mens_singles).match('1.40').winner(men.Fritz).in_sets(3)  # (   ) Hanfmann  OR  (  9) Fritz
    TEAM.draw(mens_singles).match('1.41').winner(men.Coric).in_sets(3)  # ( 13) Coric  OR  (   ) Pella
    TEAM.draw(mens_singles).match('1.42').winner(men.Bonzi).in_sets(3)  # (   ) Bonzi  OR  (  Q) Mayot
    TEAM.draw(mens_singles).match('1.43').winner(men.Gasquet).in_sets(4)  # (   ) Moutet  OR  (   ) Gasquet
    TEAM.draw(mens_singles).match('1.44').winner(men.Bautista_Agut).in_sets(3)  # (   ) Safiullin  OR  ( 20) Bautista_Agut
    TEAM.draw(mens_singles).match('1.45').winner(men.Shapovalov).in_sets(3)  # ( 26) Shapovalov  OR  (  Q) Albot
    TEAM.draw(mens_singles).match('1.46').winner(men.Harris).in_sets(4)  # (   ) Harris  OR  (   ) Barrere
    TEAM.draw(mens_singles).match('1.47').winner(men.Broady).in_sets(4)  # ( WC) Broady  OR  (   ) Lestienne
    TEAM.draw(mens_singles).match('1.48').winner(men.Ruud).in_sets(3)  # (  Q) Lokoli  OR  (  4) Ruud
    TEAM.draw(mens_singles).match('1.49').winner(men.Rublev).in_sets(3)  # (  7) Rublev  OR  (   ) Purcell
    TEAM.draw(mens_singles).match('1.50').winner(men.Van_Assche).in_sets(5)  # (   ) Van_Assche  OR  (   ) Karatsev
    TEAM.draw(mens_singles).match('1.51').winner(men.Vera).in_sets(4)  # (   ) Baez  OR  (  Q) Vera
    TEAM.draw(mens_singles).match('1.52').winner(men.Goffin).in_sets(4)  # ( WC) Goffin  OR  ( LL) Marozsan
    TEAM.draw(mens_singles).match('1.53').winner(men.Bublik).in_sets(3)  # ( 23) Bublik  OR  (   ) Mcdonald
    TEAM.draw(mens_singles).match('1.54').winner(men.Wolf).in_sets(4)  # (   ) Wolf  OR  (  Q) Couacaud
    TEAM.draw(mens_singles).match('1.55').winner(men.Gojo).in_sets(4)  # (  Q) Marterer  OR  (   ) Gojo
    TEAM.draw(mens_singles).match('1.56').winner(men.Auger_Aliassime).in_sets(3)  # (   ) Mmoh  OR  ( 11) Auger_Aliassime
    TEAM.draw(mens_singles).match('1.57').winner(men.Musetti).in_sets(3)  # ( 14) Musetti  OR  (   ) Varillas
    TEAM.draw(mens_singles).match('1.58').winner(men.Isner).in_sets(4)  # (   ) Isner  OR  (   ) Munar
    TEAM.draw(mens_singles).match('1.59').winner(men.Choinski).in_sets(5)  # ( WC) Choinski  OR  (   ) Lajovic
    TEAM.draw(mens_singles).match('1.60').winner(men.Ramos_Vinolas).in_sets(5)  # (   ) Ramos_Vinolas  OR  ( 17) Hurkacz
    TEAM.draw(mens_singles).match('1.61').winner(men.Etcheverry).in_sets(4)  # ( 29) Etcheverry  OR  (   ) Zapata_Miralles
    TEAM.draw(mens_singles).match('1.62').winner(men.Wawrinka).in_sets(4)  # (   ) Ruusuvuori  OR  (   ) Wawrinka
    TEAM.draw(mens_singles).match('1.63').winner(men.Thompson).in_sets(5)  # (   ) Thompson  OR  (   ) Nakashima
    TEAM.draw(mens_singles).match('1.64').winner(men.Djokovic).in_sets(3)  # (   ) Cachin  OR  (  2) Djokovic










