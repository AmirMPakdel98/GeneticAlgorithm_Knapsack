from Knapsack_GeneticAlgorithm.Item import Item

KNAPSACK_CAPACITY = 30

POPULATION_SIZE = 100

ELITISM = 5 # 0 - population_size/2

CROSSOVER_RATE = 1.00 # 0.00 - 1.00

MUTATION_RATE = 0.20 # 0.00 - 0.50

SOLUTION_FIX_TIME = 2000 # higher is better but slower

AVAILABLE_ITEMS = [ # 45 items

    Item(10,2),
    Item(10,3),
    Item(10,5),
    Item(10,8),
    Item(10,9),
    Item(8,2),
    Item(8,4),
    Item(8,8),
    Item(8,10),
    Item(8,12),
    Item(7,1),
    Item(7,3),
    Item(7,3),
    Item(7,3),
    Item(7,6),
    Item(7,12),
    Item(7,18),
    Item(6,3),
    Item(6,4),
    Item(6,8),
    Item(6,8),
    Item(6,11),
    Item(6,14),
    Item(6,20),
    Item(5,3),
    Item(4,1),
    Item(4,3),
    Item(4,11),
    Item(4,16),
    Item(3,7),
    Item(3,9),
    Item(3,13),
    Item(2,1),
    Item(2,1),
    Item(2,7),
    Item(2,14),
    Item(2,20),
    Item(2,20),
    Item(1,1),
    Item(1,3),
    Item(1,8),
    Item(1,11),
    Item(0,3),
    Item(0,5),
    Item(0,9)
]