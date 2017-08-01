from ..input_action import InputAction

class Append(InputAction):

    def run(self, total, game):
        return int(str(total) + str(self._value))
