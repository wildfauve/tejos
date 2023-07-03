from typing import Callable
from dataclasses import dataclass
from enum import Enum


class TypeOfError(Enum):
    INITIALISAION = 'initialisation'


class ErrorSeverity(Enum):
    FATAL = 'fatal'
    WARNING = 'warning'


@dataclass
class ConfigError:
    type_of_error: TypeOfError
    message_fn: Callable
    error_severity: ErrorSeverity


def entry_mismatch_on_initialise_draw(draw_name):
    return (f"{draw_name}: No entries hav been setup as yet, or entries dont match the number of configured matches in 1st round")