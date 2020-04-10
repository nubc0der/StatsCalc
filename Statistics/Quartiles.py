import numpy

class Quartiles:

    def __init__(self):
        pass

    @staticmethod
    def quartiles(data):
        q1 = numpy.quantile(data)
        q2 = numpy.quantile(data)
        q3 = numpy.quantile(data)

        return [a, b, c]



