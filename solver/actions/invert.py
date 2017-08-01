from ..input_action import Action

class Invert(Action):

    def run(self, total, game):
        return total * -1
