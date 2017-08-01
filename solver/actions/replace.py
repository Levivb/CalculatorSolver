from ..input_action import InputAction

class Replace(InputAction):

    def _setup(self):
        super()._setup()
        self._value_end = super()._getInput('Give replace value')

    def get_identifier(self):
        return str(self._value) + '_' + str(self._value_end)

    def run(self, total, game):
        return int(str(total).replace(str(self._value), str(self._value_end)))
