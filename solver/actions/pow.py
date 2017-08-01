from ..input_action import InputAction

class Pow(InputAction):

    def run(self, total, game):
        return total ** self._value
