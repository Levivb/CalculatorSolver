from ..input_action import InputAction

class Shift(InputAction):

    def _setup(self):
        self._value = self._getInput()

    def _getInput(self, message=None):
        if message == None:
            message = 'Give direction (<|>)'
        return super()._getInput(message)

    def run(self, total, game):
        result = total
        if self._value == '>' or self._value == '<':
            isNegative = True if result < 0 else False
            result = result * (-1 if isNegative else 1)

            result = list(str(result))

            if self._value == '>':
                result = [result[-1]] + result[:-1]
            elif self._value == '<':
                result.append(result.pop(0))

            result = int("".join(result))
            result = result * (-1 if isNegative else 1)

        return result
