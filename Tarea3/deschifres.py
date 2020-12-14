import random
from GA.ga import *
from GA.Selector.Roulette import *
from arbol import *

import matplotlib.pyplot as plt

# Class to find the binary form of a int number

class Deschiffres:

    # Contructor of a Binary, receives:
    # number_to_convert: Its the number that we would like to convert
    # number_genes: Its the umber of genes used(length of the secret word)
    # pop_size: Its the population size

    def __init__(self,target_number,set_of_numbers,number_genes,pop_size):

        self.target=target_number
        self.set_numbers = set_of_numbers
        self.set_operations= ['+','-', '*','/']

        self.n_genes=number_genes ## EL largo del set de numeros?

        self.pop_size=pop_size
        
    
    
    # Gets the fitness of an individual (of a set of bits)

    def fitness_bits(self, indv):
        value = indv.evaluate(indv.getRaiz())

        return abs(self.target -  value)
        
    # Generate a gen (from [0,1])

    def gen_factory(self):
        value1 = random.choice(self.set_numbers)
        value2 = random.choice(self.set_numbers)
        operation = random.choice(self.set_operations)
        leaf1 = Hoja(value1)
        leaf2 = Hoja(value2)
        nodo = Nodo(operation,leaf1,leaf2)
        return nodo


    # Generate an individual

    def sequence_bit_factory(self):

        n_hojas = 0
        
        while n_hojas<len(self.set_numbers):
            
            nodo = self.gen_factory()

            n_hojas = nodo.numberHojas()

        return r

    # Run the Genetical Algoritm, returns de best individual, his fits, and a list of the max. fitness over each iteration

    def runGA(self):
        selector = Roulette(self.fitness_bits)
        print("Numero a Convertir", self.n_convert)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_bits,geneFactory=self.gen_factory,individualFactory= self.sequence_bit_factory,maxIter=1000,selector=selector,terminationCondition = lambda f : f == self.maxNum)

        best_indv,max_fit,fitnessList= ga.run()
        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv)
        return max_fit,best_indv,fitnessList

# Generate the binary number (str) of an integer number manually

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

# Variation of the max. fitness over the epoch

def FitnessStudy(N,popSize):
    nGenes = len(binarizar(N))
    a = Binary(N,nGenes,popSize)
    maxfit,bestindv,fitnessList = a.runGA()
    iterationsList=list(range(len(fitnessList)))
    plt.plot(iterationsList,fitnessList)
    plt.title("FITNESS vs EPOCH")
    plt.xlabel("N°EPOCH")
    plt.ylabel("FITNESS")
    plt.show()

# Varation of the n° of the iterations using differents population size

def PopulationStudy(N,popsizeInit,popsizeEnd):
    nGenes = len(binarizar(N))
    IterationList=[]
    popSizeList=[]
    for popSize in range(popsizeInit,popsizeEnd):
        a = Binary(N,nGenes,popSize)
        maxfit,bestindv,fitnessList = a.runGA()
        IterationList.append(len(fitnessList))
        popSizeList.append(popSize)
    plt.plot(popSizeList,IterationList)
    plt.title("Population Size vs Max.EPOCH")
    plt.xlabel("Size")
    plt.ylabel("N°EPOCH")
    plt.show()

#FitnessStudy(1000,25)
#PopulationStudy(1000,10,100)