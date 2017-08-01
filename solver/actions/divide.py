from ..input_action import InputAction

class Divide(InputAction):

    def run(self, total, game):
        result = total / self._value
        return int(result) if result.is_integer() else result
