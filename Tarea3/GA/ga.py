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

    def __init__(self,populationSize, mutationRate, fitness, geneFactory,individualFactory,maxIter,selector,terminationCondition,setsNumber):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.fitness = fitness
        self.geneFactory= geneFactory
        self.individualFactory = individualFactory
        self.maxIter= maxIter
        self.selector=selector
        self.terminationCondition = terminationCondition
        self.setsNumber = setsNumber

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
        n_hojas=indA.getRaiz().numberHojas()
        n= random.randint(1,n_hojas-1)
        while(True):
            indv=self.crossover_aux(n,indA,indB)
            
            if(indv!=False):
                break
            if(n==1):
                if(self.fitness(indA)>self.fitness(indB)):
                    #print(indA.imprimir(indA.getRaiz()))
                    return indA.copy()
                else:
                    #print(indB.imprimir(indA.getRaiz()))
                    return indB.copy()
            n= random.randint(1,n_hojas-1)
        return indv
       
    def crossover_aux(self,n_hojas,indA,indB):
        print(n_hojas)
        arbolA=indA.copy()
        arbolB=indB.copy()
        # print("arbol A "+ arbolA.imprimir(arbolA.getRaiz()))
        # print("arbol B "+ arbolB.imprimir(arbolB.getRaiz()))
        n_a=arbolA.findNodo_nHojas(arbolA.getRaiz(),n_hojas)
        n_b=arbolB.findNodo_nHojas(arbolB.getRaiz(),n_hojas)
        # print(n_a)   
        # print(n_b)
        if(n_a!=None and n_b!=None):
            #print("arbol inicial "+arbolA.imprimir(arbolA.getRaiz()))
            arbolA.replaceNodo(arbolA.getRaiz(),n_a,n_b)
            # print("arbol final "+arbolA.imprimir(arbolA.getRaiz()))
            return arbolA
        return False
    # Mutate a gen of an individual using the mutate rate

    def mutation(self,ind): #Podriamos intentar mutar solo una hoja tmbn, o en realidad Cambiar solo un valor del nodo/hoja
        mutate = ind
        print("arbol inicial "+mutate.imprimir(mutate.getRaiz()))
        if(random.random()<= self.mutationRate):
            nodo = self.geneFactory()
            mutate.setRandomNodo(mutate.getRaiz(),nodo)
        print("arbol final"+mutate.imprimir(mutate.getRaiz()))
        return mutate

    # def mutation_2(self,ind):
    #     mutate = ind
    #     if(random.random()<= self.mutationRate):
    #         nodo = self.geneFactory()
    #         mutate.setRandomNodo(mutate.getRaiz(),nodo)
    #     print("arbol final"+mutate.imprimir(mutate.getRaiz()))
    #     return mutate
    
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
            print(it)
        return population[index],maxFit,fitnessList
