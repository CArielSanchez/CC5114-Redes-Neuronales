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

    def __init__(self,populationSize, mutationRate, fitness, geneFactory,individualFactory,maxIter,selector,terminationCondition,setsPoints,setsOperations, maxNum):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.fitness = fitness
        self.geneFactory= geneFactory
        self.individualFactory = individualFactory
        self.maxIter= maxIter
        self.selector=selector
        self.terminationCondition = terminationCondition
        self.setsPoints = setsPoints
        self.setsOperations = setsOperations
        self.maxNum = maxNum

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
        n_hojas_a=indA.getRaiz().numberHojas()
        n_hojas_b=indB.getRaiz().numberHojas()

        n1 = random.randint(1,n_hojas_a)
        n2 = random.randint(1,n_hojas_b)
        while(True):
            indv=self.crossover_aux(n1,n2,indA,indB)
            if(indv!=False):
                break
            if(n1==1 or n2==1):
                if(self.fitness(indA)>self.fitness(indB)):
                    #print(indA.imprimir(indA.getRaiz()))
                    return indA.copy()
                else:
                    #print(indB.imprimir(indA.getRaiz()))
                    return indB.copy()
            n1 = random.randint(1,n_hojas_a)
            n2 = random.randint(1,n_hojas_b)
        return indv
       
    def crossover_aux(self,n_hojas_a,n_hojas_b,indA,indB):
        
        #print(n_hojas)
        arbolA=indA.copy()
        arbolB=indB.copy()
        # print(n_hojas_a)
        # print(n_hojas_b)
        # print("arbol")
        # print("arbol A "+ arbolA.imprimir(arbolA.getRaiz()))
        # print("arbol B "+ arbolB.imprimir(arbolB.getRaiz()))
        n_a=arbolA.findNodo_nHojas(arbolA.getRaiz(),n_hojas_a)
        n_b=arbolB.findNodo_nHojas(arbolB.getRaiz(),n_hojas_b)
        # print("nodos")
        # print(n_a)   
        # print(n_b)
        if(n_a!=None and n_b!=None):
           #s print("entro!!!!!!!!!!!")
            #print("arbol inicial "+arbolA.imprimir(arbolA.getRaiz()))
            if(random.random() > 0.5):
                arbolA.addRandomNodo(arbolA.getRaiz(),n_b)
            else:
                arbolA.replaceNodo(arbolA.getRaiz(),n_a,n_b)
            # print("arbol final "+arbolA.imprimir(arbolA.getRaiz()))
            return arbolA
        
        return False
    # Mutate a gen of an individual using the mutate rate

    def mutation(self,ind): #Podriamos intentar mutar solo una hoja tmbn, o en realidad Cambiar solo un valor del nodo/hoja
        mutate = ind
        # print("arbol inicial "+mutate.imprimir(mutate.getRaiz()))
        if(random.random()<= self.mutationRate):
            rand = random.random()
            if (rand < 0.33):
                nodo = self.geneFactory()
                mutate.setRandomNodo(mutate.getRaiz(),nodo)
            elif(rand < 0.66):
                lists = list(range(self.maxNum))
                lists.append('x')
                mutate.setRandomHoja(mutate.getRaiz(),random.choice(lists))
            else:
                mutate.setRandomOperation(mutate.getRaiz(),mutate.getRaiz().numberHojas()-1,self.setsOperations)
        # print("arbol final"+mutate.imprimir(mutate.getRaiz()))
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
