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

# womens_singles_round_2:END


# mens_singles_round_2:START

# mens_singles_round_2:END




# womens_singles_round_1:START
def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles, '1.1').matchup(1, women.Swiatek, 2, women.Kenin).select()  # (  1) Iga Swiatek  OR  (   ) Sofia Kenin
    TEAM.draw(womens_singles, '1.2').matchup(1, women.Jones, 2, women.Martic).select()  # ( WC) Francesca Jones  OR  (   ) Petra Martic
    TEAM.draw(womens_singles, '1.3').matchup(1, women.Putintseva, 2, women.Angelique_Kerber).select()  # (   ) Yulia Putintseva  OR  ( WC) Angelique Kerber
    TEAM.draw(womens_singles, '1.4').matchup(1, women.Stakusic, 2, women.Siniakova).select()  # (  Q) Marina Stakusic  OR  ( 27) Katerina Siniakova
    TEAM.draw(womens_singles, '1.5').matchup(1, women.Garcia, 2, women.Blinkova).select()  # ( 23) Caroline Garcia  OR  (   ) Anna Blinkova
    TEAM.draw(womens_singles, '1.6').matchup(1, women.Pera, 2, women.Potapova).select()  # (   ) Bernarda Pera  OR  (   ) Anastasia Potapova
    TEAM.draw(womens_singles, '1.7').matchup(1, women.Oceane_Dodin, 2, women.Daria_Snigur).select()  # (   ) Oceane Dodin  OR  (  Q) Daria Snigur
    TEAM.draw(womens_singles, '1.8').matchup(1, women.Ajla_Tomljanovic, 2, women.Ostapenko).select()  # ( WC) Ajla Tomljanovic  OR  ( 13) Jelena Ostapenko
    TEAM.draw(womens_singles, '1.9').matchup(1, women.Collins, 2, women.Clara_Tauson).select()  # ( 11) Danielle Collins  OR  (   ) Clara Tauson
    TEAM.draw(womens_singles, '1.10').matchup(1, women.Sherif, 2, women.Galfi).select()  # (   ) Mayar Sherif  OR  (  Q) Dalma Galfi
    TEAM.draw(womens_singles, '1.11').matchup(1, women.Osorio, 2, women.Davis).select()  # (   ) Camila Osorio  OR  (   ) Lauren Davis
    TEAM.draw(womens_singles, '1.12').matchup(1, women.Frech, 2, women.Haddad_Maia).select()  # (   ) Magdalena Frech  OR  ( 20) Beatriz Haddad Maia
    TEAM.draw(womens_singles, '1.13').matchup(1, women.Krejcikova, 2, women.Kudermetova_Veronika).select()  # ( 31) Barbora Krejcikova  OR  (   ) Veronika Kudermetova
    TEAM.draw(womens_singles, '1.14').matchup(1, women.Carle, 2, women.Volynets).select()  # (   ) Maria Lourdes Carle  OR  (  Q) Katie Volynets
    TEAM.draw(womens_singles, '1.15').matchup(1, women.Bucsa, 2, women.Bogdan).select()  # (   ) Cristina Bucsa  OR  (   ) Ana Bogdan
    TEAM.draw(womens_singles, '1.16').matchup(1, women.Maneiro, 2, women.Vondrousova).select()  # (   ) Jessica Bouzas Maneiro  OR  (  6) Marketa Vondrousova
    TEAM.draw(womens_singles, '1.17').matchup(1, women.Rybakina, 2, women.Ruse).select()  # (  4) Elena Rybakina  OR  (  Q) Elena-Gabriela Ruse
    TEAM.draw(womens_singles, '1.18').matchup(1, women.Siegemund, 2, women.Baindl).select()  # (   ) Laura Siegemund  OR  (   ) Kateryna Baindl
    TEAM.draw(womens_singles, '1.19').matchup(1, women.Caroline_Wozniacki, 2, women.Parks).select()  # ( WC) Caroline Wozniacki  OR  (  Q) Alycia Parks
    TEAM.draw(womens_singles, '1.20').matchup(1, women.Bronzetti, 2, women.Fernandez).select()  # (   ) Lucia Bronzetti  OR  ( 30) Leylah Fernandez
    TEAM.draw(womens_singles, '1.21').matchup(1, women.Kalinskaya, 2, women.Udvardy).select()  # ( 17) Anna Kalinskaya  OR  (  Q) Panna Udvardy
    TEAM.draw(womens_singles, '1.22').matchup(1, women.Bouzkova, 2, women.Riera).select()  # (   ) Marie Bouzkova  OR  (   ) Julia Riera
    TEAM.draw(womens_singles, '1.23').matchup(1, women.Kalinina, 2, women.Avanesyan).select()  # (   ) Anhelina Kalinina  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles, '1.24').matchup(1, women.Masarova, 2, women.Samsonova).select()  # (   ) Rebeka Masarova  OR  ( 15) Liudmila Samsonova
    TEAM.draw(womens_singles, '1.25').matchup(1, women.Jabeur, 2, women.Uchijima).select()  # ( 10) Ons Jabeur  OR  (   ) Moyuka Uchijima
    TEAM.draw(womens_singles, '1.26').matchup(1, women.Montgomery, 2, women.Gadecki).select()  # (  Q) Robin Montgomery  OR  (  Q) Olivia Gadecki
    TEAM.draw(womens_singles, '1.27').matchup(1, women.Golubic, 2, women.Niemeier).select()  # (   ) Viktorija Golubic  OR  (   ) Jule Niemeier
    TEAM.draw(womens_singles, '1.28').matchup(1, women.Linette, 2, women.Svitolina).select()  # (   ) Magda Linette  OR  ( 21) Svitolina
    TEAM.draw(womens_singles, '1.29').matchup(1, women.Boulter, 2, women.Maria).select()  # ( 32) Katie Boulter  OR  (   ) Tatjana Maria
    TEAM.draw(womens_singles, '1.30').matchup(1, women.Dart, 2, women.Bai).select()  # (   ) Harriet Dart  OR  (  Q) Zhuoxuan Bai
    TEAM.draw(womens_singles, '1.31').matchup(1, women.Wang_Xinyu, 2, women.Tomova).select()  # (   ) Xinyu Wang  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles, '1.32').matchup(1, women.Krueger, 2, women.Pegula).select()  # (   ) Ashlyn Krueger  OR  (  5) Jessica Pegula
    TEAM.draw(womens_singles, '1.33').matchup(1, women.Zheng, 2, women.Lulu_Sun).select()  # (  8) Qinwen Zheng  OR  (  Q) Lulu Sun
    TEAM.draw(womens_singles, '1.34').matchup(1, women.Uytvanck, 2, women.Yuliia_Starodubtseva).select()  # (   ) Alison Van Uytvanck  OR  (  Q) Yuliia Starodubtseva
    TEAM.draw(womens_singles, '1.35').matchup(1, women.Begu, 2, women.Zhu).select()  # (   ) Irina-Camelia Begu  OR  (   ) Lin Zhu
    TEAM.draw(womens_singles, '1.36').matchup(1, women.Townsend, 2, women.Pavlyuchenkova).select()  # (   ) Taylor Townsend  OR  ( 25) Anastasia Pavlyuchenkova
    TEAM.draw(womens_singles, '1.37').matchup(1, women.Renata_Zarazua, 2, women.Raducanu).select()  # ( LL) Renata Zarazua  OR  ( WC) Emma Raducanu
    TEAM.draw(womens_singles, '1.38').matchup(1, women.Hibino, 2, women.Mertens).select()  # (   ) Nao Hibino  OR  (   ) Elise Mertens
    TEAM.draw(womens_singles, '1.39').matchup(1, women.Rus, 2, women.Yuan).select()  # (   ) Arantxa Rus  OR  (   ) Yue Yuan
    TEAM.draw(womens_singles, '1.40').matchup(1, women.McCartney_Kessler, 2, women.Sakkari).select()  # (  Q) McCartney Kessler  OR  (  9) Maria Sakkari
    TEAM.draw(womens_singles, '1.41').matchup(1, women.Kasatkina, 2, women.Zhang_Shuai).select()  # ( 14) Daria Kasatkina  OR  (   ) Shuai Zhang
    TEAM.draw(womens_singles, '1.42').matchup(1, women.Korpatsch, 2, women.Yuriko_Lily_Miyazaki).select()  # (   ) Tamara Korpatsch  OR  ( WC) Yuriko Lily Miyazaki
    TEAM.draw(womens_singles, '1.43').matchup(1, women.Badosa, 2, women.Muchova).select()  # (   ) Paula Badosa  OR  (   ) Karolina Muchova
    TEAM.draw(womens_singles, '1.44').matchup(1, women.Fruhvirtova_Brenda, 2, women.Andreeva_Mirra).select()  # (   ) Brenda Fruhvirtova  OR  ( 24) Mirra Andreeva
    TEAM.draw(womens_singles, '1.45').matchup(1, women.Yastremska, 2, women.Podoroska).select()  # ( 28) Dayana Yastremska  OR  (   ) Nadia Podoroska
    TEAM.draw(womens_singles, '1.46').matchup(1, women.Tsurenko, 2, women.Gracheva).select()  # (   ) Lesia Tsurenko  OR  (   ) Varvara Gracheva
    TEAM.draw(womens_singles, '1.47').matchup(1, women.Vekic, 2, women.Wang_Xiyu).select()  # (   ) Donna Vekic  OR  (   ) Xiyu Wang
    TEAM.draw(womens_singles, '1.48').matchup(1, women.Emina_Bektas, 2, women.Andreeva_Erika).select()  # (   ) Emina Bektas  OR  ( LL) Erika Andreeva
    TEAM.draw(womens_singles, '1.49').matchup(1, women.Paolini, 2, women.Sorribes_Tormo).select()  # (  7) Jasmine Paolini  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles, '1.50').matchup(1, women.Minnen, 2, women.Watson).select()  # (   ) Greet Minnen  OR  ( WC) Heather Watson
    TEAM.draw(womens_singles, '1.51').matchup(1, women.Andreescu, 2, women.Cristian).select()  # (   ) Bianca Andreescu  OR  (   ) Jaqueline Cristian
    TEAM.draw(womens_singles, '1.52').matchup(1, women.Errani, 2, women.Noskova).select()  # (   ) Sara Errani  OR  ( 26) Linda Noskova
    TEAM.draw(womens_singles, '1.53').matchup(1, women.Kostyuk, 2, women.Sramkova).select()  # ( 18) Marta Kostyuk  OR  (   ) Rebecca Sramkova
    TEAM.draw(womens_singles, '1.54').matchup(1, women.Saville, 2, women.Stearns).select()  # (   ) Daria Saville  OR  (   ) Peyton Stearns
    TEAM.draw(womens_singles, '1.55').matchup(1, women.Schmiedlova, 2, women.Yafan_Wang).select()  # (   ) Anna Karolina Schmiedlova  OR  (   ) Yafan Wang
    TEAM.draw(womens_singles, '1.56').matchup(1, women.Trevisan, 2, women.Keys).select()  # (   ) Martina Trevisan  OR  ( 12) Madison Keys
    TEAM.draw(womens_singles, '1.57').matchup(1, women.Elsa_Jacquemot, 2, women.Stephens).select()  # ( LL) Elsa Jacquemot  OR  (   ) Sloane Stephens
    TEAM.draw(womens_singles, '1.58').matchup(1, women.Pliskova, 2, women.Shnaider).select()  # (   ) Karolina Pliskova  OR  (   ) Diana Shnaider
    TEAM.draw(womens_singles, '1.59').matchup(1, women.Naomi_Osaka, 2, women.Parry).select()  # ( WC) Naomi Osaka  OR  (   ) Diane Parry
    TEAM.draw(womens_singles, '1.60').matchup(1, women.Qiang_Wang, 2, women.Navarro).select()  # (   ) Qiang Wang  OR  ( 19) Emma Navarro
    TEAM.draw(womens_singles, '1.61').matchup(1, women.Cirstea, 2, women.Kartal).select()  # ( 29) Sorana Cirstea  OR  (  Q) Sonay Kartal
    TEAM.draw(womens_singles, '1.62').matchup(1, women.Lys, 2, women.Burel).select()  # (  Q) Eva Lys  OR  (   ) Clara Burel
    TEAM.draw(womens_singles, '1.63').matchup(1, women.Danilovic, 2, women.Todoni).select()  # ( LL) Olga Danilovic  OR  (  Q) Anca Todoni
    TEAM.draw(womens_singles, '1.64').matchup(1, women.Dolehide, 2, women.Gauff).select()  # (   ) Caroline Dolehide  OR  (  2) Coco Gauff
# womens_singles_round_1:END


# mens_singles_round_1:START
def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles, '1.1').matchup(1, men.Sinner, 2, men.Hanfmann).select()  # (  1) Jannik Sinner  OR  (   ) Yannick Hanfmann
    TEAM.draw(mens_singles, '1.2').matchup(1, men.Berrettini, 2, men.Fucsovics).select()  # (   ) Matteo Berrettini  OR  (   ) Marton Fucsovics
    TEAM.draw(mens_singles, '1.3').matchup(1, men.Sumit_Nagal, 2, men.Kecmanovic).select()  # (   ) Sumit Nagal  OR  (   ) Miomir Kecmanovic
    TEAM.draw(mens_singles, '1.4').matchup(1, men.Galan, 2, men.Griekspoor).select()  # ( LL) Daniel Elahi Galan  OR  ( 27) Tallon Griekspoor
    TEAM.draw(mens_singles, '1.5').matchup(1, men.Jarry, 2, men.Shapovalov).select()  # ( 19) Nicolas Jarry  OR  (   ) Denis Shapovalov
    TEAM.draw(mens_singles, '1.6').matchup(1, men.Altmaier, 2, men.Fery).select()  # (   ) Daniel Altmaier  OR  ( WC) Arthur Fery
    TEAM.draw(mens_singles, '1.7').matchup(1, men.Harris, 2, men.Alex_Michelsen).select()  # (  Q) Lloyd Harris  OR  (   ) Alex Michelsen
    TEAM.draw(mens_singles, '1.8').matchup(1, men.Bellucci, 2, men.Shelton).select()  # (  Q) Mattia Bellucci  OR  ( 14) Ben Shelton
    TEAM.draw(mens_singles, '1.9').matchup(1, men.Dimitrov, 2, men.Lajovic).select()  # ( 10) Grigor Dimitrov  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles, '1.10').matchup(1, men.Garin, 2, men.Shang).select()  # (  Q) Cristian Garin  OR  (   ) Juncheng Shang
    TEAM.draw(mens_singles, '1.11').matchup(1, men.Wawrinka, 2, men.Broom).select()  # (   ) Stan Wawrinka  OR  ( WC) Charles Broom
    TEAM.draw(mens_singles, '1.12').matchup(1, men.Monfils, 2, men.Mannarino).select()  # (   ) Gael Monfils  OR  ( 22) Adrian Mannarino
    TEAM.draw(mens_singles, '1.13').matchup(1, men.Zhang_Zhizhen, 2, men.Janvier).select()  # ( 32) Zhizhen Zhang  OR  (  Q) Maxime Janvier
    TEAM.draw(mens_singles, '1.14').matchup(1, men.Struff, 2, men.Marozsan).select()  # (   ) Jan-Lennard Struff  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles, '1.15').matchup(1, men.Muller, 2, men.Gaston).select()  # (   ) Alexandre Muller  OR  (  Q) Hugo Gaston
    TEAM.draw(mens_singles, '1.16').matchup(1, men.Kovacevic, 2, men.Medvedev).select()  # (   ) Aleksandar Kovacevic  OR  (  5) Daniil Medvedev
    TEAM.draw(mens_singles, '1.17').matchup(1, men.Alcaraz, 2, men.Lajal).select()  # (  3) Carlos Alcaraz  OR  (  Q) Mark Lajal
    TEAM.draw(mens_singles, '1.18').matchup(1, men.Vukic, 2, men.Ofner).select()  # (   ) Aleksandar Vukic  OR  (   ) Sebastian Ofner
    TEAM.draw(mens_singles, '1.19').matchup(1, men.Coric, 2, men.Felipe_Meligeni_Alves).select()  # (   ) Borna Coric  OR  (  Q) Felipe Meligeni Alves
    TEAM.draw(mens_singles, '1.20').matchup(1, men.Arnaldi, 2, men.Tiafoe).select()  # (   ) Matteo Arnaldi  OR  ( 29) Frances Tiafoe
    TEAM.draw(mens_singles, '1.21').matchup(1, men.Baez, 2, men.Nakashima).select()  # ( 18) Sebastian Baez  OR  (   ) Brandon Nakashima
    TEAM.draw(mens_singles, '1.22').matchup(1, men.Kotov, 2, men.Thompson).select()  # (   ) Pavel Kotov  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles, '1.23').matchup(1, men.Botic_van_De_Zandschulp, 2, men.Broady).select()  # (   ) Botic van De Zandschulp  OR  ( WC) Liam Broady
    TEAM.draw(mens_singles, '1.24').matchup(1, men.Shevchenko, 2, men.Humbert).select()  # (   ) Alexander Shevchenko  OR  ( 16) Ugo Humbert
    TEAM.draw(mens_singles, '1.25').matchup(1, men.Paul, 2, men.Martinez).select()  # ( 12) Tommy Paul  OR  (   ) Pedro Martinez
    TEAM.draw(mens_singles, '1.26').matchup(1, men.Otto_Virtanen, 2, men.Purcell).select()  # (  Q) Otto Virtanen  OR  (   ) Max Purcell
    TEAM.draw(mens_singles, '1.27').matchup(1, men.Bergs, 2, men.Cazaux).select()  # (  Q) Zizou Bergs  OR  (   ) Arthur Cazaux
    TEAM.draw(mens_singles, '1.28').matchup(1, men.Jakub_Mensik, 2, men.Bublik).select()  # (   ) Jakub Mensik  OR  ( 23) Alexander Bublik
    TEAM.draw(mens_singles, '1.29').matchup(1, men.Navone, 2, men.Sonego).select()  # ( 31) Mariano Navone  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles, '1.30').matchup(1, men.Bautista_Agut, 2, men.Marterer).select()  # (   ) Roberto Bautista Agut  OR  (   ) Maximilian Marterer
    TEAM.draw(mens_singles, '1.31').matchup(1, men.Van_Assche, 2, men.Fognini).select()  # ( LL) Luca Van Assche  OR  (   ) Fabio Fognini
    TEAM.draw(mens_singles, '1.32').matchup(1, men.Bolt, 2, men.Ruud).select()  # (  Q) Alex Bolt  OR  (  8) Casper Ruud
    TEAM.draw(mens_singles, '1.33').matchup(1, men.Rublev, 2, men.Comesana).select()  # (  6) Andrey Rublev  OR  (   ) Francisco Comesana
    TEAM.draw(mens_singles, '1.34').matchup(1, men.Coria, 2, men.Adam_Walton).select()  # (   ) Federico Coria  OR  (   ) Adam Walton
    TEAM.draw(mens_singles, '1.35').matchup(1, men.Darderi, 2, men.Choinski).select()  # (   ) Luciano Darderi  OR  ( WC) Jan Choinski
    TEAM.draw(mens_singles, '1.36').matchup(1, men.Lestienne, 2, men.Musetti).select()  # (   ) Constant Lestienne  OR  ( 25) Lorenzo Musetti
    TEAM.draw(mens_singles, '1.37').matchup(1, men.Korda, 2, men.Perricard).select()  # ( 20) Sebastian Korda  OR  ( LL) Giovanni Mpetshi Perricard
    TEAM.draw(mens_singles, '1.38').matchup(1, men.Nishioka, 2, men.Borges).select()  # (   ) Yoshihito Nishioka  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles, '1.39').matchup(1, men.Ruusuvuori, 2, men.Mcdonald).select()  # (   ) Emil Ruusuvuori  OR  (   ) Mackenzie McDonald
    TEAM.draw(mens_singles, '1.40').matchup(1, men.Daniel, 2, men.Tsitsipas).select()  # (   ) Taro Daniel  OR  ( 11) Stefanos Tsitsipas
    TEAM.draw(mens_singles, '1.41').matchup(1, men.Fritz, 2, men.OConnell).select()  # ( 13) Taylor Fritz  OR  (   ) Christopher O'Connell
    TEAM.draw(mens_singles, '1.42').matchup(1, men.Kei_Nishikori, 2, men.Rinderknech).select()  # (   ) Kei Nishikori  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles, '1.43').matchup(1, men.Flavio_Cobolli, 2, men.Hijikata).select()  # (   ) Flavio Cobolli  OR  (   ) Rinky Hijikata
    TEAM.draw(mens_singles, '1.44').matchup(1, men.Evans, 2, men.Tabilo).select()  # (   ) Daniel Evans  OR  ( 24) Alejandro Tabilo
    TEAM.draw(mens_singles, '1.45').matchup(1, men.Draper, 2, men.Ymer_Elias).select()  # ( 28) Jack Draper  OR  (  Q) Elias Ymer
    TEAM.draw(mens_singles, '1.46').matchup(1, men.Norrie, 2, men.Facundo_Diaz_Acosta).select()  # (   ) Cameron Norrie  OR  (   ) Facundo Diaz Acosta
    TEAM.draw(mens_singles, '1.47').matchup(1, men.Searle, 2, men.Giron).select()  # ( WC) Henry Searle  OR  (   ) Marcos Giron
    TEAM.draw(mens_singles, '1.48').matchup(1, men.Carballes_Baena, 2, men.Zverev).select()  # (   ) Roberto Carballes Baena  OR  (  4) Alexander Zverev
    TEAM.draw(mens_singles, '1.49').matchup(1, men.Hurkacz, 2, men.Albot).select()  # (  7) Hubert Hurkacz  OR  (  Q) Radu Albot
    TEAM.draw(mens_singles, '1.50').matchup(1, men.Fils, 2, men.Stricker).select()  # (   ) Arthur Fils  OR  (   ) D.Stricker
    TEAM.draw(mens_singles, '1.51').matchup(1, men.Goffin, 2, men.Machac).select()  # ( LL) David Goffin  OR  (   ) Tomas Machac
    TEAM.draw(mens_singles, '1.52').matchup(1, men.Safiullin, 2, men.Cerundolo_Francisco).select()  # (   ) Roman Safiullin  OR  ( 26) Francisco Cerundolo
    TEAM.draw(mens_singles, '1.53').matchup(1, men.Auger_Aliassime, 2, men.Kokkinakis).select()  # ( 17) Felix Auger-Aliassime  OR  (   ) Thanasi Kokkinakis
    TEAM.draw(mens_singles, '1.54').matchup(1, men.Pouille, 2, men.Djere).select()  # (  Q) Lucas Pouille  OR  (   ) Laslo Djere
    TEAM.draw(mens_singles, '1.55').matchup(1, men.Munar, 2, men.Harris_B).select()  # (   ) Jaume Munar  OR  ( WC) Billy Harris
    TEAM.draw(mens_singles, '1.56').matchup(1, men.Duckworth, 2, men.Alex_de_Minaur).select()  # ( LL) James Duckworth  OR  (  9) Alex de Minaur
    TEAM.draw(mens_singles, '1.57').matchup(1, men.Rune, 2, men.Soonwoo_Kwon).select()  # ( 15) Holger Rune  OR  (   ) Soonwoo Kwon
    TEAM.draw(mens_singles, '1.58').matchup(1, men.Jubb, 2, men.Thiago_Seyboth_Wild).select()  # ( WC) Paul Jubb  OR  (   ) Thiago Seyboth Wild
    TEAM.draw(mens_singles, '1.59').matchup(1, men.Halys, 2, men.Eubanks).select()  # (  Q) Quentin Halys  OR  (   ) Christopher Eubanks
    TEAM.draw(mens_singles, '1.60').matchup(1, men.Karatsev, 2, men.Khachanov).select()  # (   ) Aslan Karatsev  OR  ( 21) Karen Khachanov
    TEAM.draw(mens_singles, '1.61').matchup(1, men.Etcheverry, 2, men.Nardi).select()  # ( 30) Tomas Martin Etcheverry  OR  (   ) Luca Nardi
    TEAM.draw(mens_singles, '1.62').matchup(1, men.Popyrin, 2, men.Monteiro).select()  # (   ) Alexei Popyrin  OR  (   ) Thiago Monteiro
    TEAM.draw(mens_singles, '1.63').matchup(1, men.Fearnley, 2, men.Mono_Canas).select()  # ( WC) Jacob Fearnley  OR  (  Q) Alejandro Moro Canas
    TEAM.draw(mens_singles, '1.64').matchup(1, men.Vit_Kopriva, 2, men.Djokovic).select()  # (  Q) Vit Kopriva  OR  (  2) Novak Djokovic
# mens_singles_round_1:END


