import sys

from tejos import model
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women
from tejos.players.wta_players import *
from tejos.players.atp_players import *


this = sys.modules[__name__]

TEAM = None

def team():
    this.TEAM = model.Team.get('Musical Bears')


def team_musical_bears(mens_singles, womens_singles):
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
def womens_singles_round_2(womens_singles):
    TEAM.draw(womens_singles, '2.1').matchup(1, women.Swiatek, 2, women.Saville).select(1,
                                                                                        2)  # (  1) Iga Swiatek  OR  (   ) Daria Saville
    TEAM.draw(womens_singles, '2.2').matchup(1, women.Davis, 2, women.Juvan).select(1,
                                                                                    3)  # (   ) Lauren Davis  OR  (  Q) Kaja Juvan
    TEAM.draw(womens_singles, '2.3').matchup(1, women.Ostapenko, 2, women.Avanesyan).select(1,
                                                                                            2)  # ( 20) Jelena Ostapenko  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles, '2.4').matchup(1, women.Wang_Xiyu, 2, women.Pera).select(1,
                                                                                       2)  # (   ) Xiyu Wang  OR  (   ) Bernarda Pera
    TEAM.draw(womens_singles, '2.5').matchup(1, women.Kvitova, 2, women.Caroline_Wozniacki).select(1,
                                                                                                   2)  # ( 11) Petra Kvitova  OR  ( WC) Caroline Wozniacki
    TEAM.draw(womens_singles, '2.6').matchup(1, women.Brady, 2, women.Linette).select(2,
                                                                                      2)  # (   ) Jennifer Brady  OR  ( 24) Magda Linette
    TEAM.draw(womens_singles, '2.7').matchup(1, women.Mertens, 2, women.Collins).select(1,
                                                                                        3)  # ( 32) Elise Mertens  OR  (   ) Danielle Collins
    TEAM.draw(womens_singles, '2.8').matchup(1, women.Andreeva_Mirra, 2, women.Gauff).select(2,
                                                                                             2)  # (   ) Mirra Andreeva  OR  (  6) Coco Gauff
    TEAM.draw(womens_singles, '2.9').matchup(1, women.Rybakina, 2, women.Ajla_Tomljanovic).select(1,
                                                                                                  2)  # (  4) Elena Rybakina  OR  (   ) Ajla Tomljanovic
    TEAM.draw(womens_singles, '2.10').matchup(1, women.Kalinskaya, 2, women.Cirstea).select(2,
                                                                                            3)  # (   ) Anna Kalinskaya  OR  ( 30) Sorana Cirstea
    TEAM.draw(womens_singles, '2.11').matchup(1, women.Azarenka, 2, women.Zhu).select(1,
                                                                                      3)  # ( 18) Victoria Azarenka  OR  (   ) Lin Zhu
    TEAM.draw(womens_singles, '2.12').matchup(1, women.Yuriko_Lily_Miyazaki, 2, women.Bencic).select(2,
                                                                                                     2)  # (  Q) Yuriko Lily Miyazaki  OR  ( 15) Belinda Bencic
    TEAM.draw(womens_singles, '2.13').matchup(1, women.Muchova, 2, women.Frech).select(1,
                                                                                       2)  # ( 10) Karolina Muchova  OR  (   ) Magdalena Frech
    TEAM.draw(womens_singles, '2.14').matchup(1, women.Townsend, 2, women.Haddad_Maia).select(2,
                                                                                              3)  # (   ) Taylor Townsend  OR  ( 19) Beatriz Haddad Maia
    TEAM.draw(womens_singles, '2.15').matchup(1, women.Sorribes_Tormo, 2, women.Wang_Xinyu).select(2,
                                                                                                   3)  # (   ) Sorribes Tormo  OR  (   ) Xinyu Wang
    TEAM.draw(womens_singles, '2.16').matchup(1, women.Schmiedlova, 2, women.Masarova).select(1,
                                                                                              3)  # (   ) Anna Karolina Schmiedlova  OR  (   ) Rebeka Masarova

    TEAM.draw(womens_singles, '2.17').matchup(1, women.Yafan_Wang, 2, women.Boulter).select(2, 2)  # (  Q) Yafan Wang  OR  (   ) Katie Boulter
    TEAM.draw(womens_singles, '2.18').matchup(1, women.Stearns, 2, women.Clara_Tauson).select(1, 3)  # (   ) Peyton Stearns  OR  (   ) Clara Tauson
    TEAM.draw(womens_singles, '2.19').matchup(1, women.Alexandrova, 2, women.Tsurenko).select(1, 2)  # ( 22) Ekaterina Alexandrova  OR  (   ) Lesia Tsurenko
    TEAM.draw(womens_singles, '2.20').matchup(1, women.Vondrousova, 2, women.Trevisan).select(1, 3)  # (  9) Marketa Vondrousova  OR  (   ) Martina Trevisan
    TEAM.draw(womens_singles, '2.21').matchup(1, women.Samsonova, 2, women.Korpatsch).select(1, 3)  # ( 14) Liudmila Samsonova  OR  (   ) Tamara Korpatsch
    TEAM.draw(womens_singles, '2.22').matchup(1, women.Wickmayer, 2, women.Keys).select(2, 2)  # ( LL) Yanina Wickmayer  OR  ( 17) Madison Keys
    TEAM.draw(womens_singles, '2.23').matchup(1, women.Svitolina, 2, women.Pavlyuchenkova).select(1, 2)  # ( 26) Svitolina  OR  (   ) Anastasia Pavlyuchenkova
    TEAM.draw(womens_singles, '2.24').matchup(1, women.Pegula, 2, women.Tig).select(1, 2)  # (  3) Jessica Pegula  OR  (   ) Patricia Maria Tig
    TEAM.draw(womens_singles, '2.25').matchup(1, women.Noskova, 2, None).select()  # (   ) Linda Noskova  OR  TBD
    TEAM.draw(womens_singles, '2.26').matchup(1, women.Martic, 2, women.Bouzkova).select(1, 3)  # (   ) Petra Martic  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles, '2.27').matchup(1, women.Zheng, 2, women.Kanepi).select(1, 2)  # ( 23) Qinwen Zheng  OR  (   ) Kaia Kanepi
    TEAM.draw(womens_singles, '2.28').matchup(1, women.Lys, 2, women.Bronzetti).select(2, 2)  # (  Q) Eva Lys  OR  (   ) Lucia Bronzetti
    TEAM.draw(womens_singles, '2.29').matchup(1, women.Kasatkina, 2, None).select()  # ( 13) Daria Kasatkina  OR  TBD
    TEAM.draw(womens_singles, '2.30').matchup(1, women.Minnen, 2, women.Sachia_Vickery).select(1, 3)  # (  Q) Greet Minnen  OR  (  Q) Sachia Vickery
    TEAM.draw(womens_singles, '2.31').matchup(1, women.Pliskova, 2, women.Burel).select(1, 3)  # ( 25) Karolina Pliskova  OR  (   ) Clara Burel
    TEAM.draw(womens_singles, '2.32').matchup(1, women.Burrage, 2, None).select()  # (   ) Jodie Burrage  OR  TBD
# womens_singles_round_2:END

    # mens_singles_round_2:START
def mens_singles_round_2(mens_singles):
    TEAM.draw(mens_singles, '2.1').matchup(1, men.Harris, 2, None).select()  # (   ) Lloyd Harris  OR  TBD
    TEAM.draw(mens_singles, '2.2').matchup(1, men.Evans, 2, None).select()  # ( 26) Daniel Evans  OR  TBD
    TEAM.draw(mens_singles, '2.3').matchup(1, men.Fils, 2, None).select()  # (   ) Arthur Fils  OR  TBD
    TEAM.draw(mens_singles, '2.4').matchup(1, men.Norrie, 2, men.Hsu).select(1,
                                                                             3)  # ( 16) Cameron Norrie  OR  (  Q) Yu Hsiou Hsu
    TEAM.draw(mens_singles, '2.5').matchup(1, men.Zverev, 2, men.Altmaier).select(1,
                                                                                  3)  # ( 12) Alexander Zverev  OR  (   ) Daniel Altmaier
    TEAM.draw(mens_singles, '2.6').matchup(1, men.Murray_Andy, 2, men.Dimitrov).select(1,
                                                                                       4)  # (   ) Andy Murray  OR  ( 19) Grigor Dimitrov
    TEAM.draw(mens_singles, '2.7').matchup(1, men.Wawrinka, 2, None).select()  # (   ) Stan Wawrinka  OR  TBD
    TEAM.draw(mens_singles, '2.8').matchup(1, men.Sonego, 2, men.Sinner).select(2,
                                                                                3)  # (   ) Lorenzo Sonego  OR  (  6) Jannik Sinner
    TEAM.draw(mens_singles, '2.9').matchup(1, men.Medvedev, 2, men.OConnell).select(1,
                                                                                    4)  # (  3) Daniil Medvedev  OR  (   ) Christopher O'Connell
    TEAM.draw(mens_singles, '2.10').matchup(1, men.Felipe_Meligeni_Alves, 2, men.Baez).select(2,
                                                                                              4)  # (  Q) Felipe Meligeni Alves  OR  (   ) Sebastian Baez
    TEAM.draw(mens_singles, '2.11').matchup(1, men.Jarry, 2, men.Alex_Michelsen).select(1,
                                                                                        4)  # ( 23) Nicolas Jarry  OR  ( WC) Alex Michelsen
    TEAM.draw(mens_singles, '2.12').matchup(1, men.Alex_de_Minaur, 2, men.Wu).select(1,
                                                                                     4)  # ( 13) Alex de Minaur  OR  (   ) Yibing Wu
    TEAM.draw(mens_singles, '2.13').matchup(1, men.Mmoh, 2, men.Isner).select(1,
                                                                              5)  # ( WC) Michael Mmoh  OR  ( WC) John Isner
    TEAM.draw(mens_singles, '2.14').matchup(1, men.Draper, 2, men.Hurkacz).select(2,
                                                                                  4)  # (   ) Jack Draper  OR  ( 17) Hubert Hurkacz
    TEAM.draw(mens_singles, '2.15').matchup(1, men.Berrettini, 2, men.Rinderknech).select(1,
                                                                                          4)  # (   ) Matteo Berrettini  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles, '2.16').matchup(1, men.Rublev, 2, men.Monfils).select(1,
                                                                                  4)  # (  8) Andrey Rublev  OR  (   ) Gael Monfils

    TEAM.draw(mens_singles, '2.17').matchup(1, men.Ruud, 2, men.Zhang_Zhizhen).select(1, 4)  # (  5) Casper Ruud  OR  (   ) Zhizhen Zhang
    TEAM.draw(mens_singles, '2.18').matchup(1, men.Hijikata, 2, men.Fucsovics).select(2, 5)  # ( WC) Rinky Hijikata  OR  (   ) Marton Fucsovics
    TEAM.draw(mens_singles, '2.19').matchup(1, men.Mannarino, 2, men.Marozsan).select(1, 3)  # ( 22) Adrian Mannarino  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles, '2.20').matchup(1, men.Ofner, 2, men.Tiafoe).select(2, 3)  # (   ) Sebastian Ofner  OR  ( 10) Frances Tiafoe
    TEAM.draw(mens_singles, '2.21').matchup(1, men.Paul, 2, men.Safiullin).select(1, 3)  # ( 14) Tommy Paul  OR  (   ) Roman Safiullin
    TEAM.draw(mens_singles, '2.22').matchup(1, men.Cerundolo_Juan, 2, men.Davidovich_Fokina).select(1, 5)  # (   ) Juan Manuel Cerundolo  OR  ( 21) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles, '2.23').matchup(1, men.Thiem, 2, men.Shelton).select(1, 4)  # (   ) Dominic Thiem  OR  (   ) Ben Shelton
    TEAM.draw(mens_singles, '2.24').matchup(1, men.Karatsev, 2, men.Carballes_Baena).select(2, 4)  # (   ) Aslan Karatsev  OR  (   ) Roberto Carballes Baena
    TEAM.draw(mens_singles, '2.25').matchup(1, men.Tsitsipas, 2, men.Stricker).select(2, 5)  # (  7) Stefanos Tsitsipas  OR  (  Q) D.Stricker
    TEAM.draw(mens_singles, '2.26').matchup(1, men.Bonzi, 2, men.Eubanks).select(2, 3)  # ( WC) Benjamin Bonzi  OR  ( 28) Christopher Eubanks
    TEAM.draw(mens_singles, '2.27').matchup(1, men.Titouan_Droguet, 2, men.Jakub_Mensik).select(1, 4)  # (  Q) Titouan Droguet  OR  (  Q) Jakub Mensik
    TEAM.draw(mens_singles, '2.28').matchup(1, men.Varillas, 2, men.Fritz).select(2, 4)  # (   ) Juan Pablo Varillas  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles, '2.29').matchup(1, men.Mcdonald, 2, men.Gojo).select(1, 3)  # (   ) Mackenzie McDonald  OR  (  Q) Borna Gojo
    TEAM.draw(mens_singles, '2.30').matchup(1, men.Vesely, 2, men.Cerundolo_Francisco).select(2, 3)  # (   ) Jiri Vesely  OR  ( 20) Francisco Cerundolo
    TEAM.draw(mens_singles, '2.31').matchup(1, men.Djere, 2, men.Gaston).select(1, 3)  # ( 32) Laslo Djere  OR  (  Q) Hugo Gaston
    TEAM.draw(mens_singles, '2.32').matchup(1, men.Zapata_Miralles, 2, men.Djokovic).select(2, 3)  # (   ) Bernabe Zapata Miralles  OR  (  2) Novak Djokovic
# mens_singles_round_2:END



# womens_singles_round_1:START
def womens_singles_round_1(womens_singles):
    TEAM.draw(womens_singles).match('1.1').winner(women.Swiatek).in_sets(2)  # (  1) Iga Swiatek  OR  (   ) Rebecca Peterson
    TEAM.draw(womens_singles).match('1.2').winner(women.Saville).in_sets(3)  # ( WC) Clervie Ngounoue  OR  (   ) Daria Saville
    TEAM.draw(womens_singles).match('1.3').winner(women.Davis).in_sets(3)  # (   ) Lauren Davis  OR  (   ) Danka Kovinic
    TEAM.draw(womens_singles).match('1.4').winner(women.Cocciaretto).in_sets(2)  # (  Q) Kaja Juvan  OR  ( 29) Elisabetta Cocciaretto
    TEAM.draw(womens_singles).match('1.5').winner(women.Ostapenko).in_sets(3)  # ( 20) Jelena Ostapenko  OR  (   ) Jasmine Paolini
    TEAM.draw(womens_singles).match('1.6').winner(women.Alizé_Cornet).in_sets(3)  # (   ) Alizé Cornet  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles).match('1.7').winner(women.Wang_Xiyu).in_sets(3)  # (   ) V.Hruncakova  OR  (   ) Xiyu Wang
    TEAM.draw(womens_singles).match('1.8').winner(women.Kudermetova_Veronika).in_sets(2)  # (   ) Bernarda Pera  OR  ( 16) Veronika Kudermetova
    TEAM.draw(womens_singles).match('1.9').winner(women.Kvitova).in_sets(2)  # ( 11) Petra Kvitova  OR  (   ) Cristina Bucsa
    TEAM.draw(womens_singles).match('1.10').winner(women.Caroline_Wozniacki).in_sets(3)  # (  Q) Tatiana Prozorova  OR  ( WC) Caroline Wozniacki
    TEAM.draw(womens_singles).match('1.11').winner(women.Birrell).in_sets(3)  # ( LL) Kimberly Birrell  OR  (   ) Jennifer Brady
    TEAM.draw(womens_singles).match('1.12').winner(women.Linette).in_sets(3)  # (   ) Aliaksandra Sasnovich  OR  ( 24) Magda Linette
    TEAM.draw(womens_singles).match('1.13').winner(women.Mertens).in_sets(2)  # ( 32) Elise Mertens  OR  (  Q) Mirjam Bjorklund
    TEAM.draw(womens_singles).match('1.14').winner(women.Collins).in_sets(3)  # (   ) Danielle Collins  OR  (   ) Linda Fruhvirtova
    TEAM.draw(womens_singles).match('1.15').winner(women.Andreeva_Mirra).in_sets(3)  # (  Q) Olivia Gadecki  OR  (   ) Mirra Andreeva
    TEAM.draw(womens_singles).match('1.16').winner(women.Gauff).in_sets(2)  # (  Q) Laura Siegemund  OR  (  6) Coco Gauff
    TEAM.draw(womens_singles).match('1.17').winner(women.Rybakina).in_sets(2)  # (  4) Elena Rybakina  OR  (   ) Marta Kostyuk
    TEAM.draw(womens_singles).match('1.18').winner(women.Ajla_Tomljanovic).in_sets(3)  # (   ) Panna Udvardy  OR  (   ) Ajla Tomljanovic
    TEAM.draw(womens_singles).match('1.19').winner(women.Kalinskaya).in_sets(3)  # (   ) Anna Kalinskaya  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles).match('1.20').winner(women.Cirstea).in_sets(2)  # ( WC) Kayla Day  OR  ( 30) Sorana Cirstea
    TEAM.draw(womens_singles).match('1.21').winner(women.Azarenka).in_sets(2)  # ( 18) Victoria Azarenka  OR  ( WC) Fiona Ferro
    TEAM.draw(womens_singles).match('1.22').winner(women.Sherif).in_sets(3)  # (   ) Lin Zhu  OR  (   ) Mayar Sherif
    TEAM.draw(womens_singles).match('1.23').winner(women.Betova).in_sets(3)  # (  Q) Yuriko Lily Miyazaki  OR  (   ) Margarita Betova
    TEAM.draw(womens_singles).match('1.24').winner(women.Bencic).in_sets(2)  # (   ) Kamilla Rakhimova  OR  ( 15) Belinda Bencic
    TEAM.draw(womens_singles).match('1.25').winner(women.Muchova).in_sets(3)  # ( 10) Karolina Muchova  OR  ( WC) Storm Hunter
    TEAM.draw(womens_singles).match('1.26').winner(women.Navarro).in_sets(3)  # (   ) Magdalena Frech  OR  (   ) Emma Navarro
    TEAM.draw(womens_singles).match('1.27').winner(women.Townsend).in_sets(2)  # (   ) Varvara Gracheva  OR  (   ) Taylor Townsend
    TEAM.draw(womens_singles).match('1.28').winner(women.Haddad_Maia).in_sets(2)  # (   ) Sloane Stephens  OR  ( 19) Beatriz Haddad Maia
    TEAM.draw(womens_singles).match('1.29').winner(women.Kalinina).in_sets(2)  # ( 28) Anhelina Kalinina  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles).match('1.30').winner(women.Wang_Xinyu).in_sets(3)  # (  Q) Katie Volynets  OR  (   ) Xinyu Wang
    TEAM.draw(womens_singles).match('1.31').winner(women.Schmiedlova).in_sets(3)  # (   ) Anna Karolina Schmiedlova  OR  (   ) Kateryna Baindl
    TEAM.draw(womens_singles).match('1.32').winner(women.Sakkari).in_sets(2)  # (   ) Rebeka Masarova  OR  (  8) Maria Sakkari
    TEAM.draw(womens_singles).match('1.33').winner(women.Garcia).in_sets(2)  # (  7) Caroline Garcia  OR  (  Q) Yafan Wang
    TEAM.draw(womens_singles).match('1.34').winner(women.Parry).in_sets(2)  # (   ) Katie Boulter  OR  (   ) Diane Parry
    TEAM.draw(womens_singles).match('1.35').winner(women.Stearns).in_sets(3)  # (   ) Peyton Stearns  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles).match('1.36').winner(women.Potapova).in_sets(2)  # (   ) Clara Tauson  OR  ( 27) Anastasia Potapova
    TEAM.draw(womens_singles).match('1.37').winner(women.Alexandrova).in_sets(2)  # ( 22) Ekaterina Alexandrova  OR  (   ) Leylah Fernandez
    TEAM.draw(womens_singles).match('1.38').winner(women.Tsurenko).in_sets(2)  # (  Q) Elsa Jacquemot  OR  (   ) Lesia Tsurenko
    TEAM.draw(womens_singles).match('1.39').winner(women.Putintseva).in_sets(3)  # (   ) Martina Trevisan  OR  (   ) Yulia Putintseva
    TEAM.draw(womens_singles).match('1.40').winner(women.Vondrousova).in_sets(2)  # (  Q) Na Lae Han  OR  (  9) Marketa Vondrousova
    TEAM.draw(womens_singles).match('1.41').winner(women.Samsonova).in_sets(2)  # ( 14) Liudmila Samsonova  OR  (   ) Claire Liu
    TEAM.draw(womens_singles).match('1.42').winner(women.Begu).in_sets(2)  # (   ) Irina-Camelia Begu  OR  (   ) Tamara Korpatsch
    TEAM.draw(womens_singles).match('1.43').winner(women.Zvonareva).in_sets(3)  # ( LL) Yanina Wickmayer  OR  (  Q) Vera Zvonareva
    TEAM.draw(womens_singles).match('1.44').winner(women.Keys).in_sets(2)  # (   ) Arantxa Rus  OR  ( 17) Madison Keys
    TEAM.draw(womens_singles).match('1.45').winner(women.Svitolina).in_sets(2)  # ( 26) Svitolina  OR  (   ) Anna-Lena Friedsam
    TEAM.draw(womens_singles).match('1.46').winner(women.Pavlyuchenkova).in_sets(2)  # (   ) Anastasia Pavlyuchenkova  OR  (  Q) Fiona Crawley
    TEAM.draw(womens_singles).match('1.47').winner(women.Tig).in_sets(2)  # (   ) Patricia Maria Tig  OR  (   ) Rebecca Marino
    TEAM.draw(womens_singles).match('1.48').winner(women.Pegula).in_sets(2)  # (   ) Camila Giorgi  OR  (  3) Jessica Pegula
    TEAM.draw(womens_singles).match('1.49').winner(women.Jabeur).in_sets(2)  # (  5) Ons Jabeur  OR  (   ) Camila Osorio
    TEAM.draw(womens_singles).match('1.50').winner(women.Noskova).in_sets(3)  # (   ) Linda Noskova  OR  (   ) Madison Brengle
    TEAM.draw(womens_singles).match('1.51').winner(women.Maria).in_sets(3)  # (   ) Tatjana Maria  OR  (   ) Petra Martic
    TEAM.draw(womens_singles).match('1.52').winner(women.Bouzkova).in_sets(2)  # ( WC) Ashlyn Krueger  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles).match('1.53').winner(women.Zheng).in_sets(2)  # ( 23) Qinwen Zheng  OR  (   ) Nadia Podoroska
    TEAM.draw(womens_singles).match('1.54').winner(women.Strycova).in_sets(2)  # (   ) Barbora Strycova  OR  (   ) Kaia Kanepi
    TEAM.draw(womens_singles).match('1.55').winner(women.Lys).in_sets(3)  # ( WC) Robin Montgomery  OR  (  Q) Eva Lys
    TEAM.draw(womens_singles).match('1.56').winner(women.Krejcikova).in_sets(2)  # (   ) Lucia Bronzetti  OR  ( 12) Barbora Krejcikova
    TEAM.draw(womens_singles).match('1.57').winner(women.Kasatkina).in_sets(2)  # ( 13) Daria Kasatkina  OR  (   ) Alycia Parks
    TEAM.draw(womens_singles).match('1.58').winner(women.Bogdan).in_sets(2)  # (   ) Ana Bogdan  OR  (   ) Sofia Kenin
    TEAM.draw(womens_singles).match('1.59').winner(women.Minnen).in_sets(3)  # (  Q) Greet Minnen  OR  ( WC) Venus Williams
    TEAM.draw(womens_singles).match('1.60').winner(women.Vekic).in_sets(2)  # (  Q) Sachia Vickery  OR  ( 21) Donna Vekic
    TEAM.draw(womens_singles).match('1.61').winner(women.Pliskova).in_sets(2)  # ( 25) Karolina Pliskova  OR  (  Q) Elena-Gabriela Ruse
    TEAM.draw(womens_singles).match('1.62').winner(women.Dolehide).in_sets(2)  # (   ) Caroline Dolehide  OR  (   ) Clara Burel
    TEAM.draw(womens_singles).match('1.63').winner(women.Blinkova).in_sets(2)  # (   ) Anna Blinkova  OR  (   ) Jodie Burrage
    TEAM.draw(womens_singles).match('1.64').winner(women.Sabalenka).in_sets(2)  # (   ) Maryna Zanevska  OR  (  2) Aryna Sabalenka
# womens_singles_round_1:END


# mens_singles_round_1:START
def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles).match('1.1').winner(men.Alcaraz).in_sets(3)  # (  1) Carlos Alcaraz  OR  (   ) Dominik Koepfer
    TEAM.draw(mens_singles).match('1.2').winner(men.Harris).in_sets(4)  # (   ) Lloyd Harris  OR  (   ) Guido Pella
    TEAM.draw(mens_singles).match('1.3').winner(men.Botic_van_De_Zandschulp).in_sets(4)  # (   ) Botic van De Zandschulp  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles).match('1.4').winner(men.Galan).in_sets(3)  # (   ) Daniel Elahi Galan  OR  ( 26) Daniel Evans
    TEAM.draw(mens_singles).match('1.5').winner(men.Griekspoor).in_sets(4)  # ( 24) Tallon Griekspoor  OR  (   ) Arthur Fils
    TEAM.draw(mens_singles).match('1.6').winner(men.Arnaldi).in_sets(4)  # (   ) Jason Kubler  OR  (   ) Matteo Arnaldi
    TEAM.draw(mens_singles).match('1.7').winner(men.Kokkinakis).in_sets(4)  # (   ) Thanasi Kokkinakis  OR  (  Q) Yu Hsiou Hsu
    TEAM.draw(mens_singles).match('1.8').winner(men.Norrie).in_sets(4)  # (   ) Alexander Shevchenko  OR  ( 16) Cameron Norrie
    TEAM.draw(mens_singles).match('1.9').winner(men.Zverev).in_sets(3)  # ( 12) Alexander Zverev  OR  (   ) Aleksandar Vukic
    TEAM.draw(mens_singles).match('1.10').winner(men.Lestienne).in_sets(4)  # (   ) Daniel Altmaier  OR  (   ) Constant Lestienne
    TEAM.draw(mens_singles).match('1.11').winner(men.Murray_Andy).in_sets(5)  # (   ) Andy Murray  OR  (   ) Corentin Moutet
    TEAM.draw(mens_singles).match('1.12').winner(men.Dimitrov).in_sets(3)  # (   ) Alex Molcan  OR  ( 19) Grigor Dimitrov
    TEAM.draw(mens_singles).match('1.13').winner(men.Etcheverry).in_sets(3)  # ( 30) Tomas Martin Etcheverry  OR  (  Q) Otto Virtanen
    TEAM.draw(mens_singles).match('1.14').winner(men.Nishioka).in_sets(4)  # (   ) Stan Wawrinka  OR  (   ) Yoshihito Nishioka
    TEAM.draw(mens_singles).match('1.15').winner(men.Nicolas_Moreno_De_Alboran).in_sets(4)  # (  Q) Nicolas Moreno De Alboran  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles).match('1.16').winner(men.Sinner).in_sets(3)  # (   ) Yannick Hanfmann  OR  (  6) Jannik Sinner
    TEAM.draw(mens_singles).match('1.17').winner(men.Medvedev).in_sets(3)  # (  3) Daniil Medvedev  OR  (   ) Attila Balazs
    TEAM.draw(mens_singles).match('1.18').winner(men.Purcell).in_sets(4)  # (   ) Max Purcell  OR  (   ) Christopher O'Connell
    TEAM.draw(mens_singles).match('1.19').winner(men.Duckworth).in_sets(3)  # (   ) James Duckworth  OR  (  Q) Felipe Meligeni Alves
    TEAM.draw(mens_singles).match('1.20').winner(men.Coric).in_sets(4)  # (   ) Sebastian Baez  OR  ( 27) Borna Coric
    TEAM.draw(mens_singles).match('1.21').winner(men.Jarry).in_sets(4)  # ( 23) Nicolas Jarry  OR  (   ) Luca Van Assche
    TEAM.draw(mens_singles).match('1.22').winner(men.Ramos_Vinolas).in_sets(4)  # (   ) Albert Ramos-Vinolas  OR  ( WC) Alex Michelsen
    TEAM.draw(mens_singles).match('1.23').winner(men.Lajovic).in_sets(4)  # (   ) Yibing Wu  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles).match('1.24').winner(men.Alex_de_Minaur).in_sets(4)  # (  Q) Timofey Skatov  OR  ( 13) Alex de Minaur
    TEAM.draw(mens_singles).match('1.25').winner(men.Khachanov).in_sets(4)  # ( 11) Karen Khachanov  OR  ( WC) Michael Mmoh
    TEAM.draw(mens_singles).match('1.26').winner(men.Facundo_Diaz_Acosta).in_sets(4)  # (   ) Facundo Diaz Acosta  OR  ( WC) John Isner
    TEAM.draw(mens_singles).match('1.27').winner(men.Draper).in_sets(4)  # (   ) Radu Albot  OR  (   ) Jack Draper
    TEAM.draw(mens_singles).match('1.28').winner(men.Hurkacz).in_sets(4)  # (   ) Marc-Andrea Huesler  OR  ( 17) Hubert Hurkacz
    TEAM.draw(mens_singles).match('1.29').winner(men.Humbert).in_sets(4)  # ( 29) Ugo Humbert  OR  (   ) Matteo Berrettini
    TEAM.draw(mens_singles).match('1.30').winner(men.Schwartzman).in_sets(5)  # (   ) Diego Schwartzman  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles).match('1.31').winner(men.Monfils).in_sets(3)  # (  Q) Taro Daniel  OR  (   ) Gael Monfils
    TEAM.draw(mens_singles).match('1.32').winner(men.Rublev).in_sets(4)  # (   ) Arthur Cazaux  OR  (  8) Andrey Rublev
    TEAM.draw(mens_singles).match('1.33').winner(men.Ruud).in_sets(3)  # (  5) Casper Ruud  OR  (  Q) Emilio Nava
    TEAM.draw(mens_singles).match('1.34').winner(men.Wolf).in_sets(4)  # (   ) J.J. Wolf  OR  (   ) Zhizhen Zhang
    TEAM.draw(mens_singles).match('1.35').winner(men.Kotov).in_sets(4)  # ( WC) Rinky Hijikata  OR  (   ) Pavel Kotov
    TEAM.draw(mens_singles).match('1.36').winner(men.Korda).in_sets(4)  # (   ) Marton Fucsovics  OR  ( 31) Sebastian Korda
    TEAM.draw(mens_singles).match('1.37').winner(men.Mannarino).in_sets(4)  # ( 22) Adrian Mannarino  OR  (   ) Yosuke Watanuki
    TEAM.draw(mens_singles).match('1.38').winner(men.Marozsan).in_sets(4)  # (   ) Richard Gasquet  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles).match('1.39').winner(men.Ofner).in_sets(5)  # (   ) Sebastian Ofner  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles).match('1.40').winner(men.Tiafoe).in_sets(3)  # ( WC) Learner Tien  OR  ( 10) Frances Tiafoe
    TEAM.draw(mens_singles).match('1.41').winner(men.Paul).in_sets(3)  # ( 14) Tommy Paul  OR  (  Q) Stefano Travaglia
    TEAM.draw(mens_singles).match('1.42').winner(men.Cecchinato).in_sets(4)  # (   ) Roman Safiullin  OR  (   ) Marco Cecchinato
    TEAM.draw(mens_singles).match('1.43').winner(men.Cerundolo_Juan).in_sets(4)  # (   ) Ilya Ivashka  OR  (   ) Juan Manuel Cerundolo
    TEAM.draw(mens_singles).match('1.44').winner(men.Davidovich_Fokina).in_sets(3)  # (   ) Marcos Giron  OR  ( 21) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles).match('1.45').winner(men.Bublik).in_sets(4)  # ( 25) Alexander Bublik  OR  (   ) Dominic Thiem
    TEAM.draw(mens_singles).match('1.46').winner(men.Shelton).in_sets(4)  # (   ) Pedro Cachin  OR  (   ) Ben Shelton
    TEAM.draw(mens_singles).match('1.47').winner(men.Lehecka).in_sets(4)  # (   ) Aslan Karatsev  OR  (   ) Jiri Lehecka
    TEAM.draw(mens_singles).match('1.48').winner(men.Rune).in_sets(3)  # (   ) Roberto Carballes Baena  OR  (  4) Holger Rune
    TEAM.draw(mens_singles).match('1.49').winner(men.Tsitsipas).in_sets(3)  # (  7) Stefanos Tsitsipas  OR  (   ) Milos Raonic
    TEAM.draw(mens_singles).match('1.50').winner(men.Popyrin).in_sets(4)  # (  Q) D.Stricker  OR  (   ) Alexei Popyrin
    TEAM.draw(mens_singles).match('1.51').winner(men.Halys).in_sets(4)  # (   ) Quentin Halys  OR  ( WC) Benjamin Bonzi
    TEAM.draw(mens_singles).match('1.52').winner(men.Eubanks).in_sets(4)  # (   ) Soonwoo Kwon  OR  ( 28) Christopher Eubanks
    TEAM.draw(mens_singles).match('1.53').winner(men.Musetti).in_sets(4)  # ( 18) Lorenzo Musetti  OR  (  Q) Titouan Droguet
    TEAM.draw(mens_singles).match('1.54').winner(men.Barrere).in_sets(5)  # (  Q) Jakub Mensik  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles).match('1.55').winner(men.Kecmanovic).in_sets(4)  # (   ) Miomir Kecmanovic  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles).match('1.56').winner(men.Fritz).in_sets(3)  # ( WC) Steve Johnson  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles).match('1.57').winner(men.Auger_Aliassime).in_sets(4)  # ( 15) Felix Auger-Aliassime  OR  (   ) Mackenzie McDonald
    TEAM.draw(mens_singles).match('1.58').winner(men.Dellien).in_sets(4)  # (   ) Hugo Dellien  OR  (  Q) Borna Gojo
    TEAM.draw(mens_singles).match('1.59').winner(men.Vesely).in_sets(4)  # (   ) Jiri Vesely  OR  (  Q) Enzo Couacaud
    TEAM.draw(mens_singles).match('1.60').winner(men.Cerundolo_Francisco).in_sets(4)  # (  Q) Zachary Svajda  OR  ( 20) Francisco Cerundolo
    TEAM.draw(mens_singles).match('1.61').winner(men.Nakashima).in_sets(4)  # ( 32) Laslo Djere  OR  (   ) Brandon Nakashima
    TEAM.draw(mens_singles).match('1.62').winner(men.Gaston).in_sets(5)  # (  Q) Sho Shimabukuro  OR  (  Q) Hugo Gaston
    TEAM.draw(mens_singles).match('1.63').winner(men.Zapata_Miralles).in_sets(4)  # (   ) Bernabe Zapata Miralles  OR  ( WC) Ethan Quinn
    TEAM.draw(mens_singles).match('1.64').winner(men.Djokovic).in_sets(3)  # (   ) Alexandre Muller  OR  (  2) Novak Djokovic
# mens_singles_round_1:END




