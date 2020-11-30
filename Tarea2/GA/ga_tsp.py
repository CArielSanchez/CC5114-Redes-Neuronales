import random
import sys
import numpy as np

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

    def __init__(self,populationSize, mutationRate, fitness, geneFactory,individualFactory,maxIter,selector,terminationCondition):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.fitness = fitness
        self.geneFactory= geneFactory
        self.individualFactory = individualFactory
        self.maxIter= maxIter
        self.selector=selector
        self.terminationCondition = terminationCondition

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
        sizeGenes = len(indA)

        selectGenes = random.randint(1,sizeGenes-1)
        posicion = random.randint(0,sizeGenes-1-selectGenes)

        child=indA[posicion:posicion+selectGenes]

        j=0
        i=0
        while i < sizeGenes:
            if indB[j] in child:
                j+=1
                continue
            if (posicion<=i and i< posicion+selectGenes):
                i+=1
                continue
            indA[i]=indB[j]
            i+=1
            j+=1
        return indA
    
    # Mutate a gen of an individual using the mutate rate

    def mutation(self,ind):
        mutate = ind
        sizeGenes = len(mutate)

        #Se realiza un swap aleatorio entre ciudades

        if(random.random()<= self.mutationRate):
            selectGenes = random.randint(0,sizeGenes-1)
            swapGen = random.randint(0,sizeGenes-1)
            swapCity = mutate[selectGenes]
            mutate[selectGenes] = mutate[swapGen]
            mutate[swapGen] = swapCity


        return mutate

    # Run the Genetical Algoritm, returns de best individual, his fits, and a list of the max. fitness over each iteration

    def run(self):
        it = 0
        maxFit = -1*sys.maxsize
        population = self.initializePopulation()
        fitnessList=[]
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

        #averFit=np.mean(fitPopulation)

        return population[index],maxFit,fitnessList