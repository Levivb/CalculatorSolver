from ..action import Action

class Truncate(Action):

    def run(self, total, game):
        if len(str(total)) == 1:
            return 1e9 #kill it
        result = total
        isNegative = True if result < 0 else False
        result = result * (-1 if isNegative else 1)

        result = int(str(result)[:-1])

        return result * (-1 if isNegative else 1)
