from . import results, entries, first_round_draw
from tejos.majors import tournaments
from tejos.players import atp_players
from tejos.model import tournament_event, draw
from tejos.fantasy import points_strategy

AustralianOpen2023 = tournament_event.TournamentEvent(event_of=tournaments.AustralianOpen, year=2023)

AO2023MensSingles = (draw.MensSingles(name="MensSingles",
                                      fn_symbol="mens_singles",
                                      best_of=5,
                                      tournament=AustralianOpen2023)
                     .draw_size(number_of_matches=8)
                     .add_entries(entries.mens_singles_entries())
                     .init_draw(first_round_draw.mens_draw_round_1())
                     .fantasy_points_strategy(points_strategy.strategy_5_2_1_double()))

AO2023WomensSingles = (draw.WomensSingles("WomensSingles",
                                          fn_symbol="womens_singles",
                                          best_of=3,
                                          tournament=AustralianOpen2023)
                       .draw_size(number_of_matches=8)
                       .add_entries(entries.womens_singles_entries())
                       .init_draw(first_round_draw.womens_draw_round_1())
                       .fantasy_points_strategy(points_strategy.strategy_5_2_1_double()))

AustralianOpen2023.has_draw(AO2023WomensSingles).has_draw(AO2023MensSingles)

results.add_results([AO2023MensSingles, AO2023WomensSingles])
