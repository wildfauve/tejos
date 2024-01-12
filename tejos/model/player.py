from typing import List, Tuple
from itertools import groupby
from enum import Enum

from rdflib import URIRef

from tejos import model
from tejos.players import atp_players, wta_players
from tejos.rdf import rdf_prefix
from tejos.util import tokeniser
from tejos.repo import repository
from tejos.util import monad, singleton, logger

from . import base


class MatchPlayerNumber(Enum):
    PLAYER1 = 1
    PLAYER2 = 2


class PlayerCache(singleton.Singleton):
    player_name_index = {}
    players = {}
    atp_players_module = atp_players
    wta_players_module = wta_players

    def clear(self):
        self.__class__.player_name_index = {}
        self.__class__.players = {}
        return self

    def get_by_name_or_klass(self, name=None, klass_name=None):
        if name:
            possible_hit = self.__class__.player_name_index.get(name, None)
        else:
            possible_hit = self.__class__.players.get(klass_name, None)
        if possible_hit and isinstance(possible_hit, str):
            return monad.Right(self.__class__.players[possible_hit])
        if not possible_hit:
            return monad.Left(None)
        return monad.Right(possible_hit)

    def add_to_cache(self, player):
        self.set_player_on_player_module(player)
        if self.get_by_name_or_klass(klass_name=player.klass_name).is_right():
            return monad.Right(player)
        self.__class__.players[player.klass_name] = player
        self.__class__.player_name_index[player.name] = player.klass_name
        monad.Right(player)

    def set_player_on_player_module(self, player):
        if player.tour_symbol == "ATP":
            setattr(self.__class__.atp_players_module, player.klass_name, player)
        elif player.tour_symbol == "WTA":
            setattr(self.__class__.wta_players_module, player.klass_name, player)
        else:
            breakpoint()
        pass


class Player:
    repo = model.GraphModel2().new(repository.PlayerRepo, model.GraphModel2.players_graph)
    player_cache = PlayerCache

    @classmethod
    def clear_cache(cls):
        cls.player_cache().clear()

    @classmethod
    def create(cls, name, tour_symbol: str, klass_name: str = None):
        cached_player = cls.cache_hit(name=name)
        if cached_player.is_right():
            breakpoint()
        klass_name = cls.format_player_klass_name(name)
        if cls.cls_search(klass_name=klass_name).is_right():
            breakpoint()
        return cls.new(name, tour_symbol, klass_name)

    @classmethod
    def new(cls, name, tour_symbol: str, klass_name: str, alt_names: List = None):
        cached_player = cls.cache_hit(name=name)
        if cached_player.is_right():
            return cached_player.value

        plr = cls.cls_search(name=name, alt_name=name)
        if plr.is_right():
            cls.build_player(plr.value)
        player = cls(name, tour_symbol, klass_name, alt_names)
        cls.player_cache().add_to_cache(player)
        cls.repo().upsert(player)
        return player

    @classmethod
    def loadall(cls):
        for plr in cls.repo().get_all():
            player = cls.build_player(plr)
            cls.player_cache().add_to_cache(player)
        pass

    @classmethod
    def load(cls, name: str = None, klass_name: str = None):
        cached_player = cls.cache_hit(name=name, klass_name=klass_name)
        if cached_player.is_right():
            logger.log(f"Player Cache Hit: {cached_player.value}")
            return cached_player.value

        plr = cls.cls_search(name=name, klass_name=klass_name, alt_name=name)
        if plr.is_left():
            logger.log(f"Player with Name {name} or klass_name {klass_name} not found")
            return None
        player = cls.build_player(plr.value)
        cls.player_cache().add_to_cache(player)
        return player

    @classmethod
    def build_player(cls, player_tuple):
        sub, name, tour_symbol, klass_name, alt_names = player_tuple
        return cls(name, tour_symbol, klass_name, alt_names, sub)

    @classmethod
    def cache_hit(cls, name=None, klass_name=None):
        return cls.player_cache().get_by_name_or_klass(name=name, klass_name=klass_name)

    @classmethod
    def cls_search(cls, name=None, klass_name=None, alt_name=None) -> monad.EitherMonad[Tuple]:
        plr = cls.repo().get_by_name_or_klass_name(name=name, klass_name=klass_name, alt_name=alt_name)
        if not plr:
            return monad.Left(plr)
        return monad.Right(plr)

    @classmethod
    def format_player_klass_name(cls, name):
        nm = name.rstrip().lstrip()
        if "." in nm:
            return tokeniser.string_tokeniser(nm, tokeniser.dot_splitter, tokeniser.special_char_set)
        return tokeniser.string_tokeniser(nm, tokeniser.sp_splitter, tokeniser.special_char_set)

    def __init__(self, name, tour_symbol: str, klass_name: str, alt_names: List = None, sub: URIRef = None):
        self.name = name
        self.subject = rdf_prefix.clo_te_ind_plr[klass_name] if not sub else sub
        self.tour_symbol = tour_symbol
        self.klass_name = klass_name
        self.alt_names = alt_names if alt_names else []

    def __hash__(self):
        return hash((self.name,))

    def __eq__(self, other):
        if not self or not other:
            breakpoint()
        return (self.name == other.name) and (self.klass_name == other.klass_name)

    def search_by_name(self, on_name):
        # if on_name == "Marc-Andrea Huesler" and "Huesler" in self.name:
        #     breakpoint()
        if self.__class__.format_player_klass_name(on_name) == self.klass_name:
            return self
        if self.name == on_name:
            return self
        if self.alt_names:
            # if (self._format_player_klass_name(on_name) in self.klass_name) or (
            #         self.klass_name in self._format_player_klass_name(on_name)):
            if any([alt_name == on_name for alt_name in self.alt_names]):
                return self
        return None

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, klass_name={self.klass_name})"
