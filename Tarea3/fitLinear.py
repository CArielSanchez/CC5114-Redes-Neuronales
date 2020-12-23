from GA.gaLinear import *
from GA.Selector.Roulette import *
from arbol import *
import numpy as np
import matplotlib.pyplot as plt

# Class FitLinear to find the function that fits a set of points

class FitLinear:

    # Contructor of a Fit linear, receives:
    # set_of_points: Its the sets of the points that are used to find the function
    # pop_size: Its the population size

    # Also the class has the atribbutes:
    # set_operations: Are the operations allowed to compute
    # maxNum: Its the max number allowed to compute, in this case the number to compute are [0,1,2,3,4,5,6,7,8,9]
    # maxInt: Its a number to replace inf.

    def __init__(self,set_of_points,pop_size):
        self.set_points = set_of_points
        self.set_operations= ['+','-', '*','/']
        self.pop_size=pop_size
        self.maxNum = 10
        self.maxInt = 21474836
        
    
    
    # Gets the fitness of an individual (of an tree evaluated of each point)

    def fitness_tree(self, indv):
        try:
            fit = []
            for i in (self.set_points):
                value = indv.evaluatePoint(indv.getRaiz(),i[0])
                fit.append(abs(value-i[1]))
            fitness = self.maxInt - np.mean(fit)
        except ZeroDivisionError:
            fitness = 0
        finally:
            return fitness
        
    # Generate a random nodo with the number and 'x', and the sets of operations

    def gen_factory(self):
        lists=list(range(self.maxNum))
        lists.append('x')
        value1 = random.choice(lists)
        value2 = random.choice(lists)
        operation = random.choice(self.set_operations)
        leaf1 = Hoja(value1)
        leaf2 = Hoja(value2)
        nodo = Nodo(operation,leaf1,leaf2)
        return nodo


    # Generate an individual with 1 node

    def sequence_bit_factory(self):

        raiz = self.gen_factory()
        arbol = Arbol(raiz)
        return arbol

    #Run the Genetical Algoritm, returns de best individual, his fits, and a list of the max. fitness over each iteration

    def runGA(self):
        selector = Roulette(self.fitness_tree)
        print("Puntos a encontrar", self.set_points)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.2,fitness=self.fitness_tree,geneFactory=self.gen_factory,individualFactory= self.sequence_bit_factory,maxIter=1000,selector=selector,terminationCondition = lambda f : f == self.maxInt, setsPoints  = self.set_points, setsOperations = self.set_operations,maxNum = self.maxNum)
        best_indv,max_fit,fitnessList= ga.run()
        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv.imprimir(best_indv.getRaiz()))
        return max_fit,best_indv,fitnessList


# Variation of the max. fitness over the epoch
def FitnessStudy(popSize,points):
    a = FitLinear(points,popSize)
    maxfit,bestindv,fitnessList = a.runGA()
    iterationsList=list(range(len(fitnessList)))
    plt.plot(iterationsList,fitnessList)
    plt.title("FITNESS vs EPOCH")
    plt.xlabel("N°EPOCH")
    plt.ylabel("FITNESS")
    plt.show()

# Varation of the n° of the iterations using differents population size

def PopulationStudy(popsizeInit,popsizeEnd,points):
    
    IterationList=[]
    popSizeList=[]
    for popSize in range(popsizeInit,popsizeEnd,10):
        a = FitLinear(points,popSize)
        maxfit,bestindv,fitnessList = a.runGA()
        IterationList.append(len(fitnessList))
        popSizeList.append(popSize)
    plt.plot(popSizeList,IterationList)
    plt.title("Population Size vs Max.EPOCH")
    plt.xlabel("Size")
    plt.ylabel("N°EPOCH")
    plt.show()


def Graph_Func(points):
    xs = []
    ys = []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])

    a = FitLinear(points,10)
    maxfit,bestindv,fitnessList = a.runGA()
    y_prima=[]
    for x in xs:
        y_prima.append(bestindv.evaluatePoint(bestindv.getRaiz(),x))
    plt.plot(xs,ys,'ro')
    plt.plot(xs,y_prima)
    plt.title("Function vs Points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

# Points pre sets:
# [1,2],[2,6],[3,12],[4,20],[5,30],[6,42],[7,56],[8,72],[9,90]
# [1,2],[2,6],[3,12],[4,20],[5,30]

FitnessStudy(30,[[1,2],[2,6],[3,12],[4,20],[5,30]])
PopulationStudy(10,100,[[1,21],[2,22],[3,23],[4,24],[5,25]])
Graph_Func([[1,12],[2,16],[3,22],[4,30],[5,40],[6,52],[7,66],[8,82],[9,100]])
