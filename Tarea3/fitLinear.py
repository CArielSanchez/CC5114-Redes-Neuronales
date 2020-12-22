from GA.gaLinear import *
from GA.Selector.Roulette import *
from arbol import *
import numpy as np
import matplotlib.pyplot as plt

# Class to find the binary form of a int number

class FitLinear:

    # Contructor of a Binary, receives:
    # number_to_convert: Its the number that we would like to convert
    # number_genes: Its the umber of genes used(length of the secret word)
    # pop_size: Its the population size

    def __init__(self,set_of_points,pop_size):
        self.set_points = set_of_points
        self.set_operations= ['+','-', '*','/']
        self.pop_size=pop_size
        self.maxNum = 10
        self.maxInt = 21474836
        
    
    
    # Gets the fitness of an individual (of a set of bits)
    # (x,y) = (4,6)

    def fitness_tree(self, indv): ## Si evaluate tiene division por 0, podriamos tirarlo a infinito
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
        
    # Generate a gen (from [0,1])

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


    # Generate an individual

    def sequence_bit_factory(self):

        raiz = self.gen_factory()
        arbol = Arbol(raiz)
        # n_hojas = 2
        # while n_hojas<len(self.n_genes):
        #     nodo = self.gen_factory()
        #     arbol.addRandomNodo(arbol.getRaiz(), nodo)
        #     n_hojas +=1

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

# linear = FitLinear([[1,2],[2,6],[3,12],[4,20],[5,30]],10)
# linear.runGA()


# Variation of the max. fitness over the epoch
def FitnessStudy(popSize):
    a = FitLinear([[1,2],[2,6],[3,12],[4,20],[5,30]],popSize)
    maxfit,bestindv,fitnessList = a.runGA()
    iterationsList=list(range(len(fitnessList)))
    plt.plot(iterationsList,fitnessList)
    plt.title("FITNESS vs EPOCH")
    plt.xlabel("N°EPOCH")
    plt.ylabel("FITNESS")
    plt.show()
# Varation of the n° of the iterations using differents population size

def PopulationStudy(popsizeInit,popsizeEnd):
    
    IterationList=[]
    popSizeList=[]
    for popSize in range(popsizeInit,popsizeEnd,10):
        a = FitLinear([[1,21],[2,22],[3,23],[4,24],[5,25]],popSize)
        maxfit,bestindv,fitnessList = a.runGA()
        IterationList.append(len(fitnessList))
        popSizeList.append(popSize)
    plt.plot(popSizeList,IterationList)
    plt.title("Population Size vs Max.EPOCH")
    plt.xlabel("Size")
    plt.ylabel("N°EPOCH")
    plt.show()

#FitnessStudy(30)
#PopulationStudy(10,100)
#[1,2],[2,6],[3,12],[4,20],[5,30],[6,42],[7,56],[8,72],[9,90]
#[1,2],[2,6],[3,12],[4,20],[5,30]
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

#Graph_Func([[1,12],[2,16],[3,22],[4,30],[5,40],[6,52],[7,66],[8,82],[9,100]])
