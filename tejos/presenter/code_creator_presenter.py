from typing import Dict, Callable, List, Tuple
from functools import partial
import csv

from tejos.util import echo, monad, console

sp = f"{'':>4}"


def fantasy_score_template(result_fn_calls: Dict, file):
    if file:
        f = open(file, 'w')
    for fn_draw_symbol, fn_calls_for_draw in result_fn_calls.items():
        for result in fn_calls_for_draw:
            if file:
                f.write(f"{result}\n")
            else:
                echo.echo(result)


def scores_scrap_inserter(tourn_mod_rd_result_tuple: monad.EitherMonad[Tuple]):
    if tourn_mod_rd_result_tuple.is_left():
        breakpoint()
    tourn_mod, rd_results = tourn_mod_rd_result_tuple.value
    results_file = tourn_mod.__file__.replace("tournament.py", "results.py")
    try_file = try_open_file_for_read(results_file)
    if try_file.is_left():
        breakpoint()
    all_results = try_file.value.read().split("\n")
    for rd_draw, results_for_rd in rd_results.items():
        updated, results = _template_inserter(partial(_results_insertion_point_indexes, rd_draw),
                                              all_results,
                                              results_for_rd)

    try_file.value.close()
    if updated:
        file_overwriter(results, results_file)


def fantasy_score_template_inserter(fantasy_module_team_fn_calls_tuple: Tuple):
    fantasy_module, team_fn_calls = fantasy_module_team_fn_calls_tuple
    for team, fn_calls in team_fn_calls.items():
        team_file = fantasy_module.__file__.replace("__init__.py", f"{team.result_file_name}.py")
        try_file = try_open_file_for_read(team_file)
        console.cons.print(f"Processing {team.name} with file {team_file}")
        if try_file.is_left():
            breakpoint()
        selections = try_file.value.read().split("\n")
        for round_fn, template_lines in fn_calls.items():
            updated, selections = _template_inserter(partial(_selections_insertion_point_indexes, round_fn),
                                                     selections,
                                                     template_lines)
        try_file.value.close()
        if updated:
            file_overwriter(selections, team_file)


def _template_inserter(start_end_fn: Callable, templated_file: List, inserted_lines: List):
    t_start, t_end = start_end_fn(templated_file)
    if t_start.is_left() or t_end.is_left():
        breakpoint()
        echo.echo(f"Template not found")
        return False, templated_file
    templated_file[t_start.value + 1:t_end.value] = inserted_lines
    return True, templated_file


def file_overwriter(lines: List, file_name: str):
    f = open(file_name, 'w')
    for line in lines:
        f.write(f"{line}\n")
    pass


def _selections_insertion_point_indexes(round_fn_name, selections):
    return (try_file_template_index(selections, f"# {round_fn_name}:START"),
            try_file_template_index(selections, f"# {round_fn_name}:END"))


def _results_insertion_point_indexes(results_fn_name, all_results):
    return (try_file_template_index(all_results, f"# {results_fn_name}:START"),
            try_file_template_index(all_results, f"# {results_fn_name}:END"))


def format_as_csv(draw_name, round_number, results):
    with open(f"{draw_name}-{round_number}.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['draw', 'match', 'winner', 'sets', 'match up'])
        for row in results:
            writer.writerow(row)


@monad.monadic_try()
def try_open_file_for_read(file_name):
    return open(file_name, 'r')


@monad.monadic_try()
def try_file_template_index(selections, insert_name):
    return selections.index(insert_name)
