import random
import sys
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
        self.selector()
        return 0

    def crossover(self,indA,indB):
        return 0
    
    def mutation(self,ind):
        return 0

    def run(self):
        
        it = 0
        maxFit = -1*sys.maxsize
        index = 0
        population = self.initializePopulation()

        while(self.terminationCondition(maxFit)==False or it<self.maxIter):
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


        return population[index],maxFit