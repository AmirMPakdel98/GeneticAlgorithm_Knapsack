from random import randint
from Knapsack_GeneticAlgorithm import Consts


class CandidateSolution:

    def __init__(self):

        self._knapsackCapacity = Consts.KNAPSACK_CAPACITY

        self._fixTime = Consts.SOLUTION_FIX_TIME

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

            if i == True and not self._solutionTotalWeight + self._wholeItems[j].getWeight() > self._knapsackCapacity:

                self._solutionTotalValue += self._wholeItems[j].getValue()

                self._solutionTotalWeight += self._wholeItems[j].getWeight()

                self._items.append(self._wholeItems[j])

                self._notPickedItems.remove(self._wholeItems[j])

            j += 1


    def findItem(self, id):

        for i in range(len(self._wholeItems) - 1 ):

            if self._wholeItems[i].getId() == id:

                return i

        return None


    def addItem(self, index):

        if (self._solutionTotalWeight + self._notPickedItems[index].getWeight() > self._knapsackCapacity):

            return False

        else:

            self._items.append(self._notPickedItems[index])

            self._isSelectedList[self._notPickedItems[index].getId()] = True

            self._solutionTotalWeight += self._notPickedItems[index].getWeight()

            self._solutionTotalValue += self._notPickedItems[index].getValue()

            self._notPickedItems.pop(index)

            return True


    def removeItem(self, id):

        index = self.findItem(id)

        self._isSelectedList[index] = False

        self._notPickedItems.append(self._wholeItems[index])

        self._solutionTotalWeight -= self._wholeItems[index].getWeight()

        self._solutionTotalValue -= self._wholeItems[index].getValue()

        for i in range(len(self._items)-1):

            if self._items[i].getId() == id:

                self._items.pop(i)


    def randomSolution(self):

        solution = CandidateSolution()

        randInt = randint(0, len(solution._notPickedItems) - 1)

        while solution.addItem(randInt):

            randInt = randint(0, len(solution._notPickedItems) - 1)

        solution.fix()

        if not solution.isValid():

            print("not valid")
            str1 = "["
            for i in solution.getItems():
                str1 += str(i.getId()) + " , "
            str1 += "]"
            print(str1)


        return solution


    def isValid(self):

        for i in range(len(self._items) - 1):

            for j in range(i+1, len(self._items) - 1):

                if self._items[i].getId() == self._items[j].getId():

                    return False

        return True


    def fix(self):

        while self._solutionTotalWeight != self._knapsackCapacity and self._fixTime > 0:

            length = len(self._notPickedItems)

            randInt = randint(0, len(self._notPickedItems) - 1)

            if self.addItem(randInt):

                if length == len(self._notPickedItems):

                    print("WTF")


            self._fixTime -= 1