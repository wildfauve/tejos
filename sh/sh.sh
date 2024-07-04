poetry run tourn new-tournament --tournament Wimbledon --perma-id wm

poetry run tourn new-event --tournament Wimbledon --year 2023

poetry run tourn new-draw --tournament Wimbledon --year 2023 --name WomensSingles --best-of 3 --draw-size 64 --fantasy-pt-strat WinNumSetsLossMaxSets Points21Half DoublePerRound
poetry run tourn new-draw --tournament Wimbledon --year 2023 --name MensSingles --best-of 5 --draw-size 64 --fantasy-pt-strat WinNumSetsLossMaxSets Points21Half DoublePerRound

poetry run tourn add-entries --tournament Wimbledon --year 2023 --draw WomensSingles --in-file data/2023/wm/womens_singles.csv
poetry run tourn add-entries --tournament Wimbledon --year 2023 --draw MensSingles --in-file data/2023/wm/mens_singles.csv

poetry run tourn first-round-draw --tournament Wimbledon --year 2024 --draw WomensSingles
poetry run tourn first-round-draw --tournament Wimbledon --year 2024 --draw MensSingles

poetry run fantasy fantasy-score-template-inserter --tournament Wimbledon --year 2024 --round 1

poetry run fantasy invoke-selections --tournament Wimbledon --year 2024

poetry run tourn results --tournament Wimbledon --year 2024 --rd 1 --scores-only


poetry run fantasy leaderboard --tournament Wimbledon --year 2024 --rd 1

