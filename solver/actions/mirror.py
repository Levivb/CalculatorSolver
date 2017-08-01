from ..input_action import Action

class Mirror(Action):

    def run(self, total, game):
        result = total
        isNegative = True if result < 0 else False
        result = result * (-1 if isNegative else 1)

        result = str(result)
        result += result[::-1]

        result = int(result)
        return result * (-1 if isNegative else 1)
