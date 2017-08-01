import sys
import re

from solver.game import Game
from solver.actions.add import Add
from solver.actions.append import Append
from solver.actions.button_add import ButtonAdd
from solver.actions.divide import Divide
from solver.actions.inv10 import Inv10
from solver.actions.invert import Invert
from solver.actions.mirror import Mirror
from solver.actions.multiply import Multiply
from solver.actions.pow import Pow
from solver.actions.replace import Replace
from solver.actions.reverse import Reverse
from solver.actions.shift import Shift
from solver.actions.store_use import StoreUse
from solver.actions.subtract import Subtract
from solver.actions.truncate import Truncate
from solver.actions.sum import Sum

class Solver:

    def __init__(self):
        self.__game = Game()
        self.__state = None
        self.__has_store_button = False
        self.__setup()

    def __setup(self):
        print ("""What do you want to do?
        [0] Add button
        [1] Solve
        [2] Cancel
        """)

        userChoice = None
        while True:
            try:
                userChoice = int(input('Chose an action: '))
            except ValueError:
                userChoice = None
                continue

            if userChoice == 2:
                self.__state = 'cancel'
                return
            elif userChoice == 1:
                self.__state = 'solve'
                return
            else:
                self.__add_button()


    def __add_button(self):
        message = "What button do you want to add?\n"
        for actionIndex, action in enumerate(self.__game.available_actions()):
            message += '[' + str(actionIndex) + '] ' + action + "\n"

        print (message)

        userChoice = None
        while userChoice not in range(len(self.__game.available_actions())):
            try:
                userChoice = int(input('Chose a button: '))
            except ValueError:
                userChoice = None
                continue

            actionName = self.__game.available_actions()[userChoice]
            actionClassName = re.sub('_.',lambda x: x.group()[1].upper(), actionName)
            actionClassName = actionClassName[0].upper() + actionClassName[1:]

            action = getattr(sys.modules[__name__], actionClassName)()
            identifier = str(action.get_identifier())
            key = actionName + ('_' + identifier if identifier else '')
            self.__game.add_action(key, action)

            if actionName == 'store_use':
                self.__has_store_button = True


    def run(self):
        if self.__state != 'solve':
            return

        if len(self.__game.actions) == 0:
            print ("No buttons to press")
            return

        print ('solving')
        pool = list(self.__game.actions.keys())

        combinationKeySets = self.__combinate(pool, self.__game.moves)
        if self.__has_store_button == True:
            #since the store action doesn't count for a move it's added to the combinationSets after these have been generated
            storeAction = StoreUse()
            storeAction.type = 'store'
            self.__game.add_action('store_init', storeAction)
            # print (combinationKeySets)
            combinationKeySets = self.__combinateWithStore(combinationKeySets)
            # print (combinationKeySets)
            # print ("-"*10)

        self.__game.backup()
        found = False
        for combinationKeys in combinationKeySets:
            self.__game.restore_backup()
            newTotal = self.__game.start
            # print (combinationKeys)
            for combinationKey in combinationKeys:
                # print (combinationKey)
                newTotal = self.__game.actions[combinationKey].run(newTotal, self.__game)

                if not isinstance(newTotal, int) or len(str(newTotal)) > 6:
                    #should always be int and calculator cannot handle more than 6 digits
                    break

                # print(newTotal)
                if newTotal > 0 and self.__game.portal_in != None and self.__game.portal_out != None:
                    result = list(str(newTotal))
                    while len(result) - 1 >= self.__game.portal_in:
                        multipler = pow(10, self.__game.portal_out) #keep base the same (when adding number to second index = *10)
                        index = len(result) - self.__game.portal_in - 1
                        toAdd = result.pop(index)
                        toAdd = int(toAdd) * multipler
                        # print(result)
                        result = int("".join(result))
                        result += toAdd
                        result = list(str(result))
                        # print(result)
                    newTotal = int("".join(result))

                if newTotal == self.__game.end:
                    print (combinationKeys)
                    found = True
                    if not self.__game.find_all:
                        break;
            # print("-----")
            if found and not self.__game.find_all:
                break

        if not found:
            print ("Solution not found :(")


    def __combinate(self, pool, combinationLength):
        #stored to speed processing
        poolSize = len(pool)
        currentCombination = 0
        result = []#[[]]*(poolSize**combinationLength)

        #set all indexes to zero as starter
        indexes = [0]*combinationLength
        while(indexes[0] < poolSize): #if the first index is bigger then poolSize, we are done

            #determine the current permutation
            combination = []
            for i in range(0, combinationLength):
                combination.append(pool[indexes[i]])
            result.append(combination) #append to combination list
            currentCombination += 1


            #increment indexes
            indexes[-1] += 1
            i = combinationLength - 1
            while indexes[i] == poolSize and i > 0: #if increment overflows
                indexes[i-1] += 1 #increment previous index
                indexes[i] = 0 #set current index to zero
                i -= 1
        return result

    def __combinateWithStore(self, combinationKeySets):
        def removeSetsWithoutStore(combinationKeySet):
            return 'store_use' in combinationKeySet
        combinationKeySets = [combinationKeySet for combinationKeySet in combinationKeySets if removeSetsWithoutStore(combinationKeySet)]

        newCombinationKeySets = []
        for combinationKeySet in combinationKeySets:
            storeUsages = combinationKeySet.count('store_use') #count the amount of store_use usages
            indexes = [None]*storeUsages #initialize as None, to allow store_init to occure only once
            indexes[0] = 0 #need to store_init at least once
            storeUseIndexes = [index for index, actionName in enumerate(combinationKeySet) if actionName == 'store_use'] #get the indices of the store_use usages

            # print ('####'*5)
            # print(combinationKeySet)

            while(indexes[0] <= storeUseIndexes[0]): #continue until all store_inits are inserted in each index before store_use
                newCombinationKeySet = list(combinationKeySet) #copy list to insert store_inits
                #loop in reversed order since inserting actions in the list shifts the indexes later on. Reversing it places the last actions to be placed first, so the action at the beginning isn't placed yet. preventing the shift in index
                for i in indexes[::-1]:
                    if i == None:
                        continue
                    newCombinationKeySet.insert(i, 'store_init')
                newCombinationKeySets.append(newCombinationKeySet)
                # print(newCombinationKeySet)

                # print('index_before', indexes)
                indexes[-1] = indexes[-1] + 1 if indexes[-1] != None else storeUseIndexes[-2] + 1 #start index after previous store_use button and continue from there
                i = storeUsages - 1
                while indexes[i] == storeUseIndexes[i]+1 and i > 0: #if index hits next store_use
                    # print('index_between_before', indexes)
                    indexes[i-1] = indexes[i-1] + 1 if indexes[i-1] != None else storeUseIndexes[i-2] + 1 #increment previous index
                    indexes[i] = None #set current index to zero
                    # print('index_between_after', indexes)
                    i -= 1
                # print('index_after', indexes)


        return newCombinationKeySets
