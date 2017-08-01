from ..input_action import InputAction

class Subtract(InputAction):

    def run(self, total, game):
        return total - self._value
