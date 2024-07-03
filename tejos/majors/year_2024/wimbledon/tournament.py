from . import results, entries, first_round_draw
from tejos.majors import tournaments
from tejos.model import tournament_event, draw
from tejos.fantasy import points_strategy

Wimbledon2024 = tournament_event.TournamentEvent(event_of=tournaments.Wimbledon, year=2024)


WB2024MensSingles = (draw.MensSingles(name="MensSingles",
                                      fn_symbol="mens_singles",
                                      best_of=5,
                                      tournament=Wimbledon2024)
                     .draw_size(number_of_matches=64)
                     .add_entries(entries.mens_singles_entries())
                     .first_round_draw(first_round_draw.mens_draw_round_1())
                     .fantasy_points_strategy(points_strategy.strategy_2_1_point5_double()))

WB2024WomensSingles = (draw.WomensSingles("WomensSingles",
                                          fn_symbol="womens_singles",
                                          best_of=3,
                                          tournament=Wimbledon2024)
                       .draw_size(number_of_matches=64)
                       .add_entries(entries.womens_singles_entries())
                       .first_round_draw(first_round_draw.womens_draw_round_1())
                       .fantasy_points_strategy(points_strategy.strategy_2_1_point5_double()))

Wimbledon2024.has_draw(WB2024MensSingles).has_draw(WB2024WomensSingles)

tournaments.add_results(draws=[WB2024MensSingles, WB2024WomensSingles], results_module=results)
