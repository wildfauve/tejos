import io

from rich.console import Console
from rich.markdown import Markdown
from rich import print
from rich.panel import Panel
from rich.table import Table

green = "[green]"
blue = "[blue]"
hl = "[bold magenta]"
end_hl = "[/bold magenta]"

cons = Console()

def print(body: str):
    cons.print(body)

def terminal_console():
    return Console()

def table(title):
    return Table(title=title)

def md(markdown: str):
    return Markdown(markdown)


def to_string_console():
    return Console(file=io.StringIO(), width=120)


def panel():
    return Panel


def console_print(obj):
    print(obj)
