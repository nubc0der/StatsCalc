from MathOperations.addition import Addition
from MathOperations.divison import Divsion

class Mean:
    def __init__(self):
        pass

    @staticmethod
    def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = Addition(total, num)
    return Divsion(num_values,total)