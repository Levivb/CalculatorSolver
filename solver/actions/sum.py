from ..action import Action

class Sum(Action):

    def run(self, total, game):
        result = total
        isNegative = True if result < 0 else False
        result = result * (-1 if isNegative else 1)

        result = list(str(result))
        result = [int(n) for n in result]

        return sum(result) * (-1 if isNegative else 1)
