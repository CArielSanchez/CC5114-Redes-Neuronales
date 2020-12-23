#import __init__
import random
import sys
import numpy as np
#import arbol

# Class for Genetic Algoritm 

class GeneticAlgoritm:
    
    # Constructor for Genetic Algoritm, receives:
    # populationSize: Its the number of individuals per iteration
    # mutationRate: Its the rate of the process of mutation
    # fitness: Its the fitness function
    # geneFactory: Its a function that creates a gene
    # individualFactory: Its a function that creates an individual
    # maxIter: Its the max iteration over the epochs of the Genetic Algoritm
    # selector: Its an object of the selector used in the Algoritm
    # terminationCondition: Its the termination condition of the iterations/epochs
    # setsNumber: Its the sets of numbers used to compute a tree.
    # setsOperations: Its the sets of operations used to compute a tree.

    def __init__(self,populationSize, mutationRate, fitness, geneFactory,individualFactory,maxIter,selector,terminationCondition,setsNumber,setsOperations):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.fitness = fitness
        self.geneFactory= geneFactory
        self.individualFactory = individualFactory
        self.maxIter= maxIter
        self.selector=selector
        self.terminationCondition = terminationCondition
        self.setsNumber = setsNumber
        self.setsOperations = setsOperations

    # Initialize the population, creating each individual for the population Size.

    def initializePopulation(self):
        popSize = self.populationSize
        population = []
        for i in range(popSize):
            population.append(self.individualFactory())
        return population

    # Select an individual of a set of individuals(population) using a selector

    def selection(self,population):
        selected= self.selector.run(population)
        return selected

    # Using two individuals, generate a new individual with both characteristics 
    
    def crossover(self,indA,indB):
        n_hojas=indA.getRaiz().numberHojas()
        n= random.randint(1,n_hojas-1)
        while(True):
            indv=self.crossover_aux(n,indA,indB)
            
            if(indv!=False):
                break
            if(n==1):
                if(self.fitness(indA)>self.fitness(indB)):
                    return indA.copy()
                else:
                    return indB.copy()
            n= random.randint(1,n_hojas-1)
        return indv
       
    # Aux function for crossover

    def crossover_aux(self,n_hojas,indA,indB):
        arbolA=indA.copy()
        arbolB=indB.copy()
        n_a=arbolA.findNodo_nHojas(arbolA.getRaiz(),n_hojas)
        n_b=arbolB.findNodo_nHojas(arbolB.getRaiz(),n_hojas)
        if(n_a!=None and n_b!=None):
            arbolA.replaceNodo(arbolA.getRaiz(),n_a,n_b)
            return arbolA
        return False

    # Mutate a gen of an individual using the mutate rate

    def mutation(self,ind):
        mutate = ind
        if(random.random()<= self.mutationRate):
            rand = random.random()
            if (rand < 0.33):
                nodo = self.geneFactory()
                mutate.setRandomNodo(mutate.getRaiz(),nodo)
            elif(rand < 0.66):
                mutate.setRandomHoja(mutate.getRaiz(),random.choice(self.setsNumber))
            else:
                mutate.setRandomOperation(mutate.getRaiz(),mutate.getRaiz().numberHojas()-1,self.setsOperations)
        return mutate
    
    # Run the Genetical Algoritm, returns de best individual, his fits, and a list of the max. fitness over each iteration

    def run(self):
        fitnessList=[]
        it = 0
        maxFit = -1*sys.maxsize
        population = self.initializePopulation()

        while(self.terminationCondition(maxFit)==False and it<self.maxIter):

            maxFit = -1*sys.maxsize
            index = 0
            popSize = self.populationSize
            newPopulation = []
            fitPopulation = []
            for i in range(popSize):
                indv=self.mutation(self.crossover(self.selection(population),self.selection(population)))
                fit=self.fitness(indv)
                newPopulation.append(indv)
                fitPopulation.append(fit)

                if(maxFit<fit): 
                    index=i
                    maxFit = fit

            population=newPopulation
            it+=1
            fitnessList.append(maxFit)
            print(it)
        return population[index],maxFit,fitnessList
