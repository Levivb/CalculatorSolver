from solver.action import Action

class InputAction(Action):

    def __init__(self):
        super().__init__()
        self._value = 0
        self._setup()

    def _setup(self):
        self._value = self._getInputInt()

    def get_identifier(self):
        return self._value

    def add_value(self, value):
        self._value += value

    def _getInputInt(self, message=None):
        userChoice = None
        while userChoice == None:
            try:
                userChoice = int(self._getInput(message))
            except ValueError:
                userChoice = None
                continue
        return userChoice

    def _getInput(self, message=None):
        if message == None:
            message = 'Give value'
        return input(message + ': ')
