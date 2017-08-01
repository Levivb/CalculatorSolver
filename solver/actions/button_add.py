from ..input_action import InputAction

class ButtonAdd(InputAction):

    def run(self, total, game):
        addition = self._value
        applicables = ['add','subtract','multiply','divide','append']
        def addValue(actionName):
            action = game.actions[actionName]
            typeCheck = str(type(action))
            isApplicable = False
            for applicable in applicables:
                isApplicable = 'solver.actions.'+applicable+'.' in typeCheck
                if isApplicable:
                    break

            if not isApplicable:
                return actionName

            action.add_value(addition)
            return actionName

        # print (game.actions['add_2'].__dict__)
        [addValue(x) for x in game.actions]
        # print (game.actions['add_2'].__dict__)

        return total
