from random import randint
from Knapsack_GeneticAlgorithm import Consts


class CandidateSolution:

    def __init__(self):

        self._knapsackCapacity = Consts.KNAPSACK_CAPACITY

        self._fixRate = Consts.SOLUTION_FIX_RATE

        self._wholeItems = Consts.AVAILABLE_ITEMS.copy()

        self._notPickedItems = Consts.AVAILABLE_ITEMS.copy()

        self._items = []

        self._isSelectedList = self._createIsSelectedItemList()

        self._solutionTotalWeight = 0

        self._solutionTotalValue = 0


    def _createIsSelectedItemList(self):

        isSelected = []

        for i in self._notPickedItems:

            isSelected.append(False)

        return isSelected


    def getTotalValue(self):

        return self._solutionTotalValue


    def getTotalSize(self):

        return self._solutionTotalWeight


    def getItems(self):

        return self._items


    def isSelected(self, index):

        return self._isSelectedList[index]


    def getIsSelectedList(self):

        return self._isSelectedList


    def setIsSelected(self, index, isSelected:bool):

        self._isSelectedList[index] = isSelected



    def setIsSelectedList(self, isSelected:list):

        self._isSelectedList = isSelected

        self._solutionTotalValue = 0

        self._solutionTotalWeight = 0

        j = 0

        for i in isSelected:

            if i == True:

                self._solutionTotalValue += self._notPickedItems[j].getValue()

                self._solutionTotalWeight += self._notPickedItems[j].getWeight()

            j += 1


    def addItem(self, index):

        if (self._solutionTotalWeight + self._notPickedItems[index].getWeight() > self._knapsackCapacity):

            return False

        else:

            self._items.append(self._notPickedItems[index])

            self._isSelectedList[index] = True

            self._solutionTotalWeight += self._notPickedItems[index].getWeight()

            self._solutionTotalValue += self._notPickedItems[index].getValue()

            return True


    def randomSolution(self):

        solution = CandidateSolution()

        randInt = randint(0, len(self._notPickedItems) - 1)

        while solution.addItem(randInt):

            self._notPickedItems.pop(randInt)

            randInt = randint(0, len(self._notPickedItems) - 1)

        self.fix()

        return solution


    def fix(self):

        while self._solutionTotalWeight != self._knapsackCapacity or self._fixRate == 0:

            self.addItem(randint(0, len(self._notPickedItems) - 1))

            self._fixRate -= 1