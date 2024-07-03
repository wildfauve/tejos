# from typing import List
# import importlib
# import re
#
# from tejos import model
#
# # AustralianOpen = model.GrandSlam(name="Australian Open", subject_name="AustralianOpen", perma_id="ao")
# # RolandGarros = model.GrandSlam(name="Roland Garros", subject_name="RolandGarros", perma_id="rg")
# # Wimbledon = model.GrandSlam(name="Wimbledon", subject_name="Wimbledon", perma_id="wm")
# # USOpen = model.GrandSlam(name="US Open", subject_name="UsOpen", perma_id="uo")
#
# """
# Add every new tournament to this Dict.  This allows an individual tournament and its results to be loaded without having
# to load all the others.
# + Key is the name which is used to refer to the tournament in the CLI.
# + Value: Tuple[tournament_year, tournament_module].
#          This provides the arguments for the `importlib.import_module()` module name.  tournament modules are relative
#          to this module, and are made up of a year and the name of the module.
#
# For example `'Wimbledon2023': (2023, "wimbledon")`
# + the CLI refers to the tournament as Wimbledon2023
# + the tournament module to load is .year_2023.wimbledon.tournament
# """
# TournamentLoaderConfig = {
#     'AustralianOpen2023': (2023, "australian_open"),
#     'RolandGarros2023': (2023, "wimbledon"),
#     'Wimbledon2023': (2023, "wimbledon")
# }
#
#
# def tournament_names():
#     return TournamentLoaderConfig.keys()
#
#
# def tournament_in_fantasy(name):
#     """
#     Takes a tournament name and dynamically loads the tournament module associated with that tournament.
#     For example, if the name is AustralianOpen2023, the module loaded is tejos.majors.year_2023.australian_open.tournament
#
#
#     :param name:
#     :return:
#     """
#     if name not in tournament_names():
#         return None
#
#     tournament_module = tournament_module_name(name)
#     return getattr(tournament_module, name)
#
#
# def tournament_module_name(name):
#     year, tournament_module_name = TournamentLoaderConfig.get(name)
#     tournament_module = importlib.import_module(f"tejos.majors.year_{year}.{tournament_module_name}.tournament")
#     return tournament_module
#
#
# def add_results(draws: List[model.Draw], results_module):
#     mens, womens = _for_round(model.find_draw_by_cls(model.MensSingles, draws),
#                               model.find_draw_by_cls(model.WomensSingles, draws),
#                               results_module)
#     return mens, womens
#
#
# def _for_round(mens_singles, womens_singles, results_module):
#     return _for_rd_fn_caller(results_module, [mens_singles, womens_singles])
#
#
# def _for_rd_fn_caller(results_module, draws: List):
#     for draw in draws:
#         [getattr(results_module, f)(draw) for f in dir(results_module) if re.match(f"^{draw.fn_symbol}_", f)]
#     return draws
