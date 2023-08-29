from tejos import repo


def test_new_style_triples(configure_repo2):
    g = configure_repo2.graph('players_graph')

    xx = list(g.triples((None, None, None)))
    breakpoint()
    assert len(list(g.triples((None, None, None)))) == 32
