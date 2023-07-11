poetry run tourn new-tournament --tournament Wimbledon --perma-id wm

poetry run tourn new-event --tournament Wimbledon --year 2023

poetry run tourn new-draw --tournament Wimbledon --year 2023 --name WomensSingles --best-of 3 --draw-size 64
poetry run tourn new-draw --tournament Wimbledon --year 2023 --name MensSingles --best-of 5 --draw-size 64

poetry run tourn add-entries --tournament Wimbledon --year 2023 --draw WomensSingles --in-file data/2023/wm/womens_singles.csv
poetry run tourn add-entries --tournament Wimbledon --year 2023 --draw MensSingles --in-file data/2023/wm/mens_singles.csv

poetry run tourn first-round-draw --tournament Wimbledon --year 2023 --draw WomensSingles --in-file data/2023/wm/womens_singles_first_round.csv
poetry run tourn first-round-draw --tournament Wimbledon --year 2023 --draw MensSingles --in-file data/2023/wm/mens_singles_first_round.csv