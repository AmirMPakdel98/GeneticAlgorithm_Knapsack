

class Item:
    indexCounter = 0

    def __init__(self, value, weight):

        self._id = Item.indexCounter

        Item.indexCounter += 1

        self._value = value

        self._weight = weight

    def getId(self):

        return self._id

    def getValue(self):

        return self._value

    def getWeight(self):

        return self._weight