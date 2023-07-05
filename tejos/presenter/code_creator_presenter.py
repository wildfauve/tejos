from typing import Dict
import csv

from tejos.util import echo, monad

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



def fantasy_score_template_inserter(fantasy_module_team_fn_calls_tuple: Dict):
    fantasy_module, team_fn_calls = fantasy_module_team_fn_calls_tuple
    for team, fn_calls in team_fn_calls.items():
        team_file = fantasy_module.__file__.replace("__init__.py", f"{team.result_file_name}.py")
        try_file = try_open_file_for_read(team_file)
        if try_file.is_left():
            breakpoint()
        selections = try_file.value.read().split("\n")
        updated = False
        for round_fn, template_lines in fn_calls.items():
            t_start, t_end = _insertion_point_indexes(selections, round_fn)
            if t_start.is_right() and t_end.is_right():
                selections[t_start.value+1:t_end.value] = template_lines
                updated = True
            else:
                echo.echo(f"Template not found for {team.name}, for round: {round_fn}")
        try_file.value.close()
        if updated:
            f = open(team_file, 'w')
            for line in selections:
                f.write(f"{line}\n")

def _insertion_point_indexes(selections, round_fn):
    return (try_file_template_index(selections, f"# {round_fn}:START"),
            try_file_template_index(selections, f"# {round_fn}:END"))

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