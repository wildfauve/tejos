atp = "ao/players/atp_players.py"
wta = "ao/players/wta_players.py"

def update():
    pls = [_update(pl) for pl in list(open(wta, 'r')) if "Player(" in pl]
    breakpoint()

def _update(pl):
    klass_name, definition = pl.split(" = ")
    return f"{klass_name} = {definition.replace('**', klass_name)}"