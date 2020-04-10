import unittest
import pprint

from Statistics.Statistics import Statistics
from random import random

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(9)
        randomData = []
        i = 1
        while i < 6:
            randomData.append(random.randint(1,100))
            i += 1
        pprint.pprint(randomData)

        self.testData = randomData
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, 1.5)

if __name__ == '__main__':
    unittest.main()