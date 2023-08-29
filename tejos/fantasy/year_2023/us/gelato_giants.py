import sys
from tejos import model
from tejos.fantasy import helpers
from tejos.players import atp_players as men, wta_players as women
from tejos.players.wta_players import *
from tejos.players.atp_players import *

this = sys.modules[__name__]

TEAM = None

def team():
    this.TEAM = model.Team.get('Gelato Giants')

def team_gelato_giants(mens_singles, womens_singles):
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
    TEAM.draw(womens_singles).match('1.1').winner(women).in_sets()  # (  1) Iga Swiatek  OR  (   ) Rebecca Peterson
    TEAM.draw(womens_singles).match('1.2').winner(women).in_sets()  # ( WC) Clervie Ngounoue  OR  (   ) Daria Saville
    TEAM.draw(womens_singles).match('1.3').winner(women).in_sets()  # (   ) Lauren Davis  OR  (   ) Danka Kovinic
    TEAM.draw(womens_singles).match('1.4').winner(women).in_sets()  # (  Q) Kaja Juvan  OR  ( 29) Elisabetta Cocciaretto
    TEAM.draw(womens_singles).match('1.5').winner(women).in_sets()  # ( 20) Jelena Ostapenko  OR  (   ) Jasmine Paolini
    TEAM.draw(womens_singles).match('1.6').winner(women).in_sets()  # (   ) Alizé Cornet  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles).match('1.7').winner(women).in_sets()  # (   ) Hruncakova  OR  (   ) Xiyu Wang
    TEAM.draw(womens_singles).match('1.8').winner(women).in_sets()  # (   ) Bernarda Pera  OR  ( 16) Veronika Kudermetova
    TEAM.draw(womens_singles).match('1.9').winner(women).in_sets()  # ( 11) Petra Kvitova  OR  (   ) Cristina Bucsa
    TEAM.draw(womens_singles).match('1.10').winner(women).in_sets()  # (  Q) Tatiana Prozorova  OR  ( WC) Caroline Wozniacki
    TEAM.draw(womens_singles).match('1.11').winner(women).in_sets()  # ( LL) Kimberly Birrell  OR  (   ) Jennifer Brady
    TEAM.draw(womens_singles).match('1.12').winner(women).in_sets()  # (   ) Aliaksandra Sasnovich  OR  ( 24) Magda Linette
    TEAM.draw(womens_singles).match('1.13').winner(women).in_sets()  # ( 32) Elise Mertens  OR  (  Q) Mirjam Bjorklund
    TEAM.draw(womens_singles).match('1.14').winner(women).in_sets()  # (   ) Danielle Collins  OR  (   ) Linda Fruhvirtova
    TEAM.draw(womens_singles).match('1.15').winner(women).in_sets()  # (  Q) Olivia Gadecki  OR  (   ) Mirra Andreeva
    TEAM.draw(womens_singles).match('1.16').winner(women).in_sets()  # (  Q) Laura Siegemund  OR  (  6) Coco Gauff
    TEAM.draw(womens_singles).match('1.17').winner(women).in_sets()  # (  4) Elena Rybakina  OR  (   ) Marta Kostyuk
    TEAM.draw(womens_singles).match('1.18').winner(women).in_sets()  # (   ) Panna Udvardy  OR  (   ) Ajla Tomljanovic
    TEAM.draw(womens_singles).match('1.19').winner(women).in_sets()  # (   ) Anna Kalinskaya  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles).match('1.20').winner(women).in_sets()  # ( WC) Kayla Day  OR  ( 30) Sorana Cirstea
    TEAM.draw(womens_singles).match('1.21').winner(women).in_sets()  # ( 18) Victoria Azarenka  OR  ( WC) Fiona Ferro
    TEAM.draw(womens_singles).match('1.22').winner(women).in_sets()  # (   ) Lin Zhu  OR  (   ) Mayar Sherif
    TEAM.draw(womens_singles).match('1.23').winner(women).in_sets()  # (  Q) Yuriko Lily Miyazaki  OR  (   ) Margarita Betova
    TEAM.draw(womens_singles).match('1.24').winner(women).in_sets()  # (   ) Kamilla Rakhimova  OR  ( 15) Belinda Bencic
    TEAM.draw(womens_singles).match('1.25').winner(women).in_sets()  # ( 10) Karolina Muchova  OR  ( WC) Storm Hunter
    TEAM.draw(womens_singles).match('1.26').winner(women).in_sets()  # (   ) Magdalena Frech  OR  (   ) Emma Navarro
    TEAM.draw(womens_singles).match('1.27').winner(women).in_sets()  # (   ) Varvara Gracheva  OR  (   ) Taylor Townsend
    TEAM.draw(womens_singles).match('1.28').winner(women).in_sets()  # (   ) Sloane Stephens  OR  ( 19) Beatriz Haddad Maia
    TEAM.draw(womens_singles).match('1.29').winner(women).in_sets()  # ( 28) Anhelina Kalinina  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles).match('1.30').winner(women).in_sets()  # (  Q) Katie Volynets  OR  (   ) Xinyu Wang
    TEAM.draw(womens_singles).match('1.31').winner(women).in_sets()  # (   ) Anna Karolina Schmiedlova  OR  (   ) Kateryna Baindl
    TEAM.draw(womens_singles).match('1.32').winner(women).in_sets()  # (   ) Rebeka Masarova  OR  (  8) Maria Sakkari
    TEAM.draw(womens_singles).match('1.33').winner(women).in_sets()  # (  7) Caroline Garcia  OR  (  Q) Yafan Wang
    TEAM.draw(womens_singles).match('1.34').winner(women).in_sets()  # (   ) Katie Boulter  OR  (   ) Diane Parry
    TEAM.draw(womens_singles).match('1.35').winner(women).in_sets()  # (   ) Peyton Stearns  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles).match('1.36').winner(women).in_sets()  # (   ) Clara Tauson  OR  ( 27) Anastasia Potapova
    TEAM.draw(womens_singles).match('1.37').winner(women).in_sets()  # ( 22) Ekaterina Alexandrova  OR  (   ) Leylah Fernandez
    TEAM.draw(womens_singles).match('1.38').winner(women).in_sets()  # (  Q) Elsa Jacquemot  OR  (   ) Lesia Tsurenko
    TEAM.draw(womens_singles).match('1.39').winner(women).in_sets()  # (   ) Martina Trevisan  OR  (   ) Yulia Putintseva
    TEAM.draw(womens_singles).match('1.40').winner(women).in_sets()  # (  Q) Na Lae Han  OR  (  9) Marketa Vondrousova
    TEAM.draw(womens_singles).match('1.41').winner(women).in_sets()  # ( 14) Liudmila Samsonova  OR  (   ) Claire Liu
    TEAM.draw(womens_singles).match('1.42').winner(women).in_sets()  # (   ) Irina-Camelia Begu  OR  (   ) Tamara Korpatsch
    TEAM.draw(womens_singles).match('1.43').winner(women).in_sets()  # ( LL) Yanina Wickmayer  OR  (  Q) Vera Zvonareva
    TEAM.draw(womens_singles).match('1.44').winner(women).in_sets()  # (   ) Arantxa Rus  OR  ( 17) Madison Keys
    TEAM.draw(womens_singles).match('1.45').winner(women).in_sets()  # ( 26) Svitolina  OR  (   ) Anna-Lena Friedsam
    TEAM.draw(womens_singles).match('1.46').winner(women).in_sets()  # (   ) Anastasia Pavlyuchenkova  OR  (  Q) Fiona Crawley
    TEAM.draw(womens_singles).match('1.47').winner(women).in_sets()  # (   ) Patricia Maria Tig  OR  (   ) Rebecca Marino
    TEAM.draw(womens_singles).match('1.48').winner(women).in_sets()  # (   ) Camila Giorgi  OR  (  3) Jessica Pegula
    TEAM.draw(womens_singles).match('1.49').winner(women).in_sets()  # (  5) Ons Jabeur  OR  (   ) Camila Osorio
    TEAM.draw(womens_singles).match('1.50').winner(women).in_sets()  # (   ) Linda Noskova  OR  (   ) Madison Brengle
    TEAM.draw(womens_singles).match('1.51').winner(women).in_sets()  # (   ) Tatjana Maria  OR  (   ) Petra Martic
    TEAM.draw(womens_singles).match('1.52').winner(women).in_sets()  # ( WC) Ashlyn Krueger  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles).match('1.53').winner(women).in_sets()  # ( 23) Qinwen Zheng  OR  (   ) Nadia Podoroska
    TEAM.draw(womens_singles).match('1.54').winner(women).in_sets()  # (   ) Barbora Strycova  OR  (   ) Kaia Kanepi
    TEAM.draw(womens_singles).match('1.55').winner(women).in_sets()  # ( WC) Robin Montgomery  OR  (  Q) Eva Lys
    TEAM.draw(womens_singles).match('1.56').winner(women).in_sets()  # (   ) Lucia Bronzetti  OR  ( 12) Barbora Krejcikova
    TEAM.draw(womens_singles).match('1.57').winner(women).in_sets()  # ( 13) Daria Kasatkina  OR  (   ) Alycia Parks
    TEAM.draw(womens_singles).match('1.58').winner(women).in_sets()  # (   ) Ana Bogdan  OR  (   ) Sofia Kenin
    TEAM.draw(womens_singles).match('1.59').winner(women).in_sets()  # (  Q) Greet Minnen  OR  ( WC) Venus Williams
    TEAM.draw(womens_singles).match('1.60').winner(women).in_sets()  # (  Q) Sachia Vickery  OR  ( 21) Donna Vekic
    TEAM.draw(womens_singles).match('1.61').winner(women).in_sets()  # ( 25) Karolina Pliskova  OR  (  Q) Elena-Gabriela Ruse
    TEAM.draw(womens_singles).match('1.62').winner(women).in_sets()  # (   ) Caroline Dolehide  OR  (   ) Clara Burel
    TEAM.draw(womens_singles).match('1.63').winner(women).in_sets()  # (   ) Anna Blinkova  OR  (   ) Jodie Burrage
    TEAM.draw(womens_singles).match('1.64').winner(women).in_sets()  # (   ) Maryna Zanevska  OR  (  2) Aryna Sabalenka
# womens_singles_round_1:END


# mens_singles_round_1:START
def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles).match('1.1').winner(men).in_sets()  # (  1) Carlos Alcaraz  OR  (   ) Dominik Koepfer
    TEAM.draw(mens_singles).match('1.2').winner(men).in_sets()  # (   ) Lloyd Harris  OR  (   ) Guido Pella
    TEAM.draw(mens_singles).match('1.3').winner(men).in_sets()  # (   ) Botic van De Zandschulp  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles).match('1.4').winner(men).in_sets()  # (   ) Daniel Elahi Galan  OR  ( 26) Daniel Evans
    TEAM.draw(mens_singles).match('1.5').winner(men).in_sets()  # ( 24) Tallon Griekspoor  OR  (   ) Arthur Fils
    TEAM.draw(mens_singles).match('1.6').winner(men).in_sets()  # (   ) Jason Kubler  OR  (   ) Matteo Arnaldi
    TEAM.draw(mens_singles).match('1.7').winner(men).in_sets()  # (   ) Thanasi Kokkinakis  OR  (  Q) Yu Hsiou Hsu
    TEAM.draw(mens_singles).match('1.8').winner(men).in_sets()  # (   ) Alexander Shevchenko  OR  ( 16) Cameron Norrie
    TEAM.draw(mens_singles).match('1.9').winner(men).in_sets()  # ( 12) Alexander Zverev  OR  (   ) Aleksandar Vukic
    TEAM.draw(mens_singles).match('1.10').winner(men).in_sets()  # (   ) Daniel Altmaier  OR  (   ) Constant Lestienne
    TEAM.draw(mens_singles).match('1.11').winner(men).in_sets()  # (   ) Andy Murray  OR  (   ) Corentin Moutet
    TEAM.draw(mens_singles).match('1.12').winner(men).in_sets()  # (   ) Alex Molcan  OR  ( 19) Grigor Dimitrov
    TEAM.draw(mens_singles).match('1.13').winner(men).in_sets()  # ( 30) Tomas Martin Etcheverry  OR  (  Q) Otto Virtanen
    TEAM.draw(mens_singles).match('1.14').winner(men).in_sets()  # (   ) Stan Wawrinka  OR  (   ) Yoshihito Nishioka
    TEAM.draw(mens_singles).match('1.15').winner(men).in_sets()  # (  Q) Nicolas Moreno De Alboran  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles).match('1.16').winner(men).in_sets()  # (   ) Yannick Hanfmann  OR  (  6) Jannik Sinner
    TEAM.draw(mens_singles).match('1.17').winner(men).in_sets()  # (  3) Daniil Medvedev  OR  (   ) Attila Balazs
    TEAM.draw(mens_singles).match('1.18').winner(men).in_sets()  # (   ) Max Purcell  OR  (   ) Christopher O'Connell
    TEAM.draw(mens_singles).match('1.19').winner(men).in_sets()  # (   ) Kei Nishikori  OR  (  Q) Felipe Meligeni Alves
    TEAM.draw(mens_singles).match('1.20').winner(men).in_sets()  # (   ) Sebastian Baez  OR  ( 27) Borna Coric
    TEAM.draw(mens_singles).match('1.21').winner(men).in_sets()  # ( 23) Nicolas Jarry  OR  (   ) Luca Van Assche
    TEAM.draw(mens_singles).match('1.22').winner(men).in_sets()  # (   ) Albert Ramos-Vinolas  OR  ( WC) Alex Michelsen
    TEAM.draw(mens_singles).match('1.23').winner(men).in_sets()  # (   ) Yibing Wu  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles).match('1.24').winner(men).in_sets()  # (  Q) Timofey Skatov  OR  ( 13) Alex de Minaur
    TEAM.draw(mens_singles).match('1.25').winner(men).in_sets()  # ( 11) Karen Khachanov  OR  ( WC) Michael Mmoh
    TEAM.draw(mens_singles).match('1.26').winner(men).in_sets()  # (   ) Facundo Diaz Acosta  OR  ( WC) John Isner
    TEAM.draw(mens_singles).match('1.27').winner(men).in_sets()  # (   ) Radu Albot  OR  (   ) Jack Draper
    TEAM.draw(mens_singles).match('1.28').winner(men).in_sets()  # (   ) Marc-Andrea Huesler  OR  ( 17) Hubert Hurkacz
    TEAM.draw(mens_singles).match('1.29').winner(men).in_sets()  # ( 29) Ugo Humbert  OR  (   ) Matteo Berrettini
    TEAM.draw(mens_singles).match('1.30').winner(men).in_sets()  # (   ) Diego Schwartzman  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles).match('1.31').winner(men).in_sets()  # (  Q) Taro Daniel  OR  (   ) Gael Monfils
    TEAM.draw(mens_singles).match('1.32').winner(men).in_sets()  # (   ) Emil Ruusuvuori  OR  (  8) Andrey Rublev
    TEAM.draw(mens_singles).match('1.33').winner(men).in_sets()  # (  5) Casper Ruud  OR  (  Q) Emilio Nava
    TEAM.draw(mens_singles).match('1.34').winner(men).in_sets()  # (   ) J.J. Wolf  OR  (   ) Zhizhen Zhang
    TEAM.draw(mens_singles).match('1.35').winner(men).in_sets()  # ( WC) Rinky Hijikata  OR  (   ) Pavel Kotov
    TEAM.draw(mens_singles).match('1.36').winner(men).in_sets()  # (   ) Marton Fucsovics  OR  ( 31) Sebastian Korda
    TEAM.draw(mens_singles).match('1.37').winner(men).in_sets()  # ( 22) Adrian Mannarino  OR  (   ) Yosuke Watanuki
    TEAM.draw(mens_singles).match('1.38').winner(men).in_sets()  # (   ) Richard Gasquet  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles).match('1.39').winner(men).in_sets()  # (   ) Sebastian Ofner  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles).match('1.40').winner(men).in_sets()  # ( WC) Learner Tien  OR  ( 10) Frances Tiafoe
    TEAM.draw(mens_singles).match('1.41').winner(men).in_sets()  # ( 14) Tommy Paul  OR  (  Q) Stefano Travaglia
    TEAM.draw(mens_singles).match('1.42').winner(men).in_sets()  # (   ) Roman Safiullin  OR  (   ) Marco Cecchinato
    TEAM.draw(mens_singles).match('1.43').winner(men).in_sets()  # (   ) Ilya Ivashka  OR  (   ) Juan Manuel Cerundolo
    TEAM.draw(mens_singles).match('1.44').winner(men).in_sets()  # (   ) Marcos Giron  OR  ( 21) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles).match('1.45').winner(men).in_sets()  # ( 25) Alexander Bublik  OR  (   ) Dominic Thiem
    TEAM.draw(mens_singles).match('1.46').winner(men).in_sets()  # (   ) Pedro Cachin  OR  (   ) Ben Shelton
    TEAM.draw(mens_singles).match('1.47').winner(men).in_sets()  # (   ) Aslan Karatsev  OR  (   ) Jiri Lehecka
    TEAM.draw(mens_singles).match('1.48').winner(men).in_sets()  # (   ) Roberto Carballes Baena  OR  (  4) Holger Rune
    TEAM.draw(mens_singles).match('1.49').winner(men).in_sets()  # (  7) Stefanos Tsitsipas  OR  (   ) Milos Raonic
    TEAM.draw(mens_singles).match('1.50').winner(men).in_sets()  # (  Q) D.Stricker  OR  (   ) Alexei Popyrin
    TEAM.draw(mens_singles).match('1.51').winner(men).in_sets()  # (   ) Quentin Halys  OR  ( WC) Benjamin Bonzi
    TEAM.draw(mens_singles).match('1.52').winner(men).in_sets()  # (   ) Soonwoo Kwon  OR  ( 28) Christopher Eubanks
    TEAM.draw(mens_singles).match('1.53').winner(men).in_sets()  # ( 18) Lorenzo Musetti  OR  (  Q) Titouan Droguet
    TEAM.draw(mens_singles).match('1.54').winner(men).in_sets()  # (  Q) Jakub Mensik  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles).match('1.55').winner(men).in_sets()  # (   ) Miomir Kecmanovic  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles).match('1.56').winner(men).in_sets()  # ( WC) Steve Johnson  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles).match('1.57').winner(men).in_sets()  # ( 15) Felix Auger-Aliassime  OR  (   ) Mackenzie McDonald
    TEAM.draw(mens_singles).match('1.58').winner(men).in_sets()  # (   ) Hugo Dellien  OR  (  Q) Borna Gojo
    TEAM.draw(mens_singles).match('1.59').winner(men).in_sets()  # (   ) Jiri Vesely  OR  (  Q) Enzo Couacaud
    TEAM.draw(mens_singles).match('1.60').winner(men).in_sets()  # (  Q) Zachary Svajda  OR  ( 20) Francisco Cerundolo
    TEAM.draw(mens_singles).match('1.61').winner(men).in_sets()  # ( 32) Laslo Djere  OR  (   ) Brandon Nakashima
    TEAM.draw(mens_singles).match('1.62').winner(men).in_sets()  # (  Q) Sho Shimabukuro  OR  (  Q) Hugo Gaston
    TEAM.draw(mens_singles).match('1.63').winner(men).in_sets()  # (   ) Bernabe Zapata Miralles  OR  ( WC) Ethan Quinn
    TEAM.draw(mens_singles).match('1.64').winner(men).in_sets()  # (   ) Alexandre Muller  OR  (  2) Novak Djokovic
# mens_singles_round_1:END


