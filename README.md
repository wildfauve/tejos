## CLI Commands

```shell
poetry run util draw-scrap --results-file _temp/s.py --tournament FrenchOpen2023 --round 4 --scores-only

poetry run fantasy leaderboard --tournament FrenchOpen2023 --to-discord


poetry run fantasy plot --file _temp/totals.png --tournament FrenchOpen2023 --accum-totals-plot --to-discord
poetry run fantasy plot --file _temp/rank.png --tournament FrenchOpen2023 --ranking-plot --to-discord

poetry run fantasy show-round --tournament FrenchOpen2023 --draw MensSingles --round 2

poetry run fantasy fantasy-score-template --tournament FrenchOpen2023 --round 1 

poetry run fantasy explain-team-score --tournament FrenchOpen2023 --fantasy-team-name TeamPolarPrecision
```
