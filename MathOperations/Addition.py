class addition:

    @staticmethod
    def sum(augend, addend=None):
        if isinstance(augend, list):
            return addition.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList(valueList):
        result = 0
        for value in valueList:
            result = addition.sum(result, value)

        return result
