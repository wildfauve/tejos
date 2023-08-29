from tejos import repo

class GraphModel2:

    @classmethod
    def tournament_graph(cls):
        return repo.graph('tejos_graph')

    @classmethod
    def fantasy_graph(cls):
        return repo.graph('fantasy_graph')

    @classmethod
    def players_graph(cls):
        return repo.graph('players_graph')


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
