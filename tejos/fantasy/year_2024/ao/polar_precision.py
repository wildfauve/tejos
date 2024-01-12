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


# womens_singles_round_5:START



# womens_singles_round_5:END


# mens_singles_round_5:START

# mens_singles_round_5:END


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
    TEAM.draw(womens_singles, '1.2').matchup(1, women.Collins, 2, women.Angelique_Kerber).select()  # (   ) Danielle Collins  OR  (   ) Angelique Kerber
    TEAM.draw(womens_singles, '1.3').matchup(1, women.Fiona_Ferro, 2, women.McCartney_Kessler).select()  # (  Q) Fiona Ferro  OR  ( WC) McCartney Kessler
    TEAM.draw(womens_singles, '1.4').matchup(1, women.Noskova, 2, women.Bouzkova).select()  # (   ) Linda Noskova  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles, '1.5').matchup(1, women.Svitolina, 2, women.Taylah_Preston).select()  # ( 19) Svitolina  OR  ( WC) Taylah Preston
    TEAM.draw(womens_singles, '1.6').matchup(1, women.Kayla_Day, 2, women.Tomova).select()  # (   ) Kayla Day  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles, '1.7').matchup(1, women.Cristian, 2, women.Siniakova).select()  # (   ) Jaqueline Cristian  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles, '1.8').matchup(1, women.Golubic, 2, women.Kudermetova_Veronika).select()  # (   ) Viktorija Golubic  OR  ( 15) Veronika Kudermetova
    TEAM.draw(womens_singles, '1.9').matchup(1, women.Ostapenko, 2, women.Birrell).select()  # ( 11) Jelena Ostapenko  OR  ( WC) Kimberly Birrell
    TEAM.draw(womens_singles, '1.10').matchup(1, women.Martic, 2, women.Ajla_Tomljanovic).select()  # (   ) Petra Martic  OR  (   ) Ajla Tomljanovic
    TEAM.draw(womens_singles, '1.11').matchup(1, women.Minnen, 2, women.Clara_Tauson).select()  # (   ) Greet Minnen  OR  (   ) Clara Tauson
    TEAM.draw(womens_singles, '1.12').matchup(1, women.Giorgi, 2, women.Azarenka).select()  # (   ) Camila Giorgi  OR  ( 18) Victoria Azarenka
    TEAM.draw(womens_singles, '1.13').matchup(1, women.Navarro, 2, women.Wang_Xiyu).select()  # ( 27) Emma Navarro  OR  (   ) Xiyu Wang
    TEAM.draw(womens_singles, '1.14').matchup(1, women.Cocciaretto, 2, women.Lulu_Sun).select()  # (   ) Elisabetta Cocciaretto  OR  (  Q) Lulu Sun
    TEAM.draw(womens_singles, '1.15').matchup(1, women.Wickmayer, 2, women.Gracheva).select()  # (   ) Yanina Wickmayer  OR  (   ) Varvara Gracheva
    TEAM.draw(womens_singles, '1.16').matchup(1, women.Yastremska, 2, women.Vondrousova).select()  # (  Q) Dayana Yastremska  OR  (  7) Marketa Vondrousova
    TEAM.draw(womens_singles, '1.17').matchup(1, women.Rybakina, 2, women.Pliskova).select()  # (  3) Elena Rybakina  OR  (   ) Karolina Pliskova
    TEAM.draw(womens_singles, '1.18').matchup(1, women.Bucsa, 2, women.Blinkova).select()  # (   ) Cristina Bucsa  OR  (   ) Anna Blinkova
    TEAM.draw(womens_singles, '1.19').matchup(1, women.Maria, 2, women.Osorio).select()  # (   ) Tatjana Maria  OR  (   ) Camila Osorio
    TEAM.draw(womens_singles, '1.20').matchup(1, women.Shnaider, 2, women.Paolini).select()  # (   ) Diana Shnaider  OR  ( 26) Jasmine Paolini
    TEAM.draw(womens_singles, '1.21').matchup(1, women.Kalinina, 2, women.Rus).select()  # ( 24) Anhelina Kalinina  OR  (   ) Arantxa Rus
    TEAM.draw(womens_singles, '1.22').matchup(1, women.Kalinskaya, 2, women.Volynets).select()  # (   ) Anna Kalinskaya  OR  (  Q) Katie Volynets
    TEAM.draw(womens_singles, '1.23').matchup(1, women.Stephens, 2, women.Gadecki).select()  # (   ) Sloane Stephens  OR  ( WC) Olivia Gadecki
    TEAM.draw(womens_singles, '1.24').matchup(1, women.Stearns, 2, women.Kasatkina).select()  # (   ) Peyton Stearns  OR  ( 14) Daria Kasatkina
    TEAM.draw(womens_singles, '1.25').matchup(1, women.Zheng, 2, women.Krueger).select()  # ( 12) Qinwen Zheng  OR  (   ) Ashlyn Krueger
    TEAM.draw(womens_singles, '1.26').matchup(1, women.Boulter, 2, women.Yuan).select()  # (   ) Katie Boulter  OR  (   ) Yue Yuan
    TEAM.draw(womens_singles, '1.27').matchup(1, women.Raducanu, 2, women.Rogers).select()  # (   ) Emma Raducanu  OR  (   ) Shelby Rogers
    TEAM.draw(womens_singles, '1.28').matchup(1, women.Yafan_Wang, 2, women.Cirstea).select()  # (   ) Yafan Wang  OR  ( 22) Sorana Cirstea
    TEAM.draw(womens_singles, '1.29').matchup(1, women.Zhu, 2, women.Oceane_Dodin).select()  # ( 29) Lin Zhu  OR  (   ) Oceane Dodin
    TEAM.draw(womens_singles, '1.30').matchup(1, women.Renata_Zarazua, 2, women.Trevisan).select()  # (  Q) Renata Zarazua  OR  (   ) Martina Trevisan
    TEAM.draw(womens_singles, '1.31').matchup(1, women.Aleksandra_Krunic, 2, women.Burel).select()  # (   ) Aleksandra Krunic  OR  (   ) Clara Burel
    TEAM.draw(womens_singles, '1.32').matchup(1, women.Marino, 2, women.Pegula).select()  # (  Q) Rebecca Marino  OR  (  5) Jessica Pegula
    TEAM.draw(womens_singles, '1.33').matchup(1, women.Sakkari, 2, women.Hibino).select()  # (  8) Maria Sakkari  OR  (   ) Nao Hibino
    TEAM.draw(womens_singles, '1.34').matchup(1, women.Bai, 2, women.Avanesyan).select()  # (   ) Zhuoxuan Bai  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles, '1.35').matchup(1, women.Kostyuk, 2, women.Liu).select()  # (   ) Marta Kostyuk  OR  (   ) Claire Liu
    TEAM.draw(womens_singles, '1.36').matchup(1, women.Sherif, 2, women.Mertens).select()  # (   ) Mayar Sherif  OR  ( 25) Elise Mertens
    TEAM.draw(womens_singles, '1.37').matchup(1, women.Linette, 2, women.Caroline_Wozniacki).select()  # ( 20) Magda Linette  OR  ( WC) Caroline Wozniacki
    TEAM.draw(womens_singles, '1.38').matchup(1, women.Alizé_Cornet, 2, women.Maria_Timofeeva).select()  # ( WC) Alizé Cornet  OR  (  Q) Maria Timofeeva
    TEAM.draw(womens_singles, '1.39').matchup(1, women.Sorribes_Tormo, 2, women.Alina_Korneeva).select()  # (   ) Sorribes Tormo  OR  (  Q) Alina Korneeva
    TEAM.draw(womens_singles, '1.40').matchup(1, women.Fruhvirtova_Linda, 2, women.Haddad_Maia).select()  # (   ) Linda Fruhvirtova  OR  ( 10) Beatriz Haddad Maia
    TEAM.draw(womens_singles, '1.41').matchup(1, women.Garcia, 2, women.Naomi_Osaka).select()  # ( 16) Caroline Garcia  OR  (   ) Naomi Osaka
    TEAM.draw(womens_singles, '1.42').matchup(1, women.Frech, 2, women.Saville).select()  # (   ) Magdalena Frech  OR  ( WC) Daria Saville
    TEAM.draw(womens_singles, '1.43').matchup(1, women.Putintseva, 2, women.Anastasia_Zakharova).select()  # (   ) Yulia Putintseva  OR  (  Q) Anastasia Zakharova
    TEAM.draw(womens_singles, '1.44').matchup(1, women.Juvan, 2, women.Potapova).select()  # (   ) Kaja Juvan  OR  ( 23) Anastasia Potapova
    TEAM.draw(womens_singles, '1.45').matchup(1, women.Fernandez, 2, women.Bejlek).select()  # ( 32) Leylah Fernandez  OR  (  Q) Sara Bejlek
    TEAM.draw(womens_singles, '1.46').matchup(1, women.Parks, 2, women.Daria_Snigur).select()  # (   ) Alycia Parks  OR  (  Q) Daria Snigur
    TEAM.draw(womens_singles, '1.47').matchup(1, women.Dolehide, 2, women.Jeanjean).select()  # (   ) Caroline Dolehide  OR  (  Q) Leolia Jeanjean
    TEAM.draw(womens_singles, '1.48').matchup(1, women.Schmiedlova, 2, women.Gauff).select()  # (   ) Anna Karolina Schmiedlova  OR  (  4) Coco Gauff
    TEAM.draw(womens_singles, '1.49').matchup(1, women.Jabeur, 2, women.Yuliia_Starodubtseva).select()  # (  6) Ons Jabeur  OR  (  Q) Yuliia Starodubtseva
    TEAM.draw(womens_singles, '1.50').matchup(1, women.Andreeva_Mirra, 2, women.Pera).select()  # (   ) Mirra Andreeva  OR  (   ) Bernarda Pera
    TEAM.draw(womens_singles, '1.51').matchup(1, women.Rakhimova, 2, women.Emina_Bektas).select()  # (   ) Kamilla Rakhimova  OR  (   ) Emina Bektas
    TEAM.draw(womens_singles, '1.52').matchup(1, women.Parry, 2, women.Wang_Xinyu).select()  # (   ) Diane Parry  OR  ( 30) Xinyu Wang
    TEAM.draw(womens_singles, '1.53').matchup(1, women.Alexandrova, 2, women.Siegemund).select()  # ( 17) Ekaterina Alexandrova  OR  (   ) Laura Siegemund
    TEAM.draw(womens_singles, '1.54').matchup(1, women.Hunter, 2, women.Errani).select()  # (  Q) Storm Hunter  OR  (   ) Sara Errani
    TEAM.draw(womens_singles, '1.55').matchup(1, women.Korpatsch, 2, women.Burrage).select()  # (   ) Tamara Korpatsch  OR  (   ) Jodie Burrage
    TEAM.draw(womens_singles, '1.56').matchup(1, women.Mai_Hontama, 2, women.Krejcikova).select()  # ( WC) Mai Hontama  OR  (  9) Barbora Krejcikova
    TEAM.draw(womens_singles, '1.57').matchup(1, women.Samsonova, 2, women.Anisimova).select()  # ( 13) Liudmila Samsonova  OR  (   ) Amanda Anisimova
    TEAM.draw(womens_singles, '1.58').matchup(1, women.Podoroska, 2, women.Zidansek).select()  # (   ) Nadia Podoroska  OR  (   ) Tamara Zidansek
    TEAM.draw(womens_singles, '1.59').matchup(1, women.Townsend, 2, women.Badosa).select()  # (   ) Taylor Townsend  OR  (   ) Paula Badosa
    TEAM.draw(womens_singles, '1.60').matchup(1, women.Pavlyuchenkova, 2, women.Vekic).select()  # (   ) Anastasia Pavlyuchenkova  OR  ( 21) Donna Vekic
    TEAM.draw(womens_singles, '1.61').matchup(1, women.Tsurenko, 2, women.Bronzetti).select()  # ( 28) Lesia Tsurenko  OR  (   ) Lucia Bronzetti
    TEAM.draw(womens_singles, '1.62').matchup(1, women.Masarova, 2, women.Sasnovich).select()  # (   ) Rebeka Masarova  OR  (   ) Aliaksandra Sasnovich
    TEAM.draw(womens_singles, '1.63').matchup(1, women.Bogdan, 2, women.Fruhvirtova_Brenda).select()  # (   ) Ana Bogdan  OR  (  Q) Brenda Fruhvirtova
    TEAM.draw(womens_singles, '1.64').matchup(1, women.Ella_Seidel, 2, women.Sabalenka).select()  # (  Q) Ella Seidel  OR  (  2) Aryna Sabalenka
# womens_singles_round_1:END


# mens_singles_round_1:START
def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles, '1.1').matchup(1, men.Djokovic, 2, men.Dino_Prizmic).select()  # (  1) Novak Djokovic  OR  (  Q) Dino Prizmic
    TEAM.draw(mens_singles, '1.2').matchup(1, men.Popyrin, 2, men.Marc_Polmans).select()  # (   ) Alexei Popyrin  OR  ( WC) Marc Polmans
    TEAM.draw(mens_singles, '1.3').matchup(1, men.Hanfmann, 2, men.Monfils).select()  # (   ) Yannick Hanfmann  OR  (   ) Gael Monfils
    TEAM.draw(mens_singles, '1.4').matchup(1, men.Murray_Andy, 2, men.Etcheverry).select()  # (   ) Andy Murray  OR  ( 30) Tomas Martin Etcheverry
    TEAM.draw(mens_singles, '1.5').matchup(1, men.Mannarino, 2, men.Wawrinka).select()  # ( 20) Adrian Mannarino  OR  (   ) Stan Wawrinka
    TEAM.draw(mens_singles, '1.6').matchup(1, men.Shevchenko, 2, men.Munar).select()  # (   ) Alexander Shevchenko  OR  (   ) Jaume Munar
    TEAM.draw(mens_singles, '1.7').matchup(1, men.OConnell, 2, men.Garin).select()  # (   ) Christopher O'Connell  OR  (   ) Cristian Garin
    TEAM.draw(mens_singles, '1.8').matchup(1, men.Bautista_Agut, 2, men.Shelton).select()  # (   ) Roberto Bautista Agut  OR  ( 16) Ben Shelton
    TEAM.draw(mens_singles, '1.9').matchup(1, men.Fritz, 2, men.Facundo_Diaz_Acosta).select()  # ( 12) Taylor Fritz  OR  (   ) Facundo Diaz Acosta
    TEAM.draw(mens_singles, '1.10').matchup(1, men.Carballes_Baena, 2, men.Gojo).select()  # (   ) Roberto Carballes Baena  OR  (   ) Borna Gojo
    TEAM.draw(mens_singles, '1.11').matchup(1, men.Marozsan, 2, men.Marin_Cilic).select()  # (   ) Fabian Marozsan  OR  (   ) Marin Cilic
    TEAM.draw(mens_singles, '1.12').matchup(1, men.Dane_Sweeny, 2, men.Cerundolo_Francisco).select()  # (  Q) Dane Sweeny  OR  ( 22) Francisco Cerundolo
    TEAM.draw(mens_singles, '1.13').matchup(1, men.Musetti, 2, men.Bonzi).select()  # ( 25) Lorenzo Musetti  OR  (   ) Benjamin Bonzi
    TEAM.draw(mens_singles, '1.14').matchup(1, men.Duckworth, 2, men.Van_Assche).select()  # ( WC) James Duckworth  OR  (   ) Luca Van Assche
    TEAM.draw(mens_singles, '1.15').matchup(1, men.Vukic, 2, men.Thompson).select()  # (   ) Aleksandar Vukic  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles, '1.16').matchup(1, men.Berrettini, 2, men.Tsitsipas).select()  # (   ) Matteo Berrettini  OR  (  7) Stefanos Tsitsipas
    TEAM.draw(mens_singles, '1.17').matchup(1, men.Sinner, 2, men.Botic_van_de_Zandschulp).select()  # (  4) Jannik Sinner  OR  (   ) Botic van de Zandschulp
    TEAM.draw(mens_singles, '1.18').matchup(1, men.de_Jong, 2, men.Cachin).select()  # (  Q) Jesper de Jong  OR  (   ) Pedro Cachin
    TEAM.draw(mens_singles, '1.19').matchup(1, men.Galan, 2, men.Kubler).select()  # (   ) Daniel Elahi Galan  OR  ( WC) Jason Kubler
    TEAM.draw(mens_singles, '1.20').matchup(1, men.Wolf, 2, men.Baez).select()  # (   ) J.J. Wolf  OR  ( 26) Sebastian Baez
    TEAM.draw(mens_singles, '1.21').matchup(1, men.Tiafoe, 2, men.Coric).select()  # ( 17) Frances Tiafoe  OR  (   ) Borna Coric
    TEAM.draw(mens_singles, '1.22').matchup(1, men.Machac, 2, men.Mochizuki).select()  # (   ) Tomas Machac  OR  ( LL) Shintaro Mochizuki
    TEAM.draw(mens_singles, '1.23').matchup(1, men.Tabilo, 2, men.Kovacevic).select()  # (   ) Alejandro Tabilo  OR  (  Q) Aleksandar Kovacevic
    TEAM.draw(mens_singles, '1.24').matchup(1, men.Altmaier, 2, men.Khachanov).select()  # (   ) Daniel Altmaier  OR  ( 15) Karen Khachanov
    TEAM.draw(mens_singles, '1.25').matchup(1, men.Alex_de_Minaur, 2, men.Raonic).select()  # ( 10) Alex de Minaur  OR  (   ) Milos Raonic
    TEAM.draw(mens_singles, '1.26').matchup(1, men.Arnaldi, 2, men.Adam_Walton).select()  # (   ) Matteo Arnaldi  OR  ( WC) Adam Walton
    TEAM.draw(mens_singles, '1.27').matchup(1, men.Kotov, 2, men.Rinderknech).select()  # (   ) Pavel Kotov  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles, '1.28').matchup(1, men.Flavio_Cobolli, 2, men.Jarry).select()  # (  Q) Flavio Cobolli  OR  ( 18) Nicolas Jarry
    TEAM.draw(mens_singles, '1.29').matchup(1, men.Korda, 2, men.Vit_Kopriva).select()  # ( 29) Sebastian Korda  OR  (  Q) Vit Kopriva
    TEAM.draw(mens_singles, '1.30').matchup(1, men.Halys, 2, men.Harris).select()  # (   ) Quentin Halys  OR  (  Q) Lloyd Harris
    TEAM.draw(mens_singles, '1.31').matchup(1, men.Eubanks, 2, men.Daniel).select()  # (   ) Christopher Eubanks  OR  (   ) Taro Daniel
    TEAM.draw(mens_singles, '1.32').matchup(1, men.Thiago_Seyboth_Wild, 2, men.Rublev).select()  # (   ) Thiago Seyboth Wild  OR  (  5) Andrey Rublev
    TEAM.draw(mens_singles, '1.33').matchup(1, men.Rune, 2, men.Nishioka).select()  # (  8) Holger Rune  OR  (   ) Yoshihito Nishioka
    TEAM.draw(mens_singles, '1.34').matchup(1, men.Djere, 2, men.Cazaux).select()  # (   ) Laslo Djere  OR  ( WC) Arthur Cazaux
    TEAM.draw(mens_singles, '1.35').matchup(1, men.Fils, 2, men.Vesely).select()  # (   ) Arthur Fils  OR  (   ) Jiri Vesely
    TEAM.draw(mens_singles, '1.36').matchup(1, men.Safiullin, 2, men.Griekspoor).select()  # (   ) Roman Safiullin  OR  ( 28) Tallon Griekspoor
    TEAM.draw(mens_singles, '1.37').matchup(1, men.Humbert, 2, men.Goffin).select()  # ( 21) Ugo Humbert  OR  (  Q) David Goffin
    TEAM.draw(mens_singles, '1.38').matchup(1, men.Zhang_Zhizhen, 2, men.Coria).select()  # (   ) Zhizhen Zhang  OR  (   ) Federico Coria
    TEAM.draw(mens_singles, '1.39').matchup(1, men.Shapovalov, 2, men.Jakub_Mensik).select()  # (   ) Denis Shapovalov  OR  (  Q) Jakub Mensik
    TEAM.draw(mens_singles, '1.40').matchup(1, men.Jasika, 2, men.Hurkacz).select()  # (  Q) Omar Jasika  OR  (  9) Hubert Hurkacz
    TEAM.draw(mens_singles, '1.41').matchup(1, men.Dimitrov, 2, men.Fucsovics).select()  # ( 13) Grigor Dimitrov  OR  (   ) Marton Fucsovics
    TEAM.draw(mens_singles, '1.42').matchup(1, men.Ofner, 2, men.Kokkinakis).select()  # (   ) Sebastian Ofner  OR  (   ) Thanasi Kokkinakis
    TEAM.draw(mens_singles, '1.43').matchup(1, men.Marterer, 2, men.Borges).select()  # (   ) Maximilian Marterer  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles, '1.44').matchup(1, men.Lestienne, 2, men.Davidovich_Fokina).select()  # (   ) Constant Lestienne  OR  ( 23) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles, '1.45').matchup(1, men.Auger_Aliassime, 2, men.Thiem).select()  # ( 27) Felix Auger-Aliassime  OR  (   ) Dominic Thiem
    TEAM.draw(mens_singles, '1.46').matchup(1, men.Muller, 2, men.Grenier).select()  # (   ) Alexandre Muller  OR  (  Q) Hugo Grenier
    TEAM.draw(mens_singles, '1.47').matchup(1, men.Kypson, 2, men.Ruusuvuori).select()  # ( WC) Patrick Kypson  OR  (   ) Emil Ruusuvuori
    TEAM.draw(mens_singles, '1.48').matchup(1, men.Terence_Atmane, 2, men.Medvedev).select()  # (  Q) Terence Atmane  OR  (  3) Daniil Medvedev
    TEAM.draw(mens_singles, '1.49').matchup(1, men.Zverev, 2, men.Koepfer).select()  # (  6) Alexander Zverev  OR  (   ) Dominik Koepfer
    TEAM.draw(mens_singles, '1.50').matchup(1, men.Soonwoo_Kwon, 2, men.Lukas_Klein).select()  # (   ) Soonwoo Kwon  OR  (  Q) Lukas Klein
    TEAM.draw(mens_singles, '1.51').matchup(1, men.James_McCabe, 2, men.Alex_Michelsen).select()  # ( WC) James McCabe  OR  (   ) Alex Michelsen
    TEAM.draw(mens_singles, '1.52').matchup(1, men.Zapata_Miralles, 2, men.Lehecka).select()  # (   ) Bernabe Zapata Miralles  OR  ( 32) Jiri Lehecka
    TEAM.draw(mens_singles, '1.53').matchup(1, men.Norrie, 2, men.Varillas).select()  # ( 19) Cameron Norrie  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles, '1.54').matchup(1, men.Lajovic, 2, men.Zeppieri).select()  # (   ) Dusan Lajovic  OR  (  Q) Giulio Zeppieri
    TEAM.draw(mens_singles, '1.55').matchup(1, men.Purcell, 2, men.Mate_Valkusz).select()  # (   ) Max Purcell  OR  (  Q) Mate Valkusz
    TEAM.draw(mens_singles, '1.56').matchup(1, men.Ramos_Vinolas, 2, men.Ruud).select()  # (   ) Albert Ramos-Vinolas  OR  ( 11) Casper Ruud
    TEAM.draw(mens_singles, '1.57').matchup(1, men.Paul, 2, men.Barrere).select()  # ( 14) Tommy Paul  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles, '1.58').matchup(1, men.Giron, 2, men.Draper).select()  # (   ) Marcos Giron  OR  (   ) Jack Draper
    TEAM.draw(mens_singles, '1.59').matchup(1, men.Kecmanovic, 2, men.Watanuki).select()  # (   ) Miomir Kecmanovic  OR  (   ) Yosuke Watanuki
    TEAM.draw(mens_singles, '1.60').matchup(1, men.Hijikata, 2, men.Struff).select()  # (   ) Rinky Hijikata  OR  ( 24) Jan-Lennard Struff
    TEAM.draw(mens_singles, '1.61').matchup(1, men.Bublik, 2, men.Sumit_Nagal).select()  # ( 31) Alexander Bublik  OR  (  Q) Sumit Nagal
    TEAM.draw(mens_singles, '1.62').matchup(1, men.Mcdonald, 2, men.Shang).select()  # (   ) Mackenzie McDonald  OR  ( WC) Juncheng Shang
    TEAM.draw(mens_singles, '1.63').matchup(1, men.Evans, 2, men.Sonego).select()  # (   ) Daniel Evans  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles, '1.64').matchup(1, men.Gasquet, 2, men.Alcaraz).select()  # (   ) Richard Gasquet  OR  (  2) Carlos Alcaraz
# mens_singles_round_1:END


