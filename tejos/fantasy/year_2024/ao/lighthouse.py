import sys

from tejos import model
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women
from tejos.players.wta_players import *
from tejos.players.atp_players import *


this = sys.modules[__name__]

TEAM = None

def team():
    this.TEAM = model.Team.get('LightHouse')


def team_lighthouse(mens_singles, womens_singles):
    team()
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
def womens_singles_round_5(womens_singles):
    TEAM.draw(womens_singles, '5.1').matchup(1, women.Noskova, 2, women.Yastremska).select()  # (   ) Linda Noskova  OR  (  Q) Dayana Yastremska
    TEAM.draw(womens_singles, '5.2').matchup(1, women.Zheng, 2, women.Kalinskaya).select()  # ( 12) Qinwen Zheng  OR  (   ) Anna Kalinskaya
    TEAM.draw(womens_singles, '5.3').matchup(1, women.Kostyuk, 2, women.Gauff).select()  # (   ) Marta Kostyuk  OR  (  4) Coco Gauff
    TEAM.draw(womens_singles, '5.4').matchup(1, women.Krejcikova, 2, women.Sabalenka).select()  # (  9) Barbora Krejcikova  OR  (  2) Aryna Sabalenka
# womens_singles_round_5:END


# mens_singles_round_5:START
def mens_singles_round_5(mens_singles):
    TEAM.draw(mens_singles, '5.1').matchup(1, men.Djokovic, 2, men.Fritz).select()  # (  1) Novak Djokovic  OR  ( 12) Taylor Fritz
    TEAM.draw(mens_singles, '5.2').matchup(1, men.Sinner, 2, men.Rublev).select()  # (  4) Jannik Sinner  OR  (  5) Andrey Rublev
    TEAM.draw(mens_singles, '5.3').matchup(1, men.Medvedev, 2, men.Hurkacz).select()  # (  3) Daniil Medvedev  OR  (  9) Hubert Hurkacz
    TEAM.draw(mens_singles, '5.4').matchup(1, men.Zverev, 2, men.Alcaraz).select()  # (  6) Alexander Zverev  OR  (  2) Carlos Alcaraz
# mens_singles_round_5:END


# womens_singles_round_4:START
def womens_singles_round_4(womens_singles):
    TEAM.draw(womens_singles, '4.1').matchup(1, women.Svitolina, 2, women.Noskova).select(2,3)  # ( 19) Svitolina  OR  (   ) Linda Noskova
    TEAM.draw(womens_singles, '4.2').matchup(1, women.Yastremska, 2, women.Azarenka).select(1,3)  # (  Q) Dayana Yastremska  OR  ( 18) Victoria Azarenka
    TEAM.draw(womens_singles, '4.3').matchup(1, women.Paolini, 2, women.Kalinskaya).select(2,3)  # ( 26) Jasmine Paolini  OR  (   ) Anna Kalinskaya
    TEAM.draw(womens_singles, '4.4').matchup(1, women.Zheng, 2, women.Oceane_Dodin).select(1,3)  # ( 12) Qinwen Zheng  OR  (   ) Oceane Dodin
    TEAM.draw(womens_singles).match('4.5').winner(women.Kostyuk).in_sets(3)  # (   ) Marta Kostyuk  OR  (  Q) Maria Timofeeva
    TEAM.draw(womens_singles).match('4.6').winner(women.Frech).in_sets(3)  # (   ) Magdalena Frech  OR  (  4) Coco Gauff
    TEAM.draw(womens_singles).match('4.7').winner(women.Andreeva_Mirra).in_sets(3)  # (   ) Mirra Andreeva  OR  (  9) Barbora Krejcikova
    TEAM.draw(womens_singles).match('4.8').winner(women.Sabalenka).in_sets(3)  # (  2) Aryna Sabalenka  OR  (   ) Amanda Anisimova
# womens_singles_round_4:END


# mens_singles_round_4:START
def mens_singles_round_4(mens_singles):
    TEAM.draw(mens_singles).match('4.1').winner(men.Djokovic).in_sets(3)  # (  1) Novak Djokovic  OR  ( 20) Adrian Mannarino
    TEAM.draw(mens_singles).match('4.2').winner(men.Fritz).in_sets(4)  # ( 12) Taylor Fritz  OR  (  7) Stefanos Tsitsipas
    TEAM.draw(mens_singles).match('4.3').winner(men.Sinner).in_sets(5)  # (  4) Jannik Sinner  OR  ( 15) Karen Khachanov
    TEAM.draw(mens_singles).match('4.4').winner(men.Alex_de_Minaur).in_sets(5)  # (  5) Andrey Rublev  OR  ( 10) Alex de Minaur
    TEAM.draw(mens_singles, '4.5').matchup(1, men.Cazaux, 2, men.Hurkacz).select(2,4)  # ( WC) Arthur Cazaux  OR  (  9) Hubert Hurkacz
    TEAM.draw(mens_singles, '4.6').matchup(1, men.Medvedev, 2, men.Borges).select(1,5)  # (  3) Daniil Medvedev  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles, '4.7').matchup(1, men.Norrie, 2, men.Zverev).select(2,4)  # ( 19) Cameron Norrie  OR  (  6) Alexander Zverev
    TEAM.draw(mens_singles, '4.8').matchup(1, men.Kecmanovic, 2, men.Alcaraz).select(2,3)  # (   ) Miomir Kecmanovic  OR  (  2) Carlos Alcaraz
# mens_singles_round_4:END


# womens_singles_round_3:START
def womens_singles_round_3(womens_singles):
    TEAM.draw(womens_singles, '3.1').matchup(1, women.Swiatek, 2, women.Noskova).select(1,2)  # (  1) Iga Swiatek  OR  (   ) Linda Noskova
    TEAM.draw(womens_singles, '3.2').matchup(1, women.Svitolina, 2, women.Golubic).select(1,3)  # ( 19) Svitolina  OR  (   ) Viktorija Golubic
    TEAM.draw(womens_singles, '3.3').matchup(1, women.Azarenka, 2, women.Ostapenko).select(2,3)  # ( 18) Victoria Azarenka  OR  ( 11) Jelena Ostapenko
    TEAM.draw(womens_singles, '3.4').matchup(1, women.Yastremska, 2, women.Navarro).select(2,3)  # (  Q) Dayana Yastremska  OR  ( 27) Emma Navarro
    TEAM.draw(womens_singles, '3.5').matchup(1, women.Blinkova, 2, women.Paolini).select(2,3)  # (   ) Anna Blinkova  OR  ( 26) Jasmine Paolini
    TEAM.draw(womens_singles, '3.6').matchup(1, women.Kalinskaya, 2, women.Stephens).select(1,3)  # (   ) Anna Kalinskaya  OR  (   ) Sloane Stephens
    TEAM.draw(womens_singles, '3.7').matchup(1, women.Zheng, 2, women.Yafan_Wang).select(1,3)  # ( 12) Qinwen Zheng  OR  (   ) Yafan Wang
    TEAM.draw(womens_singles, '3.8').matchup(1, women.Oceane_Dodin, 2, women.Burel).select(1,3)  # (   ) Oceane Dodin  OR  (   ) Clara Burel
    TEAM.draw(womens_singles).match('3.9').winner(women.Avanesyan).in_sets(3)  # (   ) Elina Avanesyan  OR  (   ) Marta Kostyuk
    TEAM.draw(womens_singles).match('3.10').winner(women.Haddad_Maia).in_sets(2)  # ( 10) Beatriz Haddad Maia  OR  (  Q) Maria Timofeeva
    TEAM.draw(womens_singles).match('3.11').winner(women.Frech).in_sets(2)  # (   ) Magdalena Frech  OR  (  Q) Anastasia Zakharova
    TEAM.draw(womens_singles).match('3.12').winner(women.Gauff).in_sets(2)  # (   ) Alycia Parks  OR  (  4) Coco Gauff
    TEAM.draw(womens_singles).match('3.13').winner(women.Parry).in_sets(3)  # (   ) Mirra Andreeva  OR  (   ) Diane Parry
    TEAM.draw(womens_singles).match('3.14').winner(women.Krejcikova).in_sets(3)  # (  Q) Storm Hunter  OR  (  9) Barbora Krejcikova
    TEAM.draw(womens_singles).match('3.15').winner(women.Badosa).in_sets(3)  # (   ) Amanda Anisimova  OR  (   ) Paula Badosa
    TEAM.draw(womens_singles).match('3.16').winner(women.Sabalenka).in_sets(3)  # (  2) Aryna Sabalenka  OR  ( 28) Lesia Tsurenko
# womens_singles_round_3:END


# mens_singles_round_3:START
def mens_singles_round_3(mens_singles):
    TEAM.draw(mens_singles).match('3.1').winner(men.Djokovic).in_sets(5)  # ( 30) Tomas Martin Etcheverry  OR  (  1) Novak Djokovic
    TEAM.draw(mens_singles).match('3.2').winner(men.Shelton).in_sets(5)  # ( 20) Adrian Mannarino  OR  ( 16) Ben Shelton
    TEAM.draw(mens_singles).match('3.3').winner(men.Fritz).in_sets(4)  # ( 12) Taylor Fritz  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles).match('3.4').winner(men.Tsitsipas).in_sets(5)  # (   ) Luca Van Assche  OR  (  7) Stefanos Tsitsipas
    TEAM.draw(mens_singles).match('3.5').winner(men.Sinner).in_sets(4)  # (  4) Jannik Sinner  OR  ( 26) Sebastian Baez
    TEAM.draw(mens_singles).match('3.6').winner(men.Khachanov).in_sets(4)  # ( 15) Karen Khachanov  OR  (   ) Tomas Machac
    TEAM.draw(mens_singles).match('3.7').winner(men.Alex_de_Minaur).in_sets(4)  # (  Q) Flavio Cobolli  OR  ( 10) Alex de Minaur
    TEAM.draw(mens_singles).match('3.8').winner(men.Rublev).in_sets(4)  # (  5) Andrey Rublev  OR  ( 29) Sebastian Korda
    TEAM.draw(mens_singles, '3.9').matchup(1, men.Cazaux, 2, men.Griekspoor).select(1,5)  # ( WC) Arthur Cazaux  OR  ( 28) Tallon Griekspoor
    TEAM.draw(mens_singles, '3.10').matchup(1, men.Humbert, 2, men.Hurkacz).select(2,3)  # ( 21) Ugo Humbert  OR  (  9) Hubert Hurkacz
    TEAM.draw(mens_singles, '3.11').matchup(1, men.Borges, 2, men.Dimitrov).select(2,4)  # (   ) Nuno Borges  OR  ( 13) Grigor Dimitrov
    TEAM.draw(mens_singles, '3.12').matchup(1, men.Medvedev, 2, men.Auger_Aliassime).select(1,3)  # (  3) Daniil Medvedev  OR  ( 27) Felix Auger-Aliassime
    TEAM.draw(mens_singles, '3.13').matchup(1, men.Zverev, 2, men.Alex_Michelsen).select(1,4)  # (  6) Alexander Zverev  OR  (   ) Alex Michelsen
    TEAM.draw(mens_singles, '3.14').matchup(1, men.Ruud, 2, men.Norrie).select(1,5)  # ( 11) Casper Ruud  OR  ( 19) Cameron Norrie
    TEAM.draw(mens_singles, '3.15').matchup(1, men.Kecmanovic, 2, men.Paul).select(2,4)  # (   ) Miomir Kecmanovic  OR  ( 14) Tommy Paul
    TEAM.draw(mens_singles, '3.16').matchup(1, men.Shang, 2, men.Alcaraz).select(2,4)  # ( WC) Juncheng Shang  OR  (  2) Carlos Alcaraz
# mens_singles_round_3:END


# womens_singles_round_2:START
def womens_singles_round_2(womens_singles):
    TEAM.draw(womens_singles, '2.1').matchup(1, women.Swiatek, 2, women.Collins).select(1,2)  # (  1) Iga Swiatek  OR  (   ) Danielle Collins
    TEAM.draw(womens_singles).match('2.2').winner(women.Noskova).in_sets(3)  # ( WC) McCartney Kessler  OR  (   ) Linda Noskova
    TEAM.draw(womens_singles).match('2.3').winner(women.Svitolina).in_sets(2)  # (   ) Viktoriya Tomova  OR  ( 19) Svitolina
    TEAM.draw(womens_singles).match('2.4').winner(women.Golubic).in_sets(3)  # (   ) Viktorija Golubic  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles, '2.5').matchup(1, women.Ajla_Tomljanovic, 2, women.Ostapenko).select(2,2)  # (   ) Ajla Tomljanovic  OR  ( 11) Jelena Ostapenko
    TEAM.draw(womens_singles, '2.6').matchup(1, women.Azarenka, 2, women.Clara_Tauson).select(1,2)  # ( 18) Victoria Azarenka  OR  (   ) Clara Tauson
    TEAM.draw(womens_singles, '2.7').matchup(1, women.Cocciaretto, 2, women.Navarro).select(2,3)  # (   ) Elisabetta Cocciaretto  OR  ( 27) Emma Navarro
    TEAM.draw(womens_singles).match('2.8').winner(women.Gracheva).in_sets(2)  # (   ) Varvara Gracheva  OR  (  Q) Dayana Yastremska
    TEAM.draw(womens_singles, '2.9').matchup(1, women.Blinkova, 2, women.Rybakina).select(1,3)  # (   ) Anna Blinkova  OR  (  3) Elena Rybakina
    TEAM.draw(womens_singles).match('2.10').winner(women.Paolini).in_sets(2)  # (   ) Tatjana Maria  OR  ( 26) Jasmine Paolini
    TEAM.draw(womens_singles).match('2.11').winner(women.Rus).in_sets(3)  # (   ) Arantxa Rus  OR  (   ) Anna Kalinskaya
    TEAM.draw(womens_singles, '2.12').matchup(1, women.Kasatkina, 2, women.Stephens).select(1,3)  # ( 14) Daria Kasatkina  OR  (   ) Sloane Stephens
    TEAM.draw(womens_singles, '2.13').matchup(1, women.Boulter, 2, women.Zheng).select(2,2)  # (   ) Katie Boulter  OR  ( 12) Qinwen Zheng
    TEAM.draw(womens_singles, '2.14').matchup(1, women.Yafan_Wang, 2, women.Raducanu).select(2,3)  # (   ) Yafan Wang  OR  (   ) Emma Raducanu
    TEAM.draw(womens_singles, '2.15').matchup(1, women.Oceane_Dodin, 2, women.Trevisan).select(2,2)  # (   ) Oceane Dodin  OR  (   ) Martina Trevisan
    TEAM.draw(womens_singles, '2.16').matchup(1, women.Burel, 2, women.Pegula).select(2,2)  # (   ) Clara Burel  OR  (  5) Jessica Pegula
    TEAM.draw(womens_singles).match('2.17').winner(women.Sakkari).in_sets(2)  # (  8) Maria Sakkari  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles).match('2.18').winner(women.Mertens).in_sets(2)  # (   ) Marta Kostyuk  OR  ( 25) Elise Mertens
    TEAM.draw(womens_singles).match('2.19').winner(women.Caroline_Wozniacki).in_sets(3)  # ( WC) Caroline Wozniacki  OR  (  Q) Maria Timofeeva
    TEAM.draw(womens_singles).match('2.20').winner(women.Haddad_Maia).in_sets(3)  # ( 10) Beatriz Haddad Maia  OR  (  Q) Alina Korneeva
    TEAM.draw(womens_singles).match('2.21').winner(women.Garcia).in_sets(3)  # ( 16) Caroline Garcia  OR  (   ) Magdalena Frech
    TEAM.draw(womens_singles).match('2.22').winner(women.Juvan).in_sets(2)  # (  Q) Anastasia Zakharova  OR  (   ) Kaja Juvan
    TEAM.draw(womens_singles).match('2.23').winner(women.Parks).in_sets(3)  # (   ) Alycia Parks  OR  ( 32) Leylah Fernandez
    TEAM.draw(womens_singles).match('2.24').winner(women.Gauff).in_sets(2)  # (  4) Coco Gauff  OR  (   ) Caroline Dolehide
    TEAM.draw(womens_singles).match('2.25').winner(women.Jabeur).in_sets(2)  # (  6) Ons Jabeur  OR  (   ) Mirra Andreeva
    TEAM.draw(womens_singles).match('2.26').winner(women.Rakhimova).in_sets(2)  # (   ) Kamilla Rakhimova  OR  (   ) Diane Parry
    TEAM.draw(womens_singles).match('2.27').winner(women.Hunter).in_sets(3)  # (  Q) Storm Hunter  OR  (   ) Laura Siegemund
    TEAM.draw(womens_singles).match('2.28').winner(women.Krejcikova).in_sets(2)  # (   ) Tamara Korpatsch  OR  (  9) Barbora Krejcikova
    TEAM.draw(womens_singles).match('2.29').winner(women.Podoroska).in_sets(3)  # (   ) Nadia Podoroska  OR  (   ) Amanda Anisimova
    TEAM.draw(womens_singles).match('2.30').winner(women.Badosa).in_sets(3)  # (   ) Paula Badosa  OR  (   ) Anastasia Pavlyuchenkova
    TEAM.draw(womens_singles).match('2.31').winner(women.Tsurenko).in_sets(3)  # ( 28) Lesia Tsurenko  OR  (   ) Rebeka Masarova
    TEAM.draw(womens_singles).match('2.32').winner(women.Sabalenka).in_sets(2)  # (  Q) Brenda Fruhvirtova  OR  (  2) Aryna Sabalenka
# womens_singles_round_2:END


# mens_singles_round_2:START
def mens_singles_round_2(mens_singles):
    TEAM.draw(mens_singles).match('2.1').winner(men.Djokovic).in_sets(3)  # (   ) Alexei Popyrin  OR  (  1) Novak Djokovic
    TEAM.draw(mens_singles).match('2.2').winner(men.Monfils).in_sets(5)  # ( 30) Tomas Martin Etcheverry  OR  (   ) Gael Monfils
    TEAM.draw(mens_singles).match('2.3').winner(men.Mannarino).in_sets(4)  # ( 20) Adrian Mannarino  OR  (   ) Jaume Munar
    TEAM.draw(mens_singles).match('2.4').winner(men.Shelton).in_sets(4)  # ( 16) Ben Shelton  OR  (   ) Christopher O'Connell
    TEAM.draw(mens_singles).match('2.5').winner(men.Fritz).in_sets(3)  # ( 12) Taylor Fritz  OR  (   ) Hugo Gaston
    TEAM.draw(mens_singles).match('2.6').winner(men.Cerundolo_Francisco).in_sets(4)  # ( 22) Francisco Cerundolo  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles).match('2.7').winner(men.Musetti).in_sets(5)  # (   ) Luca Van Assche  OR  ( 25) Lorenzo Musetti
    TEAM.draw(mens_singles).match('2.8').winner(men.Tsitsipas).in_sets(4)  # (  7) Stefanos Tsitsipas  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles).match('2.9').winner(men.Sinner).in_sets(3)  # (  4) Jannik Sinner  OR  (  Q) Jesper de Jong
    TEAM.draw(mens_singles).match('2.10').winner(men.Baez).in_sets(4)  # (   ) Daniel Elahi Galan  OR  ( 26) Sebastian Baez
    TEAM.draw(mens_singles).match('2.11').winner(men.Tiafoe).in_sets(4)  # (   ) Tomas Machac  OR  ( 17) Frances Tiafoe
    TEAM.draw(mens_singles).match('2.12').winner(men.Khachanov).in_sets(3)  # ( 15) Karen Khachanov  OR  (  Q) Aleksandar Kovacevic
    TEAM.draw(mens_singles).match('2.13').winner(men.Alex_de_Minaur).in_sets(3)  # (   ) Matteo Arnaldi  OR  ( 10) Alex de Minaur
    TEAM.draw(mens_singles).match('2.14').winner(men.Kotov).in_sets(4)  # (   ) Pavel Kotov  OR  (  Q) Flavio Cobolli
    TEAM.draw(mens_singles).match('2.15').winner(men.Korda).in_sets(4)  # (   ) Quentin Halys  OR  ( 29) Sebastian Korda
    TEAM.draw(mens_singles).match('2.16').winner(men.Rublev).in_sets(3)  # (  5) Andrey Rublev  OR  (   ) Christopher Eubanks
    TEAM.draw(mens_singles, '2.17').matchup(1, men.Cazaux, 2, men.Rune).select(2,3)  # ( WC) Arthur Cazaux  OR  (  8) Holger Rune
    TEAM.draw(mens_singles, '2.18').matchup(1, men.Fils, 2, men.Griekspoor).select(2,5)  # (   ) Arthur Fils  OR  ( 28) Tallon Griekspoor
    TEAM.draw(mens_singles).match('2.19').winner(men.Humbert).in_sets(5)  # ( 21) Ugo Humbert  OR  (   ) Zhizhen Zhang
    TEAM.draw(mens_singles).match('2.20').winner(men.Hurkacz).in_sets(4)  # (  Q) Jakub Mensik  OR  (  9) Hubert Hurkacz
    TEAM.draw(mens_singles, '2.21').matchup(1, men.Kokkinakis, 2, men.Dimitrov).select(2,4)  # (   ) Thanasi Kokkinakis  OR  ( 13) Grigor Dimitrov
    TEAM.draw(mens_singles).match('2.22').winner(men.Davidovich_Fokina).in_sets(4)  # (   ) Nuno Borges  OR  ( 23) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles).match('2.23').winner(men.Auger_Aliassime).in_sets(3)  # ( 27) Felix Auger-Aliassime  OR  (  Q) Hugo Grenier
    TEAM.draw(mens_singles).match('2.24').winner(men.Medvedev).in_sets(4)  # (  3) Daniil Medvedev  OR  (   ) Emil Ruusuvuori
    TEAM.draw(mens_singles, '2.25').matchup(1, men.Zverev, 2, men.Lukas_Klein).select(1,3)  # (  6) Alexander Zverev  OR  (  Q) Lukas Klein
    TEAM.draw(mens_singles, '2.26').matchup(1, men.Alex_Michelsen, 2, men.Lehecka).select(1,4)  # (   ) Alex Michelsen  OR  ( 32) Jiri Lehecka
    TEAM.draw(mens_singles, '2.27').matchup(1, men.Norrie, 2, men.Zeppieri).select(1,4)  # ( 19) Cameron Norrie  OR  (  Q) Giulio Zeppieri
    TEAM.draw(mens_singles, '2.28').matchup(1, men.Purcell, 2, men.Ruud).select()  # (   ) Max Purcell  OR  ( 11) Casper Ruud
    TEAM.draw(mens_singles, '2.29').matchup(1, men.Draper, 2, men.Paul).select()  # (   ) Jack Draper  OR  ( 14) Tommy Paul
    TEAM.draw(mens_singles).match('2.30').winner(men.Kecmanovic).in_sets(4)  # ( 24) Jan-Lennard Struff  OR  (   ) Miomir Kecmanovic
    TEAM.draw(mens_singles, '2.31').matchup(1, men.Sumit_Nagal, 2, men.Shang).select(1,4)  # (  Q) Sumit Nagal  OR  ( WC) Juncheng Shang
    TEAM.draw(mens_singles, '2.32').matchup(1, men.Alcaraz, 2, men.Sonego).select(1,4)  # (  2) Carlos Alcaraz  OR  (   ) Lorenzo Sonego
# mens_singles_round_2:END


# womens_singles_round_1:START
def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles, '1.1').matchup(1, women.Swiatek, 2, women.Kenin).select(1,2)  # (  1) Iga Swiatek  OR  (   ) Sofia Kenin
    TEAM.draw(womens_singles, '1.2').matchup(1, women.Collins, 2, women.Angelique_Kerber).select(2,2)  # (   ) Danielle Collins  OR  (   ) Angelique Kerber
    TEAM.draw(womens_singles, '1.3').matchup(1, women.Fiona_Ferro, 2, women.McCartney_Kessler).select(1,3)  # (  Q) Fiona Ferro  OR  ( WC) McCartney Kessler
    TEAM.draw(womens_singles, '1.4').matchup(1, women.Noskova, 2, women.Bouzkova).select(2,2)  # (   ) Linda Noskova  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles, '1.5').matchup(1, women.Svitolina, 2, women.Taylah_Preston).select(1,2)  # ( 19) Svitolina  OR  ( WC) Taylah Preston
    TEAM.draw(womens_singles, '1.6').matchup(1, women.Kayla_Day, 2, women.Tomova).select(2,2)  # (   ) Kayla Day  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles, '1.7').matchup(1, women.Cristian, 2, women.Siniakova).select(1,3)  # (   ) Jaqueline Cristian  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles, '1.8').matchup(1, women.Golubic, 2, women.Kudermetova_Veronika).select(2,2)  # (   ) Viktorija Golubic  OR  ( 15) Veronika Kudermetova
    TEAM.draw(womens_singles, '1.9').matchup(1, women.Ostapenko, 2, women.Birrell).select(1,2)  # ( 11) Jelena Ostapenko  OR  ( WC) Kimberly Birrell
    TEAM.draw(womens_singles, '1.10').matchup(1, women.Martic, 2, women.Ajla_Tomljanovic).select(1,3)  # (   ) Petra Martic  OR  (   ) Ajla Tomljanovic
    TEAM.draw(womens_singles, '1.11').matchup(1, women.Minnen, 2, women.Clara_Tauson).select(1,2)  # (   ) Greet Minnen  OR  (   ) Clara Tauson
    TEAM.draw(womens_singles, '1.12').matchup(1, women.Giorgi, 2, women.Azarenka).select(2,2)  # (   ) Camila Giorgi  OR  ( 18) Victoria Azarenka
    TEAM.draw(womens_singles, '1.13').matchup(1, women.Navarro, 2, women.Wang_Xiyu).select(1,3)  # ( 27) Emma Navarro  OR  (   ) Xiyu Wang
    TEAM.draw(womens_singles, '1.14').matchup(1, women.Cocciaretto, 2, women.Lulu_Sun).select(1,2)  # (   ) Elisabetta Cocciaretto  OR  (  Q) Lulu Sun
    TEAM.draw(womens_singles, '1.15').matchup(1, women.Wickmayer, 2, women.Gracheva).select(1,2)  # (   ) Yanina Wickmayer  OR  (   ) Varvara Gracheva
    TEAM.draw(womens_singles, '1.16').matchup(1, women.Yastremska, 2, women.Vondrousova).select(2,2)  # (  Q) Dayana Yastremska  OR  (  7) Marketa Vondrousova
    TEAM.draw(womens_singles, '1.17').matchup(1, women.Rybakina, 2, women.Pliskova).select(1,2)  # (  3) Elena Rybakina  OR  (   ) Karolina Pliskova
    TEAM.draw(womens_singles, '1.18').matchup(1, women.Bucsa, 2, women.Blinkova).select(2,2)  # (   ) Cristina Bucsa  OR  (   ) Anna Blinkova
    TEAM.draw(womens_singles, '1.19').matchup(1, women.Maria, 2, women.Osorio).select(2,2)  # (   ) Tatjana Maria  OR  (   ) Camila Osorio
    TEAM.draw(womens_singles, '1.20').matchup(1, women.Shnaider, 2, women.Paolini).select(2,2)  # (   ) Diana Shnaider  OR  ( 26) Jasmine Paolini
    TEAM.draw(womens_singles, '1.21').matchup(1, women.Kalinina, 2, women.Rus).select(1,2)  # ( 24) Anhelina Kalinina  OR  (   ) Arantxa Rus
    TEAM.draw(womens_singles, '1.22').matchup(1, women.Kalinskaya, 2, women.Volynets).select(1,2)  # (   ) Anna Kalinskaya  OR  (  Q) Katie Volynets
    TEAM.draw(womens_singles, '1.23').matchup(1, women.Stephens, 2, women.Gadecki).select(1,3)  # (   ) Sloane Stephens  OR  ( WC) Olivia Gadecki
    TEAM.draw(womens_singles, '1.24').matchup(1, women.Stearns, 2, women.Kasatkina).select(2,2)  # (   ) Peyton Stearns  OR  ( 14) Daria Kasatkina
    TEAM.draw(womens_singles, '1.25').matchup(1, women.Zheng, 2, women.Krueger).select(1,2)  # ( 12) Qinwen Zheng  OR  (   ) Ashlyn Krueger
    TEAM.draw(womens_singles, '1.26').matchup(1, women.Boulter, 2, women.Yuan).select(1,3)  # (   ) Katie Boulter  OR  (   ) Yue Yuan
    TEAM.draw(womens_singles, '1.27').matchup(1, women.Raducanu, 2, women.Rogers).select(2,2)  # (   ) Emma Raducanu  OR  (   ) Shelby Rogers
    TEAM.draw(womens_singles, '1.28').matchup(1, women.Yafan_Wang, 2, women.Cirstea).select(2,2)  # (   ) Yafan Wang  OR  ( 22) Sorana Cirstea
    TEAM.draw(womens_singles, '1.29').matchup(1, women.Zhu, 2, women.Oceane_Dodin).select(1,2)  # ( 29) Lin Zhu  OR  (   ) Oceane Dodin
    TEAM.draw(womens_singles, '1.30').matchup(1, women.Renata_Zarazua, 2, women.Trevisan).select(2,2)  # (  Q) Renata Zarazua  OR  (   ) Martina Trevisan
    TEAM.draw(womens_singles, '1.31').matchup(1, women.Aleksandra_Krunic, 2, women.Burel).select(1,2)  # (   ) Aleksandra Krunic  OR  (   ) Clara Burel
    TEAM.draw(womens_singles, '1.32').matchup(1, women.Marino, 2, women.Pegula).select(2,2)  # (  Q) Rebecca Marino  OR  (  5) Jessica Pegula
    TEAM.draw(womens_singles, '1.33').matchup(1, women.Sakkari, 2, women.Hibino).select(1,2)  # (  8) Maria Sakkari  OR  (   ) Nao Hibino
    TEAM.draw(womens_singles, '1.34').matchup(1, women.Bai, 2, women.Avanesyan).select(1.2)  # (   ) Zhuoxuan Bai  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles, '1.35').matchup(1, women.Kostyuk, 2, women.Liu).select(1,2)  # (   ) Marta Kostyuk  OR  (   ) Claire Liu
    TEAM.draw(womens_singles, '1.36').matchup(1, women.Sherif, 2, women.Mertens).select(2,2)  # (   ) Mayar Sherif  OR  ( 25) Elise Mertens
    TEAM.draw(womens_singles, '1.37').matchup(1, women.Linette, 2, women.Caroline_Wozniacki).select(1,2)  # ( 20) Magda Linette  OR  ( WC) Caroline Wozniacki
    TEAM.draw(womens_singles, '1.38').matchup(1, women.Alizé_Cornet, 2, women.Maria_Timofeeva).select(2,3)  # ( WC) Alizé Cornet  OR  (  Q) Maria Timofeeva
    TEAM.draw(womens_singles, '1.39').matchup(1, women.Sorribes_Tormo, 2, women.Alina_Korneeva).select(1,2)  # (   ) Sorribes Tormo  OR  (  Q) Alina Korneeva
    TEAM.draw(womens_singles, '1.40').matchup(1, women.Fruhvirtova_Linda, 2, women.Haddad_Maia).select(2,2)  # (   ) Linda Fruhvirtova  OR  ( 10) Beatriz Haddad Maia
    TEAM.draw(womens_singles, '1.41').matchup(1, women.Garcia, 2, women.Naomi_Osaka).select(1,2)  # ( 16) Caroline Garcia  OR  (   ) Naomi Osaka
    TEAM.draw(womens_singles, '1.42').matchup(1, women.Frech, 2, women.Saville).select(1,2)  # (   ) Magdalena Frech  OR  ( WC) Daria Saville
    TEAM.draw(womens_singles, '1.43').matchup(1, women.Putintseva, 2, women.Anastasia_Zakharova).select(1,2)  # (   ) Yulia Putintseva  OR  (  Q) Anastasia Zakharova
    TEAM.draw(womens_singles, '1.44').matchup(1, women.Juvan, 2, women.Potapova).select(2,2)  # (   ) Kaja Juvan  OR  ( 23) Anastasia Potapova
    TEAM.draw(womens_singles, '1.45').matchup(1, women.Fernandez, 2, women.Bejlek).select(1,2)  # ( 32) Leylah Fernandez  OR  (  Q) Sara Bejlek
    TEAM.draw(womens_singles, '1.46').matchup(1, women.Parks, 2, women.Daria_Snigur).select(1,2)  # (   ) Alycia Parks  OR  (  Q) Daria Snigur
    TEAM.draw(womens_singles, '1.47').matchup(1, women.Dolehide, 2, women.Jeanjean).select(1,2)  # (   ) Caroline Dolehide  OR  (  Q) Leolia Jeanjean
    TEAM.draw(womens_singles, '1.48').matchup(1, women.Schmiedlova, 2, women.Gauff).select(2,2)  # (   ) Anna Karolina Schmiedlova  OR  (  4) Coco Gauff
    TEAM.draw(womens_singles, '1.49').matchup(1, women.Jabeur, 2, women.Yuliia_Starodubtseva).select(1,2)  # (  6) Ons Jabeur  OR  (  Q) Yuliia Starodubtseva
    TEAM.draw(womens_singles, '1.50').matchup(1, women.Andreeva_Mirra, 2, women.Pera).select(2,3)  # (   ) Mirra Andreeva  OR  (   ) Bernarda Pera
    TEAM.draw(womens_singles, '1.51').matchup(1, women.Rakhimova, 2, women.Emina_Bektas).select(2,3)  # (   ) Kamilla Rakhimova  OR  (   ) Emina Bektas
    TEAM.draw(womens_singles, '1.52').matchup(1, women.Parry, 2, women.Wang_Xinyu).select(2,3)  # (   ) Diane Parry  OR  ( 30) Xinyu Wang
    TEAM.draw(womens_singles, '1.53').matchup(1, women.Alexandrova, 2, women.Siegemund).select(1,2)  # ( 17) Ekaterina Alexandrova  OR  (   ) Laura Siegemund
    TEAM.draw(womens_singles, '1.54').matchup(1, women.Hunter, 2, women.Errani).select(2,3)  # (  Q) Storm Hunter  OR  (   ) Sara Errani
    TEAM.draw(womens_singles, '1.55').matchup(1, women.Korpatsch, 2, women.Burrage).select(1,3)  # (   ) Tamara Korpatsch  OR  (   ) Jodie Burrage
    TEAM.draw(womens_singles, '1.56').matchup(1, women.Mai_Hontama, 2, women.Krejcikova).select(2,2)  # ( WC) Mai Hontama  OR  (  9) Barbora Krejcikova
    TEAM.draw(womens_singles, '1.57').matchup(1, women.Samsonova, 2, women.Anisimova).select(1,2)  # ( 13) Liudmila Samsonova  OR  (   ) Amanda Anisimova
    TEAM.draw(womens_singles, '1.58').matchup(1, women.Podoroska, 2, women.Zidansek).select(2,2)  # (   ) Nadia Podoroska  OR  (   ) Tamara Zidansek
    TEAM.draw(womens_singles, '1.59').matchup(1, women.Townsend, 2, women.Badosa).select(2,3)  # (   ) Taylor Townsend  OR  (   ) Paula Badosa
    TEAM.draw(womens_singles, '1.60').matchup(1, women.Pavlyuchenkova, 2, women.Vekic).select(2,2)  # (   ) Anastasia Pavlyuchenkova  OR  ( 21) Donna Vekic
    TEAM.draw(womens_singles, '1.61').matchup(1, women.Tsurenko, 2, women.Bronzetti).select(1,2)  # ( 28) Lesia Tsurenko  OR  (   ) Lucia Bronzetti
    TEAM.draw(womens_singles, '1.62').matchup(1, women.Masarova, 2, women.Sasnovich).select(2,2)  # (   ) Rebeka Masarova  OR  (   ) Aliaksandra Sasnovich
    TEAM.draw(womens_singles, '1.63').matchup(1, women.Bogdan, 2, women.Fruhvirtova_Brenda).select(1,2)  # (   ) Ana Bogdan  OR  (  Q) Brenda Fruhvirtova
    TEAM.draw(womens_singles, '1.64').matchup(1, women.Ella_Seidel, 2, women.Sabalenka).select(2,2)  # (  Q) Ella Seidel  OR  (  2) Aryna Sabalenka

# womens_singles_round_1:END


# mens_singles_round_1:START
def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles, '1.1').matchup(1, men.Djokovic, 2, men.Dino_Prizmic).select(1,3)  # (  1) Novak Djokovic  OR  (  Q) Dino Prizmic
    TEAM.draw(mens_singles, '1.2').matchup(1, men.Popyrin, 2, men.Marc_Polmans).select(1,3)  # (   ) Alexei Popyrin  OR  ( WC) Marc Polmans
    TEAM.draw(mens_singles, '1.3').matchup(1, men.Hanfmann, 2, men.Monfils).select(2,4)  # (   ) Yannick Hanfmann  OR  (   ) Gael Monfils
    TEAM.draw(mens_singles, '1.4').matchup(1, men.Murray_Andy, 2, men.Etcheverry).select(1,4)  # (   ) Andy Murray  OR  ( 30) Tomas Martin Etcheverry
    TEAM.draw(mens_singles, '1.5').matchup(1, men.Mannarino, 2, men.Wawrinka).select(2,4)  # ( 20) Adrian Mannarino  OR  (   ) Stan Wawrinka
    TEAM.draw(mens_singles, '1.6').matchup(1, men.Shevchenko, 2, men.Munar).select(2,3)  # (   ) Alexander Shevchenko  OR  (   ) Jaume Munar
    TEAM.draw(mens_singles, '1.7').matchup(1, men.OConnell, 2, men.Garin).select(2,4)  # (   ) Christopher O'Connell  OR  (   ) Cristian Garin
    TEAM.draw(mens_singles, '1.8').matchup(1, men.Bautista_Agut, 2, men.Shelton).select(2,4)  # (   ) Roberto Bautista Agut  OR  ( 16) Ben Shelton
    TEAM.draw(mens_singles, '1.9').matchup(1, men.Fritz, 2, men.Facundo_Diaz_Acosta).select(1,3)  # ( 12) Taylor Fritz  OR  (   ) Facundo Diaz Acosta
    TEAM.draw(mens_singles, '1.10').matchup(1, men.Carballes_Baena, 2, men.Gaston).select(1,4)  # (   ) Roberto Carballes Baena  OR  (   ) Borna Gojo
    TEAM.draw(mens_singles, '1.11').matchup(1, men.Marozsan, 2, men.Marin_Cilic).select(2,4)  # (   ) Fabian Marozsan  OR  (   ) Marin Cilic
    TEAM.draw(mens_singles, '1.12').matchup(1, men.Dane_Sweeny, 2, men.Cerundolo_Francisco).select(1,3)  # (  Q) Dane Sweeny  OR  ( 22) Francisco Cerundolo
    TEAM.draw(mens_singles, '1.13').matchup(1, men.Musetti, 2, men.Bonzi).select(1,3)  # ( 25) Lorenzo Musetti  OR  (   ) Benjamin Bonzi
    TEAM.draw(mens_singles, '1.14').matchup(1, men.Duckworth, 2, men.Van_Assche).select(2,4)  # ( WC) James Duckworth  OR  (   ) Luca Van Assche
    TEAM.draw(mens_singles, '1.15').matchup(1, men.Vukic, 2, men.Thompson).select(2,4)  # (   ) Aleksandar Vukic  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles, '1.16').matchup(1, men.Bergs, 2, men.Tsitsipas).select(2,3)  # (   ) Matteo Berrettini  OR  (  7) Stefanos Tsitsipas
    TEAM.draw(mens_singles, '1.17').matchup(1, men.Sinner, 2, men.Botic_van_de_Zandschulp).select(1,3)  # (  4) Jannik Sinner  OR  (   ) Botic van de Zandschulp
    TEAM.draw(mens_singles, '1.18').matchup(1, men.de_Jong, 2, men.Cachin).select(2,4)  # (  Q) Jesper de Jong  OR  (   ) Pedro Cachin
    TEAM.draw(mens_singles, '1.19').matchup(1, men.Galan, 2, men.Kubler).select(1,3)  # (   ) Daniel Elahi Galan  OR  ( WC) Jason Kubler
    TEAM.draw(mens_singles, '1.20').matchup(1, men.Wolf, 2, men.Baez).select(2,4)  # (   ) J.J. Wolf  OR  ( 26) Sebastian Baez
    TEAM.draw(mens_singles, '1.21').matchup(1, men.Tiafoe, 2, men.Coric).select(1,3)  # ( 17) Frances Tiafoe  OR  (   ) Borna Coric
    TEAM.draw(mens_singles, '1.22').matchup(1, men.Machac, 2, men.Mochizuki).select(1,4)  # (   ) Tomas Machac  OR  ( LL) Shintaro Mochizuki
    TEAM.draw(mens_singles, '1.23').matchup(1, men.Tabilo, 2, men.Kovacevic).select(1,3)  # (   ) Alejandro Tabilo  OR  (  Q) Aleksandar Kovacevic
    TEAM.draw(mens_singles, '1.24').matchup(1, men.Altmaier, 2, men.Khachanov).select(2,3)  # (   ) Daniel Altmaier  OR  ( 15) Karen Khachanov
    TEAM.draw(mens_singles, '1.25').matchup(1, men.Alex_de_Minaur, 2, men.Raonic).select(1,3)  # ( 10) Alex de Minaur  OR  (   ) Milos Raonic
    TEAM.draw(mens_singles, '1.26').matchup(1, men.Arnaldi, 2, men.Adam_Walton).select(1,3)  # (   ) Matteo Arnaldi  OR  ( WC) Adam Walton
    TEAM.draw(mens_singles, '1.27').matchup(1, men.Kotov, 2, men.Rinderknech).select(2,4)  # (   ) Pavel Kotov  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles, '1.28').matchup(1, men.Flavio_Cobolli, 2, men.Jarry).select(2,3)  # (  Q) Flavio Cobolli  OR  ( 18) Nicolas Jarry
    TEAM.draw(mens_singles, '1.29').matchup(1, men.Korda, 2, men.Vit_Kopriva).select(1,4)  # ( 29) Sebastian Korda  OR  (  Q) Vit Kopriva
    TEAM.draw(mens_singles, '1.30').matchup(1, men.Halys, 2, men.Harris).select(1,4)  # (   ) Quentin Halys  OR  (  Q) Lloyd Harris
    TEAM.draw(mens_singles, '1.31').matchup(1, men.Eubanks, 2, men.Daniel).select(1,4)  # (   ) Christopher Eubanks  OR  (   ) Taro Daniel
    TEAM.draw(mens_singles, '1.32').matchup(1, men.Thiago_Seyboth_Wild, 2, men.Rublev).select(2,3)  # (   ) Thiago Seyboth Wild  OR  (  5) Andrey Rublev
    TEAM.draw(mens_singles, '1.33').matchup(1, men.Rune, 2, men.Nishioka).select(1,3)  # (  8) Holger Rune  OR  (   ) Yoshihito Nishioka
    TEAM.draw(mens_singles, '1.34').matchup(1, men.Djere, 2, men.Cazaux).select(1,4)  # (   ) Laslo Djere  OR  ( WC) Arthur Cazaux
    TEAM.draw(mens_singles, '1.35').matchup(1, men.Fils, 2, men.Vesely).select(2,4)  # (   ) Arthur Fils  OR  (   ) Jiri Vesely
    TEAM.draw(mens_singles, '1.36').matchup(1, men.Safiullin, 2, men.Griekspoor).select(2,4)  # (   ) Roman Safiullin  OR  ( 28) Tallon Griekspoor
    TEAM.draw(mens_singles, '1.37').matchup(1, men.Humbert, 2, men.Goffin).select(1,3)  # ( 21) Ugo Humbert  OR  (  Q) David Goffin
    TEAM.draw(mens_singles, '1.38').matchup(1, men.Zhang_Zhizhen, 2, men.Coria).select(2,4)  # (   ) Zhizhen Zhang  OR  (   ) Federico Coria
    TEAM.draw(mens_singles, '1.39').matchup(1, men.Shapovalov, 2, men.Jakub_Mensik).select(1,4)  # (   ) Denis Shapovalov  OR  (  Q) Jakub Mensik
    TEAM.draw(mens_singles, '1.40').matchup(1, men.Jasika, 2, men.Hurkacz).select(2,3)  # (  Q) Omar Jasika  OR  (  9) Hubert Hurkacz
    TEAM.draw(mens_singles, '1.41').matchup(1, men.Dimitrov, 2, men.Fucsovics).select(1,3)  # ( 13) Grigor Dimitrov  OR  (   ) Marton Fucsovics
    TEAM.draw(mens_singles, '1.42').matchup(1, men.Ofner, 2, men.Kokkinakis).select(1,4)  # (   ) Sebastian Ofner  OR  (   ) Thanasi Kokkinakis
    TEAM.draw(mens_singles, '1.43').matchup(1, men.Marterer, 2, men.Borges).select(1,4)  # (   ) Maximilian Marterer  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles, '1.44').matchup(1, men.Lestienne, 2, men.Davidovich_Fokina).select(2,4)  # (   ) Constant Lestienne  OR  ( 23) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles, '1.45').matchup(1, men.Auger_Aliassime, 2, men.Thiem).select(1,4)  # ( 27) Felix Auger-Aliassime  OR  (   ) Dominic Thiem
    TEAM.draw(mens_singles, '1.46').matchup(1, men.Muller, 2, men.Grenier).select(1,4)  # (   ) Alexandre Muller  OR  (  Q) Hugo Grenier
    TEAM.draw(mens_singles, '1.47').matchup(1, men.Kypson, 2, men.Ruusuvuori).select(2,3)  # ( WC) Patrick Kypson  OR  (   ) Emil Ruusuvuori
    TEAM.draw(mens_singles, '1.48').matchup(1, men.Terence_Atmane, 2, men.Medvedev).select(2,3)  # (  Q) Terence Atmane  OR  (  3) Daniil Medvedev
    TEAM.draw(mens_singles, '1.49').matchup(1, men.Zverev, 2, men.Koepfer).select(1,3)  # (  6) Alexander Zverev  OR  (   ) Dominik Koepfer
    TEAM.draw(mens_singles, '1.50').matchup(1, men.Soonwoo_Kwon, 2, men.Lukas_Klein).select(1,3)  # (   ) Soonwoo Kwon  OR  (  Q) Lukas Klein
    TEAM.draw(mens_singles, '1.51').matchup(1, men.James_McCabe, 2, men.Alex_Michelsen).select(2,4)  # ( WC) James McCabe  OR  (   ) Alex Michelsen
    TEAM.draw(mens_singles, '1.52').matchup(1, men.Zapata_Miralles, 2, men.Lehecka).select(2,4)  # (   ) Bernabe Zapata Miralles  OR  ( 32) Jiri Lehecka
    TEAM.draw(mens_singles, '1.53').matchup(1, men.Norrie, 2, men.Varillas).select(1,3)  # ( 19) Cameron Norrie  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles, '1.54').matchup(1, men.Lajovic, 2, men.Zeppieri).select(1,3)  # (   ) Dusan Lajovic  OR  (  Q) Giulio Zeppieri
    TEAM.draw(mens_singles, '1.55').matchup(1, men.Purcell, 2, men.Mate_Valkusz).select(1,4)  # (   ) Max Purcell  OR  (  Q) Mate Valkusz
    TEAM.draw(mens_singles, '1.56').matchup(1, men.Ramos_Vinolas, 2, men.Ruud).select(2,3)  # (   ) Albert Ramos-Vinolas  OR  ( 11) Casper Ruud
    TEAM.draw(mens_singles, '1.57').matchup(1, men.Paul, 2, men.Barrere).select(1,3)  # ( 14) Tommy Paul  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles, '1.58').matchup(1, men.Giron, 2, men.Draper).select(1,4)  # (   ) Marcos Giron  OR  (   ) Jack Draper
    TEAM.draw(mens_singles, '1.59').matchup(1, men.Kecmanovic, 2, men.Watanuki).select(2,4)  # (   ) Miomir Kecmanovic  OR  (   ) Yosuke Watanuki
    TEAM.draw(mens_singles, '1.60').matchup(1, men.Hijikata, 2, men.Struff).select(2,3)  # (   ) Rinky Hijikata  OR  ( 24) Jan-Lennard Struff
    TEAM.draw(mens_singles, '1.61').matchup(1, men.Bublik, 2, men.Sumit_Nagal).select(1,4)  # ( 31) Alexander Bublik  OR  (  Q) Sumit Nagal
    TEAM.draw(mens_singles, '1.62').matchup(1, men.Mcdonald, 2, men.Shang).select(1,4)  # (   ) Mackenzie McDonald  OR  ( WC) Juncheng Shang
    TEAM.draw(mens_singles, '1.63').matchup(1, men.Evans, 2, men.Sonego).select(2,4)  # (   ) Daniel Evans  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles, '1.64').matchup(1, men.Gasquet, 2, men.Alcaraz).select(2,3)  # (   ) Richard Gasquet  OR  (  2) Carlos Alcaraz

# mens_singles_round_1:END














