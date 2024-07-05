from . import player, entry
from tejos.util import error, console

from tejos.util import fn


class Set:
    def __init__(self, number, entry1, entry2):
        self.number = number
        self.entry1 = entry1
        self.entry2 = entry2
        self.games = []
        self.winner = None

    def __repr__(self):
        cls_name = self.__class__.__name__
        components = [f"{entry.player()}, {score}" for entry, score in self.games]
        return f"{cls_name}(number='{self.number}', games=[{', '.join(fn.remove_none(components))}]"


    def result_for_player(self, for_entry, score, allow_equal_games_in_set: bool = False):
        en = entry.find_player_from_entry(for_entry, self._entries())
        self.games.append((en, score))
        if self._set_completed():
            self.winner = self.determine_winner(allow_equal_games_in_set)
        return self

    def _entries(self):
        return [self.entry1, self.entry2]

    def _set_completed(self):
        return self.games and (len([g for pl, g in self.games]) == 2) and self._set_score_at_least_6()

    def _set_score_at_least_6(self):
        return [g[1] for g in self.games if g[1] >= 6]

    def determine_winner(self, allow_equal_games_in_set) -> bool | None:
        if not self._set_completed():
            return None
        en1, en1_games = self.games[0]
        en2, en2_games = self.games[1]
        if en1_games == en2_games:
            if allow_equal_games_in_set:
                console.print("Games are the same length, and allow-equal-games is set")
                return None
            else:
                raise error.ConfigException(f"{en1.player().name} games {en1_games} same as {en2.player().name} games {en2_games}")
        return en1 if en1_games > en2_games else en2
