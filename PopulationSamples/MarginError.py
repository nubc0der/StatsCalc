from StatisticTests.StandardDeviation import StandardDeviation
from StatisticTests.Zscore import Zscore
from MathOperations import Root

class MarginError():
    @staticmethod
    def marginError(data, n):
        zscore = Zscore(data)
        standardDeviation = StandardDeviation.StandardDeviation(data)
        MoE = zscore * (standardDeviation/(Root(n, 2)))
        return MoE