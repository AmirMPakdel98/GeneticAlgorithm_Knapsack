from random import randint
import Knapsack_GeneticAlgorithm.Consts as Consts
from Knapsack_GeneticAlgorithm.CandidateSolution import CandidateSolution


class GeneticKnapsack:


    def __init__(self):

        self._currentGeneration = self._createInitialPopulation()

        self._sortIndividuals(self._currentGeneration)

        self._fittest = self._currentGeneration[0]

        self._generation = 0

        self._populationSize = Consts.POPULATION_SIZE

        self._elitism = Consts.ELITISM

        self._crossoverRate = Consts.CROSSOVER_RATE

        self._mutationRate = Consts.MUTATION_RATE

        self._KnapsackCapacity = Consts.KNAPSACK_CAPACITY

        self._availableItems = Consts.AVAILABLE_ITEMS


    def _sortIndividuals(self, generation):

        for i in range(len(generation) - 1):

            for j in range(len(generation) - 1):

                if(generation[j].getTotalValue() < generation[j+1].getTotalValue()):

                    generation[j], generation[j + 1] = generation[j + 1], generation[j]

                elif(generation[j].getTotalValue() == generation[j+1].getTotalValue()
                     and generation[j].getTotalSize() > generation[j+1].getTotalSize()):

                    generation[j], generation[j + 1] = generation[j + 1], generation[j]


    def _createInitialPopulation(self):

        initialPopulation = []

        for i in range(Consts.POPULATION_SIZE):

            initialPopulation.append(CandidateSolution().randomSolution())

        return initialPopulation


    def _crossover(self, individual_A:CandidateSolution, individual_B:CandidateSolution):

        if randint(0,99) < self._crossoverRate * 100 :

            child1 = CandidateSolution()

            child2 = CandidateSolution()

            splitPoint = randint(0, len(individual_A.getIsSelectedList()) -1)

            for i in range(0, splitPoint):

                child1.setIsSelected(i, individual_A.isSelected(i))
                child2.setIsSelected(i, individual_B.isSelected(i))

            for i in range(splitPoint, len(individual_A.getIsSelectedList())):

                child1.setIsSelected(i, individual_B.isSelected(i))
                child2.setIsSelected(i, individual_A.isSelected(i))


            child1.setIsSelectedList(child1.getIsSelectedList())

            child2.setIsSelectedList(child2.getIsSelectedList())

            self._possibleMutation(child1)

            self._possibleMutation(child2)

            if not child1.isValid() or not child2.isValid():
                print("not valid")


            return [child1, child2]

        else:

            return [individual_A,individual_B]


    def _possibleMutation(self, child:CandidateSolution):

        if randint(0, 99) < self._mutationRate * 100:

            mutationSize = self._mutationRate * 100000

            while child._solutionTotalWeight != child._knapsackCapacity and mutationSize > 0:

                randInt = randint(0, len(child._notPickedItems) - 1)

                child.addItem(randInt)

                mutationSize -= 1


    def _checkFittest(self):

        if (self._currentGeneration[0].getTotalValue() > self._fittest.getTotalValue() or
                        self._currentGeneration[0].getTotalValue() == self._fittest.getTotalValue() and self._currentGeneration[0].getTotalSize() < self._fittest.getTotalSize()):

            self._fittest = self._currentGeneration[0]


    def _rouletteWheelSelection(self):

        newGeneration = []

        sum = 0

        percentList = []

        i = 0

        for individual in self._currentGeneration:

            sum += individual.getTotalValue()

            for j in range(individual.getTotalValue()):

                percentList.append(i)

            i += 1

        for i in range(self._populationSize // 2):

            randInt1 = randint(0, len(percentList) - 1)

            randInt2 = randint(0, len(percentList) - 1)

            child1, child2 = self._crossover(self._currentGeneration[percentList[randInt1]], self._currentGeneration[percentList[randInt2]])

            newGeneration.append(child1)

            newGeneration.append(child2)

        self._generation += 1

        self._currentGeneration = newGeneration

        self._sortIndividuals()

        if (self._currentGeneration[0].getTotalValue() > self._fittest.getTotalValue() or
                        self._currentGeneration[0].getTotalValue() == self._fittest.getTotalValue() and self._currentGeneration[0].getTotalSize() < self._fittest.getTotalSize()):

            self._fittest = self._currentGeneration[0]


    def _tournamentSelection(self, tournamentSize:int):

        tournament = []

        for i in range(tournamentSize):

            contestant = self._currentGeneration[randint(0, self._populationSize -1)]

            tournament.append(contestant)

        # sorting tournament array
        self._sortIndividuals(tournament)

        # return 2 of the best individuals
        return [tournament[0],tournament[1]]


    def _createNewGeneration(self):

        new_generation = []

        #selecting first 5 Individuals as best solutions
        best_solutions_until_now = self._currentGeneration[0:5]

        for i in range(len(best_solutions_until_now) - 1):

            for j in range(1, len(best_solutions_until_now) - i):

                child = self._crossover(best_solutions_until_now[i], best_solutions_until_now[i + j])

                new_generation.append(child)

        self._currentGeneration = new_generation

        self._sortIndividuals(self._currentGeneration)

        self._generation += 1


    def generate_rouletteSelection(self, generation_number):

        for i in range(generation_number):

            self._rouletteWheelSelection()


    def generate_tournamentSelection(self, generation_number):

        for i in range(generation_number):

            newGeneration = []

            # putting the fittest individuals of current generation in the next one with elitism size
            for i in range(0, self._elitism -1):

                newGeneration.append(self._currentGeneration[i])

            for i in range(0, self._populationSize - self._elitism):

                winners = self._tournamentSelection(10)

                child1, child2 = self._crossover(winners[0], winners[1])

                newGeneration.append(child1)

                newGeneration.append(child2)

            self._sortIndividuals(newGeneration)

            # check newGeneration's size and set it az current generation
            self._currentGeneration = newGeneration[0:self._populationSize]

            self._generation += 1

            print("generation :" + str(self._generation))

            self._checkFittest()


    def show(self):

        print("-----====== Generation : "+ str(self._generation))


        num = 1

        for i in self._currentGeneration:

            print("Solution (" + str(num) +") =>  <value : " + str(i.getTotalValue()) + "> , <size :" + str(i.getTotalSize()) + ">")

            num +=1

        print("\n----->>> Fittest solution : <value : " + str(self._fittest.getTotalValue()) + "> , <size : " + str(self._fittest.getTotalSize()) + ">")

        self.saveFittest(self.showFittestItems())


    def showFittestItems(self):

        items = self._fittest.getItems()

        message = " fittest : ["

        for i in items:

            message += "<value : "+str(i.getValue())+", weight : "+str(i.getWeight())+"> "


        message += "]"

        print(message)

        return message


    def saveFittest(self, message):

        file = open("Fittest.txt",'w')

        file.write("----->>> Fittest solution : <value : " + str(self._fittest.getTotalValue()) + "> , <size : " + str(self._fittest.getTotalSize()) + ">")

        file.write("\n"+message)