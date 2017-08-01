from glob import glob
import os
import copy

class Game:

    def __init__(self):
        setup = {
            'start': None,
            'end': None,
            'moves': None
        }

        for var in setup:
            while setup[var] == None:
                i = None
                try:
                    i = int(input('Give '+var+'-number? '))
                except ValueError:
                    pass
                if type(i) == int:
                    setup[var] = i

        self.__backup = {}
        self.actions = {}
        self.find_all = False
        self.start = setup['start']
        self.end = setup['end']
        self.moves = setup['moves']
        self.saved_value = None
        self.portal_in = None
        self.portal_out = None

        showAll = input('Show all solutions? (takes longer) [N/y]')
        if showAll.lower() == 'y':
            self.find_all = True

        hasPortals = input('Portals available? [N/y]')
        if hasPortals.lower() == 'y':
            self.portal_in = int(input('Give portal-enter index? ')) #zero-based
            self.portal_out = int(input('Give portal-exit index? ')) #zero-based

        self._availableActions = []
        for file in glob('solver/actions/*.py'):
            action = os.path.splitext(os.path.basename(file))[0]
            # if action[0]=='_' #ability to add hidden actions
                # continue
            self._availableActions.append(action)


    def available_actions(self):
        return self._availableActions


    def add_action(self, key, action):
        self.actions[key] = action

    def backup(self):
        self.__backup['actions'] = copy.deepcopy(self.actions)

    def restore_backup(self):
        # print (self.actions['add_2'].__dict__)
        self.actions = copy.deepcopy(self.__backup['actions'])
