class GraphModel:
    cached_tournament_graph = None
    cached_players_graph = None

    @classmethod
    def tournament_graph(cls):
        if not cls.cached_tournament_graph:
            from tejos import repo
            cls.cached_tournament_graph = repo.tournament_graph()
        return cls.cached_tournament_graph


    @classmethod
    def players_graph(cls):
        if not cls.cached_players_graph:
            from tejos import repo
            cls.cached_players_graph = repo.players_graph()
        return cls.cached_players_graph
