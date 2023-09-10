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
def womens_singles_round_7(womens_singles):
    TEAM.draw(womens_singles, '7.1').matchup(1, women.Gauff, 2, women.Sabalenka).select()  # (  6) Coco Gauff  OR  (  2) Aryna Sabalenka
# womens_singles_round_7:END


# mens_singles_round_7:START
def mens_singles_round_7(mens_singles):
    TEAM.draw(mens_singles, '7.1').matchup(1, men.Djokovic, 2, men.Medvedev).select()  # (  2) Novak Djokovic  OR  (  3) Daniil Medvedev
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
    """
    To make a selection select the player number from the matchup and the number of sets (in that order).
    For example, in the Women's singles match 1.1, between Swiatek and Peterson, to select Swiatek in 2 sets the
    line should look like this...
    TEAM.draw(womens_singles, '1.1').matchup(1, women.Swiatek, 2, women.Peterson).select(1, 2)
    """

    TEAM.draw(womens_singles, '1.1').matchup(1, women.Swiatek, 2, women.Peterson).select()  # (  1) Iga Swiatek  OR  (   ) Rebecca Peterson
    TEAM.draw(womens_singles, '1.2').matchup(1, women.Clervie_Ngounoue, 2, women.Saville).select()  # ( WC) Clervie Ngounoue  OR  (   ) Daria Saville
    TEAM.draw(womens_singles, '1.3').matchup(1, women.Davis, 2, women.Kovinic).select()  # (   ) Lauren Davis  OR  (   ) Danka Kovinic
    TEAM.draw(womens_singles, '1.4').matchup(1, women.Juvan, 2, women.Cocciaretto).select()  # (  Q) Kaja Juvan  OR  ( 29) Elisabetta Cocciaretto
    TEAM.draw(womens_singles, '1.5').matchup(1, women.Ostapenko, 2, women.Paolini).select()  # ( 20) Jelena Ostapenko  OR  (   ) Jasmine Paolini
    TEAM.draw(womens_singles, '1.6').matchup(1, women.Alizé_Cornet, 2, women.Avanesyan).select()  # (   ) Alizé Cornet  OR  (   ) Elina Avanesyan
    TEAM.draw(womens_singles, '1.7').matchup(1, women.Hruncakova, 2, women.Wang_Xiyu).select()  # (   ) V.Hruncakova  OR  (   ) Xiyu Wang
    TEAM.draw(womens_singles, '1.8').matchup(1, women.Pera, 2, women.Kudermetova_Veronika).select()  # (   ) Bernarda Pera  OR  ( 16) Veronika Kudermetova
    TEAM.draw(womens_singles, '1.9').matchup(1, women.Kvitova, 2, women.Bucsa).select()  # ( 11) Petra Kvitova  OR  (   ) Cristina Bucsa
    TEAM.draw(womens_singles, '1.10').matchup(1, women.Tatiana_Prozorova, 2, women.Caroline_Wozniacki).select()  # (  Q) Tatiana Prozorova  OR  ( WC) Caroline Wozniacki
    TEAM.draw(womens_singles, '1.11').matchup(1, women.Birrell, 2, women.Brady).select()  # ( LL) Kimberly Birrell  OR  (   ) Jennifer Brady
    TEAM.draw(womens_singles, '1.12').matchup(1, women.Sasnovich, 2, women.Linette).select()  # (   ) Aliaksandra Sasnovich  OR  ( 24) Magda Linette
    TEAM.draw(womens_singles, '1.13').matchup(1, women.Mertens, 2, women.Bjorklund).select()  # ( 32) Elise Mertens  OR  (  Q) Mirjam Bjorklund
    TEAM.draw(womens_singles, '1.14').matchup(1, women.Collins, 2, women.Fruhvirtova_Linda).select()  # (   ) Danielle Collins  OR  (   ) Linda Fruhvirtova
    TEAM.draw(womens_singles, '1.15').matchup(1, women.Gadecki, 2, women.Andreeva_Mirra).select()  # (  Q) Olivia Gadecki  OR  (   ) Mirra Andreeva
    TEAM.draw(womens_singles, '1.16').matchup(1, women.Siegemund, 2, women.Gauff).select()  # (  Q) Laura Siegemund  OR  (  6) Coco Gauff
    TEAM.draw(womens_singles, '1.17').matchup(1, women.Rybakina, 2, women.Kostyuk).select()  # (  4) Elena Rybakina  OR  (   ) Marta Kostyuk
    TEAM.draw(womens_singles, '1.18').matchup(1, women.Udvardy, 2, women.Ajla_Tomljanovic).select()  # (   ) Panna Udvardy  OR  (   ) Ajla Tomljanovic
    TEAM.draw(womens_singles, '1.19').matchup(1, women.Kalinskaya, 2, women.Siniakova).select()  # (   ) Anna Kalinskaya  OR  (   ) Katerina Siniakova
    TEAM.draw(womens_singles, '1.20').matchup(1, women.Kayla_Day, 2, women.Cirstea).select()  # ( WC) Kayla Day  OR  ( 30) Sorana Cirstea
    TEAM.draw(womens_singles, '1.21').matchup(1, women.Azarenka, 2, women.Fiona_Ferro).select()  # ( 18) Victoria Azarenka  OR  ( WC) Fiona Ferro
    TEAM.draw(womens_singles, '1.22').matchup(1, women.Zhu, 2, women.Sherif).select()  # (   ) Lin Zhu  OR  (   ) Mayar Sherif
    TEAM.draw(womens_singles, '1.23').matchup(1, women.Yuriko_Lily_Miyazaki, 2, women.Betova).select()  # (  Q) Yuriko Lily Miyazaki  OR  (   ) Margarita Betova
    TEAM.draw(womens_singles, '1.24').matchup(1, women.Rakhimova, 2, women.Bencic).select()  # (   ) Kamilla Rakhimova  OR  ( 15) Belinda Bencic
    TEAM.draw(womens_singles, '1.25').matchup(1, women.Muchova, 2, women.Hunter).select()  # ( 10) Karolina Muchova  OR  ( WC) Storm Hunter
    TEAM.draw(womens_singles, '1.26').matchup(1, women.Frech, 2, women.Navarro).select()  # (   ) Magdalena Frech  OR  (   ) Emma Navarro
    TEAM.draw(womens_singles, '1.27').matchup(1, women.Gracheva, 2, women.Townsend).select()  # (   ) Varvara Gracheva  OR  (   ) Taylor Townsend
    TEAM.draw(womens_singles, '1.28').matchup(1, women.Stephens, 2, women.Haddad_Maia).select()  # (   ) Sloane Stephens  OR  ( 19) Beatriz Haddad Maia
    TEAM.draw(womens_singles, '1.29').matchup(1, women.Kalinina, 2, women.Sorribes_Tormo).select()  # ( 28) Anhelina Kalinina  OR  (   ) Sorribes Tormo
    TEAM.draw(womens_singles, '1.30').matchup(1, women.Volynets, 2, women.Wang_Xinyu).select()  # (  Q) Katie Volynets  OR  (   ) Xinyu Wang
    TEAM.draw(womens_singles, '1.31').matchup(1, women.Schmiedlova, 2, women.Baindl).select()  # (   ) Anna Karolina Schmiedlova  OR  (   ) Kateryna Baindl
    TEAM.draw(womens_singles, '1.32').matchup(1, women.Masarova, 2, women.Sakkari).select()  # (   ) Rebeka Masarova  OR  (  8) Maria Sakkari
    TEAM.draw(womens_singles, '1.33').matchup(1, women.Garcia, 2, women.Yafan_Wang).select()  # (  7) Caroline Garcia  OR  (  Q) Yafan Wang
    TEAM.draw(womens_singles, '1.34').matchup(1, women.Boulter, 2, women.Parry).select()  # (   ) Katie Boulter  OR  (   ) Diane Parry
    TEAM.draw(womens_singles, '1.35').matchup(1, women.Stearns, 2, women.Tomova).select()  # (   ) Peyton Stearns  OR  (   ) Viktoriya Tomova
    TEAM.draw(womens_singles, '1.36').matchup(1, women.Clara_Tauson, 2, women.Potapova).select()  # (   ) Clara Tauson  OR  ( 27) Anastasia Potapova
    TEAM.draw(womens_singles, '1.37').matchup(1, women.Alexandrova, 2, women.Fernandez).select()  # ( 22) Ekaterina Alexandrova  OR  (   ) Leylah Fernandez
    TEAM.draw(womens_singles, '1.38').matchup(1, women.Elsa_Jacquemot, 2, women.Tsurenko).select()  # (  Q) Elsa Jacquemot  OR  (   ) Lesia Tsurenko
    TEAM.draw(womens_singles, '1.39').matchup(1, women.Trevisan, 2, women.Putintseva).select()  # (   ) Martina Trevisan  OR  (   ) Yulia Putintseva
    TEAM.draw(womens_singles, '1.40').matchup(1, women.Na_Lae_Han, 2, women.Vondrousova).select()  # (  Q) Na Lae Han  OR  (  9) Marketa Vondrousova
    TEAM.draw(womens_singles, '1.41').matchup(1, women.Samsonova, 2, women.Liu).select()  # ( 14) Liudmila Samsonova  OR  (   ) Claire Liu
    TEAM.draw(womens_singles, '1.42').matchup(1, women.Begu, 2, women.Korpatsch).select()  # (   ) Irina-Camelia Begu  OR  (   ) Tamara Korpatsch
    TEAM.draw(womens_singles, '1.43').matchup(1, women.Wickmayer, 2, women.Zvonareva).select()  # ( LL) Yanina Wickmayer  OR  (  Q) Vera Zvonareva
    TEAM.draw(womens_singles, '1.44').matchup(1, women.Rus, 2, women.Keys).select()  # (   ) Arantxa Rus  OR  ( 17) Madison Keys
    TEAM.draw(womens_singles, '1.45').matchup(1, women.Svitolina, 2, women.Friedsam).select()  # ( 26) Svitolina  OR  (   ) Anna-Lena Friedsam
    TEAM.draw(womens_singles, '1.46').matchup(1, women.Pavlyuchenkova, 2, women.Fiona_Crawley).select()  # (   ) Anastasia Pavlyuchenkova  OR  (  Q) Fiona Crawley
    TEAM.draw(womens_singles, '1.47').matchup(1, women.Tig, 2, women.Marino).select()  # (   ) Patricia Maria Tig  OR  (   ) Rebecca Marino
    TEAM.draw(womens_singles, '1.48').matchup(1, women.Giorgi, 2, women.Pegula).select()  # (   ) Camila Giorgi  OR  (  3) Jessica Pegula
    TEAM.draw(womens_singles, '1.49').matchup(1, women.Jabeur, 2, women.Osorio).select()  # (  5) Ons Jabeur  OR  (   ) Camila Osorio
    TEAM.draw(womens_singles, '1.50').matchup(1, women.Noskova, 2, women.Brengle).select()  # (   ) Linda Noskova  OR  (   ) Madison Brengle
    TEAM.draw(womens_singles, '1.51').matchup(1, women.Maria, 2, women.Martic).select()  # (   ) Tatjana Maria  OR  (   ) Petra Martic
    TEAM.draw(womens_singles, '1.52').matchup(1, women.Krueger, 2, women.Bouzkova).select()  # ( WC) Ashlyn Krueger  OR  ( 31) Marie Bouzkova
    TEAM.draw(womens_singles, '1.53').matchup(1, women.Zheng, 2, women.Podoroska).select()  # ( 23) Qinwen Zheng  OR  (   ) Nadia Podoroska
    TEAM.draw(womens_singles, '1.54').matchup(1, women.Strycova, 2, women.Kanepi).select()  # (   ) Barbora Strycova  OR  (   ) Kaia Kanepi
    TEAM.draw(womens_singles, '1.55').matchup(1, women.Montgomery, 2, women.Lys).select()  # ( WC) Robin Montgomery  OR  (  Q) Eva Lys
    TEAM.draw(womens_singles, '1.56').matchup(1, women.Bronzetti, 2, women.Krejcikova).select()  # (   ) Lucia Bronzetti  OR  ( 12) Barbora Krejcikova
    TEAM.draw(womens_singles, '1.57').matchup(1, women.Kasatkina, 2, women.Parks).select()  # ( 13) Daria Kasatkina  OR  (   ) Alycia Parks
    TEAM.draw(womens_singles, '1.58').matchup(1, women.Bogdan, 2, women.Kenin).select()  # (   ) Ana Bogdan  OR  (   ) Sofia Kenin
    TEAM.draw(womens_singles, '1.59').matchup(1, women.Minnen, 2, women.Williams).select()  # (  Q) Greet Minnen  OR  ( WC) Venus Williams
    TEAM.draw(womens_singles, '1.60').matchup(1, women.Sachia_Vickery, 2, women.Vekic).select()  # (  Q) Sachia Vickery  OR  ( 21) Donna Vekic
    TEAM.draw(womens_singles, '1.61').matchup(1, women.Pliskova, 2, women.Ruse).select()  # ( 25) Karolina Pliskova  OR  (  Q) Elena-Gabriela Ruse
    TEAM.draw(womens_singles, '1.62').matchup(1, women.Dolehide, 2, women.Burel).select()  # (   ) Caroline Dolehide  OR  (   ) Clara Burel
    TEAM.draw(womens_singles, '1.63').matchup(1, women.Blinkova, 2, women.Burrage).select()  # (   ) Anna Blinkova  OR  (   ) Jodie Burrage
    TEAM.draw(womens_singles, '1.64').matchup(1, women.Zanevska, 2, women.Sabalenka).select()  # (   ) Maryna Zanevska  OR  (  2) Aryna Sabalenka
# womens_singles_round_1:END


# mens_singles_round_1:START
def mens_singles_round_1(mens_singles):
    TEAM.draw(mens_singles, '1.1').matchup(1, men.Alcaraz, 2, men.Koepfer).select()  # (  1) Carlos Alcaraz  OR  (   ) Dominik Koepfer
    TEAM.draw(mens_singles, '1.2').matchup(1, men.Harris, 2, men.Pella).select()  # (   ) Lloyd Harris  OR  (   ) Guido Pella
    TEAM.draw(mens_singles, '1.3').matchup(1, men.Botic_van_De_Zandschulp, 2, men.Thompson).select()  # (   ) Botic van De Zandschulp  OR  (   ) Jordan Thompson
    TEAM.draw(mens_singles, '1.4').matchup(1, men.Galan, 2, men.Evans).select()  # (   ) Daniel Elahi Galan  OR  ( 26) Daniel Evans
    TEAM.draw(mens_singles, '1.5').matchup(1, men.Griekspoor, 2, men.Fils).select()  # ( 24) Tallon Griekspoor  OR  (   ) Arthur Fils
    TEAM.draw(mens_singles, '1.6').matchup(1, men.Kubler, 2, men.Arnaldi).select()  # (   ) Jason Kubler  OR  (   ) Matteo Arnaldi
    TEAM.draw(mens_singles, '1.7').matchup(1, men.Kokkinakis, 2, men.Hsu).select()  # (   ) Thanasi Kokkinakis  OR  (  Q) Yu Hsiou Hsu
    TEAM.draw(mens_singles, '1.8').matchup(1, men.Shevchenko, 2, men.Norrie).select()  # (   ) Alexander Shevchenko  OR  ( 16) Cameron Norrie
    TEAM.draw(mens_singles, '1.9').matchup(1, men.Zverev, 2, men.Vukic).select()  # ( 12) Alexander Zverev  OR  (   ) Aleksandar Vukic
    TEAM.draw(mens_singles, '1.10').matchup(1, men.Altmaier, 2, men.Lestienne).select()  # (   ) Daniel Altmaier  OR  (   ) Constant Lestienne
    TEAM.draw(mens_singles, '1.11').matchup(1, men.Murray_Andy, 2, men.Moutet).select()  # (   ) Andy Murray  OR  (   ) Corentin Moutet
    TEAM.draw(mens_singles, '1.12').matchup(1, men.Molcan, 2, men.Dimitrov).select()  # (   ) Alex Molcan  OR  ( 19) Grigor Dimitrov
    TEAM.draw(mens_singles, '1.13').matchup(1, men.Etcheverry, 2, men.Otto_Virtanen).select()  # ( 30) Tomas Martin Etcheverry  OR  (  Q) Otto Virtanen
    TEAM.draw(mens_singles, '1.14').matchup(1, men.Wawrinka, 2, men.Nishioka).select()  # (   ) Stan Wawrinka  OR  (   ) Yoshihito Nishioka
    TEAM.draw(mens_singles, '1.15').matchup(1, men.Nicolas_Moreno_De_Alboran, 2, men.Sonego).select()  # (  Q) Nicolas Moreno De Alboran  OR  (   ) Lorenzo Sonego
    TEAM.draw(mens_singles, '1.16').matchup(1, men.Hanfmann, 2, men.Sinner).select()  # (   ) Yannick Hanfmann  OR  (  6) Jannik Sinner
    TEAM.draw(mens_singles, '1.17').matchup(1, men.Medvedev, 2, men.Attila_Balazs).select()  # (  3) Daniil Medvedev  OR  (   ) Attila Balazs
    TEAM.draw(mens_singles, '1.18').matchup(1, men.Purcell, 2, men.OConnell).select()  # (   ) Max Purcell  OR  (   ) Christopher O'Connell
    TEAM.draw(mens_singles, '1.19').matchup(1, men.Duckworth, 2, men.Felipe_Meligeni_Alves).select()  # (   ) James Duckworth  OR  (  Q) Felipe Meligeni Alves
    TEAM.draw(mens_singles, '1.20').matchup(1, men.Baez, 2, men.Coric).select()  # (   ) Sebastian Baez  OR  ( 27) Borna Coric
    TEAM.draw(mens_singles, '1.21').matchup(1, men.Jarry, 2, men.Van_Assche).select()  # ( 23) Nicolas Jarry  OR  (   ) Luca Van Assche
    TEAM.draw(mens_singles, '1.22').matchup(1, men.Ramos_Vinolas, 2, men.Alex_Michelsen).select()  # (   ) Albert Ramos-Vinolas  OR  ( WC) Alex Michelsen
    TEAM.draw(mens_singles, '1.23').matchup(1, men.Wu, 2, men.Lajovic).select()  # (   ) Yibing Wu  OR  (   ) Dusan Lajovic
    TEAM.draw(mens_singles, '1.24').matchup(1, men.Skatov, 2, men.Alex_de_Minaur).select()  # (  Q) Timofey Skatov  OR  ( 13) Alex de Minaur
    TEAM.draw(mens_singles, '1.25').matchup(1, men.Khachanov, 2, men.Mmoh).select()  # ( 11) Karen Khachanov  OR  ( WC) Michael Mmoh
    TEAM.draw(mens_singles, '1.26').matchup(1, men.Facundo_Diaz_Acosta, 2, men.Isner).select()  # (   ) Facundo Diaz Acosta  OR  ( WC) John Isner
    TEAM.draw(mens_singles, '1.27').matchup(1, men.Albot, 2, men.Draper).select()  # (   ) Radu Albot  OR  (   ) Jack Draper
    TEAM.draw(mens_singles, '1.28').matchup(1, men.Huesler, 2, men.Hurkacz).select()  # (   ) Marc-Andrea Huesler  OR  ( 17) Hubert Hurkacz
    TEAM.draw(mens_singles, '1.29').matchup(1, men.Humbert, 2, men.Berrettini).select()  # ( 29) Ugo Humbert  OR  (   ) Matteo Berrettini
    TEAM.draw(mens_singles, '1.30').matchup(1, men.Schwartzman, 2, men.Rinderknech).select()  # (   ) Diego Schwartzman  OR  (   ) Arthur Rinderknech
    TEAM.draw(mens_singles, '1.31').matchup(1, men.Daniel, 2, men.Monfils).select()  # (  Q) Taro Daniel  OR  (   ) Gael Monfils
    TEAM.draw(mens_singles, '1.32').matchup(1, men.Cazaux, 2, men.Rublev).select()  # (   ) Arthur Cazaux  OR  (  8) Andrey Rublev
    TEAM.draw(mens_singles, '1.33').matchup(1, men.Ruud, 2, men.Nava).select()  # (  5) Casper Ruud  OR  (  Q) Emilio Nava
    TEAM.draw(mens_singles, '1.34').matchup(1, men.Wolf, 2, men.Zhang_Zhizhen).select()  # (   ) J.J. Wolf  OR  (   ) Zhizhen Zhang
    TEAM.draw(mens_singles, '1.35').matchup(1, men.Hijikata, 2, men.Kotov).select()  # ( WC) Rinky Hijikata  OR  (   ) Pavel Kotov
    TEAM.draw(mens_singles, '1.36').matchup(1, men.Fucsovics, 2, men.Korda).select()  # (   ) Marton Fucsovics  OR  ( 31) Sebastian Korda
    TEAM.draw(mens_singles, '1.37').matchup(1, men.Mannarino, 2, men.Watanuki).select()  # ( 22) Adrian Mannarino  OR  (   ) Yosuke Watanuki
    TEAM.draw(mens_singles, '1.38').matchup(1, men.Gasquet, 2, men.Marozsan).select()  # (   ) Richard Gasquet  OR  (   ) Fabian Marozsan
    TEAM.draw(mens_singles, '1.39').matchup(1, men.Ofner, 2, men.Borges).select()  # (   ) Sebastian Ofner  OR  (   ) Nuno Borges
    TEAM.draw(mens_singles, '1.40').matchup(1, men.Tien, 2, men.Tiafoe).select()  # ( WC) Learner Tien  OR  ( 10) Frances Tiafoe
    TEAM.draw(mens_singles, '1.41').matchup(1, men.Paul, 2, men.Stefano_Travaglia).select()  # ( 14) Tommy Paul  OR  (  Q) Stefano Travaglia
    TEAM.draw(mens_singles, '1.42').matchup(1, men.Safiullin, 2, men.Cecchinato).select()  # (   ) Roman Safiullin  OR  (   ) Marco Cecchinato
    TEAM.draw(mens_singles, '1.43').matchup(1, men.Ivashka, 2, men.Cerundolo_Juan).select()  # (   ) Ilya Ivashka  OR  (   ) Juan Manuel Cerundolo
    TEAM.draw(mens_singles, '1.44').matchup(1, men.Giron, 2, men.Davidovich_Fokina).select()  # (   ) Marcos Giron  OR  ( 21) Alejandro Davidovich Fokina
    TEAM.draw(mens_singles, '1.45').matchup(1, men.Bublik, 2, men.Thiem).select()  # ( 25) Alexander Bublik  OR  (   ) Dominic Thiem
    TEAM.draw(mens_singles, '1.46').matchup(1, men.Cachin, 2, men.Shelton).select()  # (   ) Pedro Cachin  OR  (   ) Ben Shelton
    TEAM.draw(mens_singles, '1.47').matchup(1, men.Karatsev, 2, men.Lehecka).select()  # (   ) Aslan Karatsev  OR  (   ) Jiri Lehecka
    TEAM.draw(mens_singles, '1.48').matchup(1, men.Carballes_Baena, 2, men.Rune).select()  # (   ) Roberto Carballes Baena  OR  (  4) Holger Rune
    TEAM.draw(mens_singles, '1.49').matchup(1, men.Tsitsipas, 2, men.Raonic).select()  # (  7) Stefanos Tsitsipas  OR  (   ) Milos Raonic
    TEAM.draw(mens_singles, '1.50').matchup(1, men.Stricker, 2, men.Popyrin).select()  # (  Q) D.Stricker  OR  (   ) Alexei Popyrin
    TEAM.draw(mens_singles, '1.51').matchup(1, men.Halys, 2, men.Bonzi).select()  # (   ) Quentin Halys  OR  ( WC) Benjamin Bonzi
    TEAM.draw(mens_singles, '1.52').matchup(1, men.Soonwoo_Kwon, 2, men.Eubanks).select()  # (   ) Soonwoo Kwon  OR  ( 28) Christopher Eubanks
    TEAM.draw(mens_singles, '1.53').matchup(1, men.Musetti, 2, men.Titouan_Droguet).select()  # ( 18) Lorenzo Musetti  OR  (  Q) Titouan Droguet
    TEAM.draw(mens_singles, '1.54').matchup(1, men.Jakub_Mensik, 2, men.Barrere).select()  # (  Q) Jakub Mensik  OR  (   ) Gregoire Barrere
    TEAM.draw(mens_singles, '1.55').matchup(1, men.Kecmanovic, 2, men.Varillas).select()  # (   ) Miomir Kecmanovic  OR  (   ) Juan Pablo Varillas
    TEAM.draw(mens_singles, '1.56').matchup(1, men.Steve_Johnson, 2, men.Fritz).select()  # ( WC) Steve Johnson  OR  (  9) Taylor Fritz
    TEAM.draw(mens_singles, '1.57').matchup(1, men.Auger_Aliassime, 2, men.Mcdonald).select()  # ( 15) Felix Auger-Aliassime  OR  (   ) Mackenzie McDonald
    TEAM.draw(mens_singles, '1.58').matchup(1, men.Dellien, 2, men.Gojo).select()  # (   ) Hugo Dellien  OR  (  Q) Borna Gojo
    TEAM.draw(mens_singles, '1.59').matchup(1, men.Vesely, 2, men.Couacaud).select()  # (   ) Jiri Vesely  OR  (  Q) Enzo Couacaud
    TEAM.draw(mens_singles, '1.60').matchup(1, men.Zachary_Svajda, 2, men.Cerundolo_Francisco).select()  # (  Q) Zachary Svajda  OR  ( 20) Francisco Cerundolo
    TEAM.draw(mens_singles, '1.61').matchup(1, men.Djere, 2, men.Nakashima).select()  # ( 32) Laslo Djere  OR  (   ) Brandon Nakashima
    TEAM.draw(mens_singles, '1.62').matchup(1, men.Shimabukuro, 2, men.Gaston).select()  # (  Q) Sho Shimabukuro  OR  (  Q) Hugo Gaston
    TEAM.draw(mens_singles, '1.63').matchup(1, men.Zapata_Miralles, 2, men.Ethan_Quinn).select()  # (   ) Bernabe Zapata Miralles  OR  ( WC) Ethan Quinn
    TEAM.draw(mens_singles, '1.64').matchup(1, men.Muller, 2, men.Djokovic).select()  # (   ) Alexandre Muller  OR  (  2) Novak Djokovic
# mens_singles_round_1:END














