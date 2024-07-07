import sys
from tejos import model
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women
from tejos.players.wta_players import *
from tejos.players.atp_players import *

this = sys.modules[__name__]

TEAM = None

def team():
    this.TEAM = model.Team.get('Polar Precision')


def team_polar_precision(mens_singles, womens_singles):
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


#womens_singles_round_5:START

#womens_singles_round_5:END

#mens_singles_round_5:START

#mens_singles_round_5:END


# womens_singles_round_4:START

# womens_singles_round_4:END


# mens_singles_round_4:START

# mens_singles_round_4:END


# womens_singles_round_3:START

# womens_singles_round_3:END


# mens_singles_round_3:START

# mens_singles_round_3:END


# womens_singles_round_2:START
def womens_singles_round_2(womens_singles):
    TEAM.draw(womens_singles, '2.1').matchup(1, women.Swiatek, 2, women.Martic).select(1,2)  # (  1) Iga Swiatek  OR  (   ) Petra Martic
    TEAM.draw(womens_singles, '2.2').matchup(1, women.Putintseva, 2, women.Siniakova).select(2,3)  # (   ) Yulia Putintseva  OR  ( 27) Katerina Siniakova
    TEAM.draw(womens_singles, '2.3').matchup(1, women.Garcia, 2, women.Pera).select(1,2)  # ( 23) Caroline Garcia  OR  (   ) Bernarda Pera
    TEAM.draw(womens_singles, '2.4').matchup(1, women.Daria_Snigur, 2, women.Ostapenko).select(2,2)  # (  Q) Daria Snigur  OR  ( 13) Jelena Ostapenko
    TEAM.draw(womens_singles, '2.5').matchup(1, women.Collins, 2, women.Galfi).select(1,2)  # ( 11) Danielle Collins  OR  (  Q) Dalma Galfi
    TEAM.draw(womens_singles, '2.6').matchup(1, women.Osorio, 2, women.Haddad_Maia).select(2,2)  # (   ) Camila Osorio  OR  ( 20) Beatriz Haddad Maia
    TEAM.draw(womens_singles, '2.7').matchup(1, women.Krejcikova, 2, women.Volynets).select(1,3)  # ( 31) Barbora Krejcikova  OR  (  Q) Katie Volynets
    TEAM.draw(womens_singles, '2.8').matchup(1, women.Bucsa, 2, women.Maneiro).select(1,3)  # (   ) Cristina Bucsa  OR  (   ) Jessica Bouzas Maneiro
    TEAM.draw(womens_singles, '2.9').matchup(1, women.Rybakina, 2, women.Siegemund).select(1,3)  # (  4) Elena Rybakina  OR  (   ) Laura Siegemund
    TEAM.draw(womens_singles, '2.10').matchup(1, women.Caroline_Wozniacki, 2, women.Fernandez).select(1,3)  # ( WC) Caroline Wozniacki  OR  ( 30) Leylah Fernandez
    TEAM.draw(womens_singles, '2.11').matchup(1, women.Kalinskaya, 2, women.Bouzkova).select(2,3)  # ( 17) Anna Kalinskaya  OR  (   ) Marie Bouzkova
    TEAM.draw(womens_singles, '2.12').matchup(1, women.Avanesyan, 2, women.Samsonova).select(2,2)  # (   ) Elina Avanesyan  OR  ( 15) Liudmila Samsonova
    TEAM.draw(womens_singles, '2.13').matchup(1, women.Jabeur, 2, women.Montgomery).select(1,2)  # ( 10) Ons Jabeur  OR  (  Q) Robin Montgomery
    TEAM.draw(womens_singles, '2.14').matchup(1, women.Niemeier, 2, women.Svitolina).select(2,2)  # (   ) Jule Niemeier  OR  ( 21) Svitolina
    TEAM.draw(womens_singles, '2.15').matchup(1, women.Boulter, 2, women.Dart).select(2,3)  # ( 32) Katie Boulter  OR  (   ) Harriet Dart
    TEAM.draw(womens_singles, '2.16').matchup(1, women.Wang_Xinyu, 2, women.Pegula).select(1,3)  # (   ) Xinyu Wang  OR  (  5) Jessica Pegula
    TEAM.draw(womens_singles, '2.17').matchup(1, women.Lulu_Sun, 2, women.Yuliia_Starodubtseva).select(1,3)  # (  Q) Lulu Sun  OR  (  Q) Yuliia Starodubtseva
    TEAM.draw(womens_singles, '2.18').matchup(1, women.Zhu, 2, women.Pavlyuchenkova).select(2,2)  # (   ) Lin Zhu  OR  ( 25) Anastasia Pavlyuchenkova
    TEAM.draw(womens_singles, '2.19').matchup(1, women.Raducanu, 2, women.Mertens).select(1,2)  # ( WC) Emma Raducanu  OR  (   ) Elise Mertens
    TEAM.draw(womens_singles, '2.20').matchup(1, women.Rus, 2, women.Sakkari).select(2,2)  # (   ) Arantxa Rus  OR  (  9) Maria Sakkari
    TEAM.draw(womens_singles, '2.21').matchup(1, women.Kasatkina, 2, women.Yuriko_Lily_Miyazaki).select(1,2)  # ( 14) Daria Kasatkina  OR  ( WC) Yuriko Lily Miyazaki
    TEAM.draw(womens_singles, '2.22').matchup(1, women.Badosa, 2, women.Fruhvirtova_Brenda).select(1,2)  # (   ) Paula Badosa  OR  (   ) Brenda Fruhvirtova
    TEAM.draw(womens_singles, '2.23').matchup(1, women.Yastremska, 2, women.Gracheva).select(1,2)  # ( 28) Dayana Yastremska  OR  (   ) Varvara Gracheva
    TEAM.draw(womens_singles, '2.24').matchup(1, women.Vekic, 2, women.Andreeva_Erika).select(1,2)  # (   ) Donna Vekic  OR  ( LL) Erika Andreeva
    TEAM.draw(womens_singles, '2.25').matchup(1, women.Paolini, 2, women.Minnen).select(1,2)  # (  7) Jasmine Paolini  OR  (   ) Greet Minnen
    TEAM.draw(womens_singles, '2.26').matchup(1, women.Andreescu, 2, women.Noskova).select(2,3)  # (   ) Bianca Andreescu  OR  ( 26) Linda Noskova
    TEAM.draw(womens_singles, '2.27').matchup(1, women.Kostyuk, 2, women.Saville).select(1,2)  # ( 18) Marta Kostyuk  OR  (   ) Daria Saville
    TEAM.draw(womens_singles, '2.28').matchup(1, women.Yafan_Wang, 2, women.Keys).select(2,2)  # (   ) Yafan Wang  OR  ( 12) Madison Keys
    TEAM.draw(womens_singles, '2.29').matchup(1, women.Stephens, 2, women.Shnaider).select(1,2)  # (   ) Sloane Stephens  OR  (   ) Diana Shnaider
    TEAM.draw(womens_singles, '2.30').matchup(1, women.Naomi_Osaka, 2, women.Navarro).select(1,2)  # ( WC) Naomi Osaka  OR  ( 19) Emma Navarro
    TEAM.draw(womens_singles, '2.31').matchup(1, women.Kartal, 2, women.Burel).select(2,2)  # (  Q) Sonay Kartal  OR  (   ) Clara Burel
    TEAM.draw(womens_singles, '2.32').matchup(1, women.Todoni, 2, women.Gauff).select(2,2)  # (  Q) Anca Todoni  OR  (  2) Coco Gauff
# womens_singles_round_2:END


# mens_singles_round_2:START
def mens_singles_round_2(mens_singles):
    TEAM.draw(mens_singles, '2.1').matchup(1, men.Sinner, 2, men.Berrettini).select(1,4)  # (  1) Jannik Sinner  OR  (   ) Matteo Berrettini
    TEAM.draw(mens_singles, '2.2').matchup(1, men.Kecmanovic, 2, men.Griekspoor).select(2,4)  # (   ) Miomir Kecmanovic  OR  ( 27) Tallon Griekspoor
    TEAM.draw(mens_singles, '2.3').matchup(1, men.Shapovalov, 2, men.Altmaier).select(1,4)  # (   ) Denis Shapovalov  OR  (   ) Daniel Altmaier
    TEAM.draw(mens_singles, '2.4').matchup(1, men.Harris, 2, men.Shelton).select(2,3)  # (  Q) Lloyd Harris  OR  ( 14) Ben Shelton
    TEAM.draw(mens_singles, '2.5').matchup(1, men.Dimitrov, 2, men.Shang).select(1,3)  # ( 10) Grigor Dimitrov  OR  (   ) Juncheng Shang
    TEAM.draw(mens_singles, '2.6').matchup(1, men.Wawrinka, 2, men.Monfils).select(2,3)  # (   ) Stan Wawrinka  OR  (   ) Gael Monfils
    TEAM.draw(mens_singles, '2.7').matchup(1, men.Zhang_Zhizhen, 2, men.Struff).select(1,4)  # ( 32) Zhizhen Zhang  OR  (   ) Jan-Lennard Struff
    TEAM.draw(mens_singles, '2.8').matchup(1, men.Muller, 2, men.Medvedev).select(2,3)  # (   ) Alexandre Muller  OR  (  5) Daniil Medvedev
    TEAM.draw(mens_singles, '2.9').matchup(1, men.Alcaraz, 2, men.Vukic).select(1,3)  # (  3) Carlos Alcaraz  OR  (   ) Aleksandar Vukic
    TEAM.draw(mens_singles, '2.10').matchup(1, men.Coric, 2, men.Tiafoe).select(2,4)  # (   ) Borna Coric  OR  ( 29) Frances Tiafoe
    TEAM.draw(mens_singles, '2.11').matchup(1, men.Nakashima, 2, men.Thompson).select(1,4)  # (   ) Brandon Nakashima  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles, '2.12').matchup(1, men.Botic_van_De_Zandschulp, 2, men.Humbert).select(2,4)  # (   ) Botic van De Zandschulp  OR  ( 16) Ugo Humbert
    TEAM.draw(mens_singles, '2.13').matchup(1, men.Paul, 2, men.Otto_Virtanen).select(1,3)  # ( 12) Tommy Paul  OR  (  Q) Otto Virtanen
    TEAM.draw(mens_singles, '2.14').matchup(1, men.Cazaux, 2, men.Bublik).select(2,4)  # (   ) Arthur Cazaux  OR  ( 23) Alexander Bublik
    TEAM.draw(mens_singles, '2.15').matchup(1, men.Sonego, 2, men.Bautista_Agut).select(2,5)  # (   ) Lorenzo Sonego  OR  (   ) Roberto Bautista Agut
    TEAM.draw(mens_singles, '2.16').matchup(1, men.Fognini, 2, men.Ruud).select(2,4)  # (   ) Fabio Fognini  OR  (  8) Casper Ruud
    TEAM.draw(mens_singles, '2.17').matchup(1, men.Comesana, 2, men.Adam_Walton).select(1,4)  # (   ) Francisco Comesana  OR  (   ) Adam Walton
    TEAM.draw(mens_singles, '2.18').matchup(1, men.Darderi, 2, men.Musetti).select(2,5)  # (   ) Luciano Darderi  OR  ( 25) Lorenzo Musetti
    TEAM.draw(mens_singles, '2.19').matchup(1, men.Perricard, 2, men.Nishioka).select(2,4)  # ( LL) Giovanni Mpetshi Perricard  OR  (   ) Yoshihito Nishioka
    TEAM.draw(mens_singles, '2.20').matchup(1, men.Ruusuvuori, 2, men.Tsitsipas).select(2,3)  # (   ) Emil Ruusuvuori  OR  ( 11) Stefanos Tsitsipas
    TEAM.draw(mens_singles, '2.21').matchup(1, men.Fritz, 2, men.Rinderknech).select(1,4)  # ( 13) Taylor Fritz  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles, '2.22').matchup(1, men.Flavio_Cobolli, 2, men.Tabilo).select(2,4)  # (   ) Flavio Cobolli  OR  ( 24) Alejandro Tabilo
    TEAM.draw(mens_singles, '2.23').matchup(1, men.Draper, 2, men.Norrie).select(2,3)  # ( 28) Jack Draper  OR  (   ) Cameron Norrie
    TEAM.draw(mens_singles, '2.24').matchup(1, men.Giron, 2, men.Zverev).select(2,3)  # (   ) Marcos Giron  OR  (  4) Alexander Zverev
    TEAM.draw(mens_singles, '2.25').matchup(1, men.Hurkacz, 2, men.Fils).select(1,4)  # (  7) Hubert Hurkacz  OR  (   ) Arthur Fils
    TEAM.draw(mens_singles, '2.26').matchup(1, men.Machac, 2, men.Safiullin).select(1,4)  # (   ) Tomas Machac  OR  (   ) Roman Safiullin
    TEAM.draw(mens_singles, '2.27').matchup(1, men.Kokkinakis, 2, men.Pouille).select(1,5)  # (   ) Thanasi Kokkinakis  OR  (  Q) Lucas Pouille
    TEAM.draw(mens_singles, '2.28').matchup(1, men.Munar, 2, men.Alex_de_Minaur).select(2,3)  # (   ) Jaume Munar  OR  (  9) Alex de Minaur
    TEAM.draw(mens_singles, '2.29').matchup(1, men.Rune, 2, men.Thiago_Seyboth_Wild).select(1,3)  # ( 15) Holger Rune  OR  (   ) Thiago Seyboth Wild
    TEAM.draw(mens_singles, '2.30').matchup(1, men.Halys, 2, men.Khachanov).select(2,3)  # (  Q) Quentin Halys  OR  ( 21) Karen Khachanov
    TEAM.draw(mens_singles, '2.31').matchup(1, men.Etcheverry, 2, men.Popyrin).select(1,4)  # ( 30) Tomas Martin Etcheverry  OR  (   ) Alexei Popyrin
    TEAM.draw(mens_singles, '2.32').matchup(1, men.Fearnley, 2, men.Djokovic).select(2,3)  # ( WC) Jacob Fearnley  OR  (  2) Novak Djokovic
# mens_singles_round_2:END



# womens_singles_round_1:START
def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles, '1.1').matchup(1, women.Swiatek, 2, women.Kenin).select(1,2)  # (  1) Iga Swiatek  OR  (   ) Sofia Kenin
    TEAM.draw(womens_singles, '1.2').matchup(1, women.Jones, 2, women.Martic).select(2,2)  # ( WC) Francesca Jones  OR  (   ) Petra Martic
    TEAM.draw(womens_singles, '1.3').matchup(1, women.Putintseva, 2, women.Angelique_Kerber).select(1,2)  # (   ) Yulia Putintseva  OR  ( WC) Angelique Kerber
    TEAM.draw(womens_singles, '1.4').matchup(1, women.Stakusic, 2, women.Siniakova).select(2,2)  # (  Q) Marina Stakusic  OR  ( 27) Katerina Siniakova
    TEAM.draw(womens_singles, '1.5').matchup(1, women.Garcia, 2, women.Blinkova).select(1,3)  # ( 23) Caroline Garcia  OR  (   ) Anna Blinkova
    TEAM.draw(womens_singles, '1.6').matchup(1, women.Pera, 2, women.Potapova).select(1,2)  # (   ) Bernarda Pera  OR  (   ) Anastasia Potapova
    TEAM.draw(womens_singles, '1.7').matchup(1, women.Oceane_Dodin, 2, women.Daria_Snigur).select(1,2)  # (   ) Oceane Dodin  OR  (  Q) Daria Snigur
    TEAM.draw(womens_singles, '1.8').matchup(1, women.Ajla_Tomljanovic, 2, women.Ostapenko).select(2,2)  # ( WC) Ajla Tomljanovic  OR  ( 13) Jelena Ostapenko
    TEAM.draw(womens_singles, '1.9').matchup(1, women.Collins, 2, women.Clara_Tauson).select(1,2)  # ( 11) Danielle Collins  OR  (   ) Clara Tauson
    TEAM.draw(womens_singles, '1.10').matchup(1, women.Sherif, 2, women.Galfi).select(1,3)  # (   ) Mayar Sherif  OR  (  Q) Dalma Galfi
    TEAM.draw(womens_singles, '1.11').matchup(1, women.Osorio, 2, women.Davis).select(1,2)  # (   ) Camila Osorio  OR  (   ) Lauren Davis
    TEAM.draw(womens_singles, '1.12').matchup(1, women.Frech, 2, women.Haddad_Maia).select(2,2)  # (   ) Magdalena Frech  OR  ( 20) Beatriz Haddad Maia
    TEAM.draw(womens_singles, '1.13').matchup(1, women.Krejcikova, 2, women.Kudermetova_Veronika).select(1,3)  # ( 31) Barbora Krejcikova  OR  (   ) Veronika Kudermetova
    TEAM.draw(womens_singles, '1.14').matchup(1, women.Carle, 2, women.Volynets).select(2,2)  # (   ) Maria Lourdes Carle  OR  (  Q) Katie Volynets
    TEAM.draw(womens_singles, '1.15').matchup(1, women.Bucsa, 2, women.Bogdan).select(1,3)  # (   ) Cristina Bucsa  OR  (   ) Ana Bogdan
    TEAM.draw(womens_singles, '1.16').matchup(1, women.Maneiro, 2, women.Vondrousova).select(2,2)  # (   ) Jessica Bouzas Maneiro  OR  (  6) Marketa Vondrousova
    TEAM.draw(womens_singles, '1.17').matchup(1, women.Rybakina, 2, women.Ruse).select(1,2)  # (  4) Elena Rybakina  OR  (  Q) Elena-Gabriela Ruse
    TEAM.draw(womens_singles, '1.18').matchup(1, women.Siegemund, 2, women.Baindl).select(1,2)  # (   ) Laura Siegemund  OR  (   ) Kateryna Baindl
    TEAM.draw(womens_singles, '1.19').matchup(1, women.Caroline_Wozniacki, 2, women.Parks).select(1,2)  # ( WC) Caroline Wozniacki  OR  (  Q) Alycia Parks
    TEAM.draw(womens_singles, '1.20').matchup(1, women.Bronzetti, 2, women.Fernandez).select(2,3)  # (   ) Lucia Bronzetti  OR  ( 30) Leylah Fernandez
    TEAM.draw(womens_singles, '1.21').matchup(1, women.Kalinskaya, 2, women.Udvardy).select(1,2)  # ( 17) Anna Kalinskaya  OR  (  Q) Panna Udvardy
    TEAM.draw(womens_singles, '1.22').matchup(1, women.Bouzkova, 2, women.Riera).select(1,2)  # (   ) Marie Bouzkova  OR  (   ) Julia Riera
    TEAM.draw(womens_singles, '1.23').matchup(1, women.Kalinina, 2, women.Avanesyan).select(1,2)  # (   ) Anhelina Kalinina  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles, '1.24').matchup(1, women.Masarova, 2, women.Samsonova).select(2,2)  # (   ) Rebeka Masarova  OR  ( 15) Liudmila Samsonova
    TEAM.draw(womens_singles, '1.25').matchup(1, women.Jabeur, 2, women.Uchijima).select(1,2)  # ( 10) Ons Jabeur  OR  (   ) Moyuka Uchijima
    TEAM.draw(womens_singles, '1.26').matchup(1, women.Montgomery, 2, women.Gadecki).select(1,3)  # (  Q) Robin Montgomery  OR  (  Q) Olivia Gadecki
    TEAM.draw(womens_singles, '1.27').matchup(1, women.Golubic, 2, women.Niemeier).select(2,2)  # (   ) Viktorija Golubic  OR  (   ) Jule Niemeier
    TEAM.draw(womens_singles, '1.28').matchup(1, women.Linette, 2, women.Svitolina).select(2,3)  # (   ) Magda Linette  OR  ( 21) Svitolina
    TEAM.draw(womens_singles, '1.29').matchup(1, women.Boulter, 2, women.Maria).select(1,3)  # ( 32) Katie Boulter  OR  (   ) Tatjana Maria
    TEAM.draw(womens_singles, '1.30').matchup(1, women.Dart, 2, women.Bai).select(1,3)  # (   ) Harriet Dart  OR  (  Q) Zhuoxuan Bai
    TEAM.draw(womens_singles, '1.31').matchup(1, women.Wang_Xinyu, 2, women.Tomova).select(1,2)  # (   ) Xinyu Wang  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles, '1.32').matchup(1, women.Krueger, 2, women.Pegula).select(2,2)  # (   ) Ashlyn Krueger  OR  (  5) Jessica Pegula
    TEAM.draw(womens_singles, '1.33').matchup(1, women.Zheng, 2, women.Lulu_Sun).select(1,2)  # (  8) Qinwen Zheng  OR  (  Q) Lulu Sun
    TEAM.draw(womens_singles, '1.34').matchup(1, women.Uytvanck, 2, women.Yuliia_Starodubtseva).select(1,2)  # (   ) Alison Van Uytvanck  OR  (  Q) Yuliia Starodubtseva
    TEAM.draw(womens_singles, '1.35').matchup(1, women.Begu, 2, women.Zhu).select(1,2)  # (   ) Irina-Camelia Begu  OR  (   ) Lin Zhu
    TEAM.draw(womens_singles, '1.36').matchup(1, women.Townsend, 2, women.Pavlyuchenkova).select(2,2)  # (   ) Taylor Townsend  OR  ( 25) Anastasia Pavlyuchenkova
    TEAM.draw(womens_singles, '1.37').matchup(1, women.Renata_Zarazua, 2, women.Raducanu).select(1,3)  # ( LL) Renata Zarazua  OR  ( WC) Emma Raducanu
    TEAM.draw(womens_singles, '1.38').matchup(1, women.Hibino, 2, women.Mertens).select(2,2)  # (   ) Nao Hibino  OR  (   ) Elise Mertens
    TEAM.draw(womens_singles, '1.39').matchup(1, women.Rus, 2, women.Yuan).select(1,2)  # (   ) Arantxa Rus  OR  (   ) Yue Yuan
    TEAM.draw(womens_singles, '1.40').matchup(1, women.McCartney_Kessler, 2, women.Sakkari).select(2,2)  # (  Q) McCartney Kessler  OR  (  9) Maria Sakkari
    TEAM.draw(womens_singles, '1.41').matchup(1, women.Kasatkina, 2, women.Zhang_Shuai).select(1,2)  # ( 14) Daria Kasatkina  OR  (   ) Shuai Zhang
    TEAM.draw(womens_singles, '1.42').matchup(1, women.Korpatsch, 2, women.Yuriko_Lily_Miyazaki).select(1,2)  # (   ) Tamara Korpatsch  OR  ( WC) Yuriko Lily Miyazaki
    TEAM.draw(womens_singles, '1.43').matchup(1, women.Badosa, 2, women.Muchova).select(2,3)  # (   ) Paula Badosa  OR  (   ) Karolina Muchova
    TEAM.draw(womens_singles, '1.44').matchup(1, women.Fruhvirtova_Brenda, 2, women.Andreeva_Mirra).select(2,3)  # (   ) Brenda Fruhvirtova  OR  ( 24) Mirra Andreeva
    TEAM.draw(womens_singles, '1.45').matchup(1, women.Yastremska, 2, women.Podoroska).select(1,3)  # ( 28) Dayana Yastremska  OR  (   ) Nadia Podoroska
    TEAM.draw(womens_singles, '1.46').matchup(1, women.Tsurenko, 2, women.Gracheva).select(1,2)  # (   ) Lesia Tsurenko  OR  (   ) Varvara Gracheva
    TEAM.draw(womens_singles, '1.47').matchup(1, women.Vekic, 2, women.Wang_Xiyu).select(1,2)  # (   ) Donna Vekic  OR  (   ) Xiyu Wang
    TEAM.draw(womens_singles, '1.48').matchup(1, women.Emina_Bektas, 2, women.Andreeva_Erika).select(1,3)  # (   ) Emina Bektas  OR  ( LL) Erika Andreeva
    TEAM.draw(womens_singles, '1.49').matchup(1, women.Paolini, 2, women.Sorribes_Tormo).select(1,2)  # (  7) Jasmine Paolini  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles, '1.50').matchup(1, women.Minnen, 2, women.Watson).select(1,2)  # (   ) Greet Minnen  OR  ( WC) Heather Watson
    TEAM.draw(womens_singles, '1.51').matchup(1, women.Andreescu, 2, women.Cristian).select(1,2)  # (   ) Bianca Andreescu  OR  (   ) Jaqueline Cristian
    TEAM.draw(womens_singles, '1.52').matchup(1, women.Errani, 2, women.Noskova).select(2,2)  # (   ) Sara Errani  OR  ( 26) Linda Noskova
    TEAM.draw(womens_singles, '1.53').matchup(1, women.Kostyuk, 2, women.Sramkova).select(1,2)  # ( 18) Marta Kostyuk  OR  (   ) Rebecca Sramkova
    TEAM.draw(womens_singles, '1.54').matchup(1, women.Saville, 2, women.Stearns).select(2,3)  # (   ) Daria Saville  OR  (   ) Peyton Stearns
    TEAM.draw(womens_singles, '1.55').matchup(1, women.Schmiedlova, 2, women.Yafan_Wang).select(2,2)  # (   ) Anna Karolina Schmiedlova  OR  (   ) Yafan Wang
    TEAM.draw(womens_singles, '1.56').matchup(1, women.Trevisan, 2, women.Keys).select(2,2)  # (   ) Martina Trevisan  OR  ( 12) Madison Keys
    TEAM.draw(womens_singles, '1.57').matchup(1, women.Elsa_Jacquemot, 2, women.Stephens).select(2,2)  # ( LL) Elsa Jacquemot  OR  (   ) Sloane Stephens
    TEAM.draw(womens_singles, '1.58').matchup(1, women.Pliskova, 2, women.Shnaider).select(2,2)  # (   ) Karolina Pliskova  OR  (   ) Diana Shnaider
    TEAM.draw(womens_singles, '1.59').matchup(1, women.Naomi_Osaka, 2, women.Parry).select(1,2)  # ( WC) Naomi Osaka  OR  (   ) Diane Parry
    TEAM.draw(womens_singles, '1.60').matchup(1, women.Qiang_Wang, 2, women.Navarro).select(2,2)  # (   ) Qiang Wang  OR  ( 19) Emma Navarro
    TEAM.draw(womens_singles, '1.61').matchup(1, women.Cirstea, 2, women.Kartal).select(2,3)  # ( 29) Sorana Cirstea  OR  (  Q) Sonay Kartal
    TEAM.draw(womens_singles, '1.62').matchup(1, women.Lys, 2, women.Burel).select(2,2)  # (  Q) Eva Lys  OR  (   ) Clara Burel
    TEAM.draw(womens_singles, '1.63').matchup(1, women.Danilovic, 2, women.Todoni).select(2,2)  # ( LL) Olga Danilovic  OR  (  Q) Anca Todoni
    TEAM.draw(womens_singles, '1.64').matchup(1, women.Dolehide, 2, women.Gauff).select(2,2)  # (   ) Caroline Dolehide  OR  (  2) Coco Gauff
# womens_singles_round_1:END


# mens_singles_round_1:START
def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles, '1.1').matchup(1, men.Sinner, 2, men.Hanfmann).select(1,4)  # (  1) Jannik Sinner  OR  (   ) Yannick Hanfmann
    TEAM.draw(mens_singles, '1.2').matchup(1, men.Berrettini, 2, men.Fucsovics).select(1,4)  # (   ) Matteo Berrettini  OR  (   ) Marton Fucsovics
    TEAM.draw(mens_singles, '1.3').matchup(1, men.Sumit_Nagal, 2, men.Kecmanovic).select(1,4)  # (   ) Sumit Nagal  OR  (   ) Miomir Kecmanovic
    TEAM.draw(mens_singles, '1.4').matchup(1, men.Galan, 2, men.Griekspoor).select(2,3)  # ( LL) Daniel Elahi Galan  OR  ( 27) Tallon Griekspoor
    TEAM.draw(mens_singles, '1.5').matchup(1, men.Jarry, 2, men.Shapovalov).select(1,3)  # ( 19) Nicolas Jarry  OR  (   ) Denis Shapovalov
    TEAM.draw(mens_singles, '1.6').matchup(1, men.Altmaier, 2, men.Fery).select(1,3)  # (   ) Daniel Altmaier  OR  ( WC) Arthur Fery
    TEAM.draw(mens_singles, '1.7').matchup(1, men.Harris, 2, men.Alex_Michelsen).select(2,3)  # (  Q) Lloyd Harris  OR  (   ) Alex Michelsen
    TEAM.draw(mens_singles, '1.8').matchup(1, men.Bellucci, 2, men.Shelton).select(2,3)  # (  Q) Mattia Bellucci  OR  ( 14) Ben Shelton
    TEAM.draw(mens_singles, '1.9').matchup(1, men.Dimitrov, 2, men.Lajovic).select(1,3)  # ( 10) Grigor Dimitrov  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles, '1.10').matchup(1, men.Garin, 2, men.Shang).select(2,3)  # (  Q) Cristian Garin  OR  (   ) Juncheng Shang
    TEAM.draw(mens_singles, '1.11').matchup(1, men.Wawrinka, 2, men.Broom).select(1,3)  # (   ) Stan Wawrinka  OR  ( WC) Charles Broom
    TEAM.draw(mens_singles, '1.12').matchup(1, men.Monfils, 2, men.Mannarino).select(1,4)  # (   ) Gael Monfils  OR  ( 22) Adrian Mannarino
    TEAM.draw(mens_singles, '1.13').matchup(1, men.Zhang_Zhizhen, 2, men.Janvier).select(1,4)  # ( 32) Zhizhen Zhang  OR  (  Q) Maxime Janvier
    TEAM.draw(mens_singles, '1.14').matchup(1, men.Struff, 2, men.Marozsan).select(1,4)  # (   ) Jan-Lennard Struff  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles, '1.15').matchup(1, men.Muller, 2, men.Gaston).select(1,4)  # (   ) Alexandre Muller  OR  (  Q) Hugo Gaston
    TEAM.draw(mens_singles, '1.16').matchup(1, men.Kovacevic, 2, men.Medvedev).select(2,3)  # (   ) Aleksandar Kovacevic  OR  (  5) Daniil Medvedev
    TEAM.draw(mens_singles, '1.17').matchup(1, men.Alcaraz, 2, men.Lajal).select(1,3)  # (  3) Carlos Alcaraz  OR  (  Q) Mark Lajal
    TEAM.draw(mens_singles, '1.18').matchup(1, men.Vukic, 2, men.Ofner).select(1,4)  # (   ) Aleksandar Vukic  OR  (   ) Sebastian Ofner
    TEAM.draw(mens_singles, '1.19').matchup(1, men.Coric, 2, men.Felipe_Meligeni_Alves).select(1,4)  # (   ) Borna Coric  OR  (  Q) Felipe Meligeni Alves
    TEAM.draw(mens_singles, '1.20').matchup(1, men.Arnaldi, 2, men.Tiafoe).select(2,4)  # (   ) Matteo Arnaldi  OR  ( 29) Frances Tiafoe
    TEAM.draw(mens_singles, '1.21').matchup(1, men.Baez, 2, men.Nakashima).select(1,3)  # ( 18) Sebastian Baez  OR  (   ) Brandon Nakashima
    TEAM.draw(mens_singles, '1.22').matchup(1, men.Kotov, 2, men.Thompson).select(1,3)  # (   ) Pavel Kotov  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles, '1.23').matchup(1, men.Botic_van_De_Zandschulp, 2, men.Broady).select(1,3)  # (   ) Botic van De Zandschulp  OR  ( WC) Liam Broady
    TEAM.draw(mens_singles, '1.24').matchup(1, men.Shevchenko, 2, men.Humbert).select(2,4)  # (   ) Alexander Shevchenko  OR  ( 16) Ugo Humbert
    TEAM.draw(mens_singles, '1.25').matchup(1, men.Paul, 2, men.Martinez).select(1,3)  # ( 12) Tommy Paul  OR  (   ) Pedro Martinez
    TEAM.draw(mens_singles, '1.26').matchup(1, men.Otto_Virtanen, 2, men.Purcell).select(2,4)  # (  Q) Otto Virtanen  OR  (   ) Max Purcell
    TEAM.draw(mens_singles, '1.27').matchup(1, men.Bergs, 2, men.Cazaux).select(2,4)  # (  Q) Zizou Bergs  OR  (   ) Arthur Cazaux
    TEAM.draw(mens_singles, '1.28').matchup(1, men.Jakub_Mensik, 2, men.Bublik).select(2,4)  # (   ) Jakub Mensik  OR  ( 23) Alexander Bublik
    TEAM.draw(mens_singles, '1.29').matchup(1, men.Navone, 2, men.Sonego).select(2,3)  # ( 31) Mariano Navone  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles, '1.30').matchup(1, men.Bautista_Agut, 2, men.Marterer).select(1,4)  # (   ) Roberto Bautista Agut  OR  (   ) Maximilian Marterer
    TEAM.draw(mens_singles, '1.31').matchup(1, men.Van_Assche, 2, men.Fognini).select(2,3)  # ( LL) Luca Van Assche  OR  (   ) Fabio Fognini
    TEAM.draw(mens_singles, '1.32').matchup(1, men.Bolt, 2, men.Ruud).select(2,3)  # (  Q) Alex Bolt  OR  (  8) Casper Ruud
    TEAM.draw(mens_singles, '1.33').matchup(1, men.Rublev, 2, men.Comesana).select(1,3)  # (  6) Andrey Rublev  OR  (   ) Francisco Comesana
    TEAM.draw(mens_singles, '1.34').matchup(1, men.Coria, 2, men.Adam_Walton).select(1,4)  # (   ) Federico Coria  OR  (   ) Adam Walton
    TEAM.draw(mens_singles, '1.35').matchup(1, men.Darderi, 2, men.Choinski).select(1,4)  # (   ) Luciano Darderi  OR  ( WC) Jan Choinski
    TEAM.draw(mens_singles, '1.36').matchup(1, men.Lestienne, 2, men.Musetti).select(2,4)  # (   ) Constant Lestienne  OR  ( 25) Lorenzo Musetti
    TEAM.draw(mens_singles, '1.37').matchup(1, men.Korda, 2, men.Perricard).select(1,3)  # ( 20) Sebastian Korda  OR  ( LL) Giovanni Mpetshi Perricard
    TEAM.draw(mens_singles, '1.38').matchup(1, men.Nishioka, 2, men.Borges).select(1,4)  # (   ) Yoshihito Nishioka  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles, '1.39').matchup(1, men.Ruusuvuori, 2, men.Mcdonald).select(1,5)  # (   ) Emil Ruusuvuori  OR  (   ) Mackenzie McDonald
    TEAM.draw(mens_singles, '1.40').matchup(1, men.Daniel, 2, men.Tsitsipas).select(2,3)  # (   ) Taro Daniel  OR  ( 11) Stefanos Tsitsipas
    TEAM.draw(mens_singles, '1.41').matchup(1, men.Fritz, 2, men.OConnell).select(1,3)  # ( 13) Taylor Fritz  OR  (   ) Christopher O'Connell
    TEAM.draw(mens_singles, '1.42').matchup(1, men.Kei_Nishikori, 2, men.Rinderknech).select(2,5)  # (   ) Kei Nishikori  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles, '1.43').matchup(1, men.Flavio_Cobolli, 2, men.Hijikata).select(1,4)  # (   ) Flavio Cobolli  OR  (   ) Rinky Hijikata
    TEAM.draw(mens_singles, '1.44').matchup(1, men.Evans, 2, men.Tabilo).select(1,3)  # (   ) Daniel Evans  OR  ( 24) Alejandro Tabilo
    TEAM.draw(mens_singles, '1.45').matchup(1, men.Draper, 2, men.Ymer_Elias).select(1,4)  # ( 28) Jack Draper  OR  (  Q) Elias Ymer
    TEAM.draw(mens_singles, '1.46').matchup(1, men.Norrie, 2, men.Facundo_Diaz_Acosta).select(1,3)  # (   ) Cameron Norrie  OR  (   ) Facundo Diaz Acosta
    TEAM.draw(mens_singles, '1.47').matchup(1, men.Searle, 2, men.Giron).select(2,4)  # ( WC) Henry Searle  OR  (   ) Marcos Giron
    TEAM.draw(mens_singles, '1.48').matchup(1, men.Carballes_Baena, 2, men.Zverev).select(2,3)  # (   ) Roberto Carballes Baena  OR  (  4) Alexander Zverev
    TEAM.draw(mens_singles, '1.49').matchup(1, men.Hurkacz, 2, men.Albot).select(1,3)  # (  7) Hubert Hurkacz  OR  (  Q) Radu Albot
    TEAM.draw(mens_singles, '1.50').matchup(1, men.Fils, 2, men.Stricker).select(1,4)  # (   ) Arthur Fils  OR  (   ) D.Stricker
    TEAM.draw(mens_singles, '1.51').matchup(1, men.Goffin, 2, men.Machac).select(2,3)  # ( LL) David Goffin  OR  (   ) Tomas Machac
    TEAM.draw(mens_singles, '1.52').matchup(1, men.Safiullin, 2, men.Cerundolo_Francisco).select(1,5)  # (   ) Roman Safiullin  OR  ( 26) Francisco Cerundolo
    TEAM.draw(mens_singles, '1.53').matchup(1, men.Auger_Aliassime, 2, men.Kokkinakis).select(2,5)  # ( 17) Felix Auger-Aliassime  OR  (   ) Thanasi Kokkinakis
    TEAM.draw(mens_singles, '1.54').matchup(1, men.Pouille, 2, men.Djere).select(1,3)  # (  Q) Lucas Pouille  OR  (   ) Laslo Djere
    TEAM.draw(mens_singles, '1.55').matchup(1, men.Munar, 2, men.Harris_B).select(1,4)  # (   ) Jaume Munar  OR  ( WC) Billy Harris
    TEAM.draw(mens_singles, '1.56').matchup(1, men.Duckworth, 2, men.Alex_de_Minaur).select(2,3)  # ( LL) James Duckworth  OR  (  9) Alex de Minaur
    TEAM.draw(mens_singles, '1.57').matchup(1, men.Rune, 2, men.Soonwoo_Kwon).select(1,3)  # ( 15) Holger Rune  OR  (   ) Soonwoo Kwon
    TEAM.draw(mens_singles, '1.58').matchup(1, men.Jubb, 2, men.Thiago_Seyboth_Wild).select(2,3)  # ( WC) Paul Jubb  OR  (   ) Thiago Seyboth Wild
    TEAM.draw(mens_singles, '1.59').matchup(1, men.Halys, 2, men.Eubanks).select(1,3)  # (  Q) Quentin Halys  OR  (   ) Christopher Eubanks
    TEAM.draw(mens_singles, '1.60').matchup(1, men.Karatsev, 2, men.Khachanov).select(2,4)  # (   ) Aslan Karatsev  OR  ( 21) Karen Khachanov
    TEAM.draw(mens_singles, '1.61').matchup(1, men.Etcheverry, 2, men.Nardi).select(1,4)  # ( 30) Tomas Martin Etcheverry  OR  (   ) Luca Nardi
    TEAM.draw(mens_singles, '1.62').matchup(1, men.Popyrin, 2, men.Monteiro).select(1,4)  # (   ) Alexei Popyrin  OR  (   ) Thiago Monteiro
    TEAM.draw(mens_singles, '1.63').matchup(1, men.Fearnley, 2, men.Mono_Canas).select(2,5)  # ( WC) Jacob Fearnley  OR  (  Q) Alejandro Moro Canas
    TEAM.draw(mens_singles, '1.64').matchup(1, men.Vit_Kopriva, 2, men.Djokovic).select(2,3)  # (  Q) Vit Kopriva  OR  (  2) Novak Djokovic
# mens_singles_round_1:END



