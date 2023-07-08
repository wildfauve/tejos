from tejos import repo
class GraphModel:
    cached_graph = None

    @classmethod
    def init(cls, g):
        cls.cached_graph = g
        return cls

    @classmethod
    def graph(cls):
        if not cls.cached_graph:
            cls.init(g=repo.graph())
        return cls.cached_graph