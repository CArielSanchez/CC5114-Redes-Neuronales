import random
import sys
import numpy as np
class GeneticAlgoritm:
    
    def __init__(self,populationSize, mutationRate, fitness, geneFactory,individualFactory,maxIter,selector,terminationCondition):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.fitness = fitness
        self.geneFactory= geneFactory
        self.individualFactory = individualFactory
        self.maxIter= maxIter
        self.selector=selector
        self.terminationCondition = terminationCondition

    def initializePopulation(self):
        popSize = self.populationSize
        population = []
        #quizas desde 0-popSize
        for i in range(popSize):
            population.append(self.individualFactory())
        return population

    def selection(self,population):
        selected= self.selector.run(population)
        return selected

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
    
    def mutation(self,ind):
        mutate = ind
        sizeGenes = len(mutate)

        #Si el rand esta dentro de la taza de mutacion, mutamos si no no
        #Se realiza un swap aleatorio entre ciudades

        if(random.random()<= self.mutationRate):
            selectGenes = random.randint(0,sizeGenes-1)
            swapGen = random.randint(0,sizeGenes-1)
            swapCity = mutate[selectGenes]
            mutate[selectGenes] = mutate[swapGen]
            mutate[swapGen] = swapCity


        return mutate

    def run(self):
        print("Maximas Iteraciones: ", self.maxIter)

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

        print("Iteraciones: ",it)
        averFit=np.mean(fitPopulation)

        return fitPopulation,population,population[index],averFit,maxFit