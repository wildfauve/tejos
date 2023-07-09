from rdflib import Graph

class GraphRepo:

    def __init__(self, graph: Graph):
        self.graph = graph


    def output(self):
        print(self.graph.serialize(format="ttl"))
        pass