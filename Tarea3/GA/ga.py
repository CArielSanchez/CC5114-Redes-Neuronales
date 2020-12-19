import random
import sys
import numpy as np
import Tarea3.arbol

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
        #quizas desde 0-popSize
        for i in range(popSize):
            population.append(self.individualFactory())
        return population

    # Select an individual of a set of individuals(population) using a selector

    def selection(self,population):
        selected= self.selector.run(population)
        return selected

    # Using two individuals, generate a new individual with both characteristics #Falta esta funcion

    def crossover(self,indA,indB):

        numeroTotalHojas = indA.getRaiz().numberHojas.()
        selectGenes = random.randint(0,sizeGenes-1)
        crossover = indA[:selectGenes]+ indB[selectGenes:]
        return crossover
    
    # Mutate a gen of an individual using the mutate rate

    def mutation(self,ind):
        mutate = ind
        if(random.random()<= self.mutationRate):
            nodo = self.geneFactory()
            mutate.setRandomNodo(mutate.getRaiz(),nodo)
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
        #averFit=np.mean(fitPopulation)

        return population[index],maxFit,fitnessList