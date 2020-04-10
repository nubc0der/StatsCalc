from Calculator.Calculator import Calculator
from Statistics.Mean import Mean
from Statistics.Median import Median
from Statistics.Mode import Mode
from Statistics.PopulationCorrelation import PopulationCorrelation
from Statistics.Quartiles import Quartiles
from Statistics.Skewness import Skewness
from Statistics.Variance import Variance
from Statistics.StandardDeviation import StandardDeviation
from Statistics.MeanDeviation import MeanDeviation
from Random.RandomNoSeed import RandomNoSeed
from Random.RandomWithSeed import RandomWithSeed
from Random.RandomList import RandomList
from PopSamplingFunctions.SimpleSampling import SimpleSampling
from PopSamplingFunctions.SystematicSampling import SystematicSampling
from PopSamplingFunctions.ConfidenceInterval import ConfidenceInterval
from PopSamplingFunctions.MarginError import MarginError
from PopSamplingFunctions.Cochran import Cochran
from PopSamplingFunctions import SampleSizeKnown, SampleSizeUnknownPop


class Statistics(Calculator):

    def __init__(self):
        self.result = Mean.mean(data)

    def mean(self, data):
        return self.result

    def median(self, data):
        self.result = Median.median(data)
        return self.result

    def mode(self, data):
        self.result = Mode.mode(data)
        return self.result

    def var(self, data):
        self.result = Variance.variance(data)
        return self.result

    def std(self, data):
        self.result = StandardDeviation.standardDeviation(data)
        return self.result

    def mean_deviation(self, data):
        self.result = MeanDeviation.meanDeviation(data)
        return self.result

    def quart(self, data):
        self.result = Quartiles.quartiles(data)
        return self.result

    def skew(self, data):
        self.result = Skewness.skewness(data)
        return self.result

    def popCo(self, data, data2):
        self.result = PopulationCorrelation.popCor(data, data2)
        return self.result

    def randomNoSeedInt(self, a, b):
        self.result = RandomNoSeed.randomInt(a, b)
        return self.result

    def randomNoSeedDec(self, a, b):
        self.result = RandomNoSeed.randomDec(a, b)
        return self.result

    def randomWithSeedInt(self, sd, a, b):
        self.result = RandomWithSeed.randomInt(sd, a, b)
        return self.result

    def randomWithSeedDec(self, sd, a, b):
        self.result = RandomWithSeed.randomDec(sd, a, b)
        return self.result

    def randomListInt(self, a, b, lngth, sd):
        self.result = RandomList.listInt(a, b, lngth, sd)
        return self.result

    def randomListDec(self, a, b, lngth, sd):
        self.result = RandomList.listDec(a, b, lngth, sd)
        return self.result

    def SimpleSampling(self, sd, lst, rnge):
        self.result = SimpleSampling.generateSampling(sd, lst, rnge)
        return self.result

    def SystematicSampling(self, lst):
        self.result = SystematicSampling.systematicSampling(lst)
        return self.result

    def ConfidenceIntervalSample(self, conf, data, sd, higher):
        self.result = ConfidenceInterval.confidenceIntervalPop(conf, data, sd, higher)
        return self.result

    def MarginError(self, data, n):
        self.result = MarginError.marginError(data, n)
        return self.result

    def test_Cochran(self, sd, data, rnge):
        self.result = Cochran.cochran(sd, data, rnge)
        return self.result

    def test_SampleSizeUnknown(self, sd, data, percentage):
        self.result = SampleSizeUnknownPop.SampleSizeUnkownPop(sd, data, percentage)
        return self.result

    def test_SampleSizeknown(self, sd, data):
        self.result = SampleSizeKnown.SampleSizeKnownPop(sd, data)
        return self.result