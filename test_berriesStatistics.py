from flask import json
import berriesStatistics

def test_getBerriesNames():
    with open("test_berries_list.json", "r") as test_berries:
        berriesInfo = json.load(test_berries)
        assert berriesStatistics.getBerriesNames(berriesInfo) == ["salac", "petaya"]

def test_getMinGrowthTime():
    assert berriesStatistics.getMinGrowthTime([1,2,3]) == 1

def test_getMedianGrowthTime():
    assert berriesStatistics.getMedianGrowthTime([5,6,7]) == 6

def test_getMaxGrowthTime():
    assert berriesStatistics.getMaxGrowthTime([5,6,7]) == 7

def test_getVarianceGrowthTime():
    assert berriesStatistics.getVarianceGrowthTime([5,6,7]) == 1

def test_getMeanGrowthTime():
    assert berriesStatistics.getMeanGrowthTime([5,6,7,8]) == 6.5

def test_getFrequencyGrowthTime():
    assert berriesStatistics.getFrequencyGrowthTime([5,5,6,7,7]) == {5:2, 6:1, 7:2}
