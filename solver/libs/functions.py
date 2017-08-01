from glob import glob
import os

import importlib

def import_actions():
    for action in action_list():
        #my_module = importlib.import_module('solver.actions.'+action)
        exec('from solver.actions.' + action + ' import ' + action.capitalize())

def str_to_class(str):
    return getattr(sys.modules[__name__], str)


def action_list():
    result = []
    for file in glob('solver/actions/*.py'):
        action = os.path.splitext(os.path.basename(file))[0]
        result.append(action)
    return result
