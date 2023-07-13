from tejos import repo

class GraphModel2:

    @classmethod
    def tournament_graph(cls):
        return repo.tournament_graph()

    @classmethod
    def fantasy_graph(cls):
        return repo.fantasy_graph()

    def new(self, repository, graph):
        self.repository = repository
        self.graph = graph
        self.repo_instance = None
        return self

    def __call__(self):
        if self.repo_instance:
            return self.repo_instance
        self.repo_instance = self.repository(self.graph())
        return self.repo_instance


class GraphModel:
    cached_tournament_graph = None
    cached_players_graph = None
    repo_instance = None

    @classmethod
    def clear_cache(cls):
        cls.cached_tournament_graph = None
        cls.cached_players_graph = None
        cls.repo_instance = None

    @classmethod
    def repository(cls):
        # if cls.repo_instance:
        #     return cls.repo_instance
        if not cls.repo_graph:
            breakpoint()
        return cls.repo(cls.repo_graph())
        # cls.repo_instance = inst
        # return inst

    @classmethod
    def tournament_graph(cls):
        return repo.tournament_graph()


    @classmethod
    def players_graph(cls):
        return repo.players_graph()
