from random import randint
import Knapsack_GeneticAlgorithm.Consts as Consts
from Knapsack_GeneticAlgorithm.CandidateSolution import CandidateSolution


class GeneticKnapsack:


    def __init__(self):

        self._currentGeneration = self._createInitialPopulation()

        self._sortIndividuals()

        self._fittest = self._currentGeneration[0]

        self._generation = 0

        self._populationSize = Consts.POPULATION_SIZE

        self._crossoverRate = Consts.CROSSOVER_RATE

        self._mutationRate = Consts.MUTATION_RATE

        self._KnapsackCapacity = Consts.KNAPSACK_CAPACITY

        self._availableItems = Consts.AVAILABLE_ITEMS


    def _sortIndividuals(self):

        for i in range(len(self._currentGeneration) - 1):

            for j in range(len(self._currentGeneration) - 1):

                if(self._currentGeneration[j].getTotalValue() < self._currentGeneration[j+1].getTotalValue()):

                    self._currentGeneration[j], self._currentGeneration[j + 1] = self._currentGeneration[j + 1], self._currentGeneration[j]

                elif(self._currentGeneration[j].getTotalValue() == self._currentGeneration[j+1].getTotalValue()
                     and self._currentGeneration[j].getTotalSize() > self._currentGeneration[j+1].getTotalSize()):

                    self._currentGeneration[j], self._currentGeneration[j + 1] = self._currentGeneration[j + 1], self._currentGeneration[j]


    def _createInitialPopulation(self):

        initialPopulation = []

        for i in range(Consts.POPULATION_SIZE):

            initialPopulation.append(CandidateSolution().randomSolution())

        return initialPopulation


    def _crossover(self, individual_A:CandidateSolution, individual_B:CandidateSolution):

        #child1, child2 = individual_A, individual_B

        child1, child2 = CandidateSolution()

        if randint(0,99) < self._crossoverRate * 100 :

            itemCount = len(individual_A.getItems())

            splitPoint = randint(0, itemCount - 1)

            for i in range(0, splitPoint):

                child1.setIsSelected(i, individual_A.isSelected(i))
                child2.setIsSelected(i, individual_B.isSelected(i))

            for i in range(splitPoint, itemCount):

                child1.setIsSelected(i, individual_B.isSelected(i))
                child2.setIsSelected(i, individual_A.isSelected(i))

            #child1.setIsSelectedList(individual_A.getIsSelectedList()[0:splitPoint] + individual_B.getIsSelectedList()[splitPoint:len(self._availableItems)])

            #child2.setIsSelectedList(individual_B.getIsSelectedList()[0:splitPoint] + individual_A.getIsSelectedList()[splitPoint:len(self._availableItems)])

        child1.fix()

        child2.fix()

        return child1, child2

    #TODO:: method is empty
    def _possibleMutation(self):

        return None


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


    def _createNewGeneration(self):

        new_generation = []

        #selecting first 5 Individuals as best solutions
        best_solutions_until_now = self._currentGeneration[0:5]

        for i in range(len(best_solutions_until_now) - 1):

            for j in range(1, len(best_solutions_until_now) - i):

                child = self._crossover(best_solutions_until_now[i], best_solutions_until_now[i + j])

                new_generation.append(child)

        self._currentGeneration = new_generation

        self._sortIndividuals()

        self._generation += 1


    def generate(self, generation_number):

        for i in range(generation_number):

            self._rouletteWheelSelection()


    def show(self):

        print("-----====== Generation : "+ str(self._generation))


        num = 1

        for i in self._currentGeneration:

            print("Solution (" + str(num) +") =>  <value : " + str(i.getTotalValue()) + "> , <size :" + str(i.getTotalSize()) + ">")

            num +=1

        print("\n----->>> Fittest solution : <value : " + str(self._fittest.getTotalValue()) + "> , <size : " + str(self._fittest.getTotalSize()) + ">")