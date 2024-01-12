from __future__ import annotations

from pathlib import Path
from typing import Dict
import csv

from tejos import model
from tejos.util import monad


def generate_entries_file(draws: monad.EitherMonad[Dict], tournament: model.GrandSlam, year: int):
    if not draws.is_right():
        return None
    for draw, matches in draws.value.items():

        path = Path(f"data/{year}/{tournament.perma_id}")
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)

        with open((path / f"{draw}.csv"), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['name', 'klass-name', 'seed'])
            for match in matches:
                for player in [match.player1, match.player2]:
                    if not player.player_klass:
                        writer.writerow([player.name, "missing", player.seed])
                    else:
                        writer.writerow([player.name, player.player_klass.klass_name, player.seed])
