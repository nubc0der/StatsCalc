from Statistics.Covariance import Covariance
from Statistics.StandardDeviation import StandardDeviation
from Random.SelectWithSeed import WithSeed


class SampleCorrelation():
    def __init__(self):
        pass

    @staticmethod
    def correlation(sd, a, b):
        sample1 = SelectWithSeed.pickItem(sd, a, 10)
        sample2 = SelectWithSeed.pickItem(sd, b, 10)

        cov = Covariance.covariance(sample1, sample2)
        std1 = StandardDeviation.standardDeviation(sample1)
        std2 = StandardDeviation.standardDeviation(sample2)
        return cov / (std1 * std2)
