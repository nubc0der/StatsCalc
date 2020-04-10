from Statistics.Mean import Mean
from Statistics.StandardDeviation import StandardDeviation
from RandomG.PickSeed import PickSeedList
from MathOperations.Division import Division


class Zscore():
    def __init__(self):
        pass

    @staticmethod
    def zscore(sd, data):
        X = PickSeedList.pickSeed(sd, data)
        meanData = Mean.mean(data)
        sd = StandardDeviation.standardDeviation(data)
        z = Division.divide(X - meanData, sd)
        return z
