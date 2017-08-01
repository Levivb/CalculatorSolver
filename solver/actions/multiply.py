from ..input_action import InputAction

class Multiply(InputAction):

    def run(self, total, game):
        return total * self._value
