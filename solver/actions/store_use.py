from ..action import Action

class StoreUse(Action):

    def __init__(self):
        super().__init__()
        self.type = 'use'

    def run(self, total, game):
        result = total

        if self.type == 'store':
            if result >= 0:
                game.saved_value = result
        elif self.type == 'use':
            if game.saved_value == None:
                return result

            isNegative = True if result < 0 else False
            result = result * (-1 if isNegative else 1)

            result = str(result)
            result += str(game.saved_value)

            result = int(result)
            return result * (-1 if isNegative else 1)

        return result
