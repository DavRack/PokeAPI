import statistics
def getBerriesNames(berriesInfo):
    return list(map(lambda b: b["name"], berriesInfo))

def getMinGrowthTime(berriesGrowTime):
    return min(berriesGrowTime)

def getMedianGrowthTime(berriesGrowTime):
    return statistics.median(berriesGrowTime)

def getMaxGrowthTime(berriesGrowTime):
    return max(berriesGrowTime)

def getVarianceGrowthTime(berriesGrowTime):
    return statistics.variance(berriesGrowTime)

def getMeanGrowthTime(berriesGrowTime):
    return statistics.mean(berriesGrowTime)

def getFrequencyGrowthTime(berriesGrowTime):
    frequencyGrowthTable = {}

    for growthTime in berriesGrowTime:
        actualFrequency = frequencyGrowthTable.get(growthTime, 0)
        frequencyGrowthTable[growthTime] = actualFrequency + 1

    return frequencyGrowthTable
