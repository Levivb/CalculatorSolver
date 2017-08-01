from ..action import Action

class Inv10(Action):

    def run(self, total, game):
        result = total
        isNegative = True if result < 0 else False
        result = result * (-1 if isNegative else 1)

        result = list(str(result))
        result = [str(10-int(n) if n!='0' else 0) for n in result]
        result = int("".join(result))

        return result * (-1 if isNegative else 1)
