from rdflib import URIRef

from tejos.fantasy import points_strategy

def test_strategy_to_subject():
    strategy = points_strategy.WinNumSetsLossMaxSets(points_strategy.Points21Half, points_strategy.DoublePerRound())
    sub = strategy.subject()

    assert sub.toPython() == 'https://clojos.io/ontology/FantasyTennis/FantasyPointsStrategy/WinNumSetsLossMaxSets/Points21Half/DoublePerRound'

def test_strategy_from_subject():
    sub = URIRef('https://clojos.io/ontology/FantasyTennis/FantasyPointsStrategy/WinNumSetsLossMaxSets/Points21Half/DoublePerRound')

    strategy = points_strategy.PointsStrategyCalculator.build(sub)

    assert strategy.subject() == sub


def test_strategy_from_components():
    expected_sub = URIRef('https://clojos.io/ontology/FantasyTennis/FantasyPointsStrategy/WinNumSetsLossMaxSets/Points21Half/DoublePerRound')

    strategy = points_strategy.PointsStrategyCalculator.build(("WinNumSetsLossMaxSets", "Points21Half", "DoublePerRound"))

    assert strategy.subject() == expected_sub
