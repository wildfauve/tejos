from tejos.fantasy.year_2023 import wm as wm_2023, us as us_2023
from tejos.fantasy.year_2024 import ao as ao_2024, wm as wm_2024
from tejos import adapter

fantasy_tournaments = {
    "Wimbledon2023": wm_2023,
    "UsOpen2023": us_2023,
    "AustralianOpen2024": ao_2024,
    "Wimbledon2024": wm_2024
}

tournament_adapters = {
    "Wimbledon": adapter.wm_draw_parser
}

