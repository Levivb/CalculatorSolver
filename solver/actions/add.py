from ..input_action import InputAction

class Add(InputAction):

    def run(self, total, game):
        return total + self._value
