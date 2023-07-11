from . import results, entries, first_round_draw
from tejos.majors import tournaments
from tejos.model import tournament_event, draw
from tejos.fantasy import points_strategy

RolandGarros2023 = tournament_event.TournamentEvent(event_of=tournaments.RolandGarros, year=2023)


RG2023MensSingles = (draw.MensSingles(name="MensSingles",
                                      fn_symbol="mens_singles",
                                      best_of=5,
                                      tournament=RolandGarros2023)
                     .draw_size(number_of_matches=64)
                     .add_entries(entries.mens_singles_entries())
                     .first_round_draw(first_round_draw.mens_draw_round_1())
                     .fantasy_points_strategy(points_strategy.strategy_2_1_point5_double()))

RG2023WomensSingles = (draw.WomensSingles("WomensSingles",
                                          fn_symbol="womens_singles",
                                          best_of=3,
                                          tournament=RolandGarros2023)
                       .draw_size(number_of_matches=64)
                       .add_entries(entries.womens_singles_entries())
                       .first_round_draw(first_round_draw.womens_draw_round_1())
                       .fantasy_points_strategy(points_strategy.strategy_2_1_point5_double()))

RolandGarros2023.has_draw(RG2023WomensSingles).has_draw(RG2023MensSingles)

tournaments.add_results(draws=[RG2023MensSingles, RG2023WomensSingles], results_module=results)
