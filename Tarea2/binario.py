import random
from GA.ga import *
from GA.Selector.Roulette import *
import matplotlib.pyplot as plt

# Class to find the binary form of a int number

class Binary:

    # Contructor of a Binary, receives:
    # number_to_convert: Its the number that we would like to convert
    # number_genes: Its the umber of genes used(length of the secret word)
    # pop_size: Its the population size

    def __init__(self,number_to_convert,number_genes,pop_size):
        self.n_convert=number_to_convert
        self.n_genes=number_genes
        self.pop_size=pop_size
        self.maxNum = 2**(self.n_genes)
    
    # Gets the fitness of an individual (of a set of bits)

    def fitness_bits(self, indv):
        result=0
        exp = 1
        for i in indv[::-1]:
            result += int(i) * exp
            exp *= 2
        return self.maxNum - abs(self.n_convert - result )
        
    # Generate a gen (from [0,1])

    def gen_factory(self):
        if(random.random() > 0.5):
            return '1'
        else:
            return '0'

    # Generate an individual

    def sequence_bit_factory(self):
        r=[]
        for i in range(self.n_genes):
            r.append(self.gen_factory()) 
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

#FitnessStudy(1000,10)
#PopulationStudy(1000,10,100)