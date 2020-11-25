
class GeneticAlgoritm:
    
    def __init__(self,populationSize, mutationRate, fitness, geneFactory,individualFactory,maxIter,selector):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.fitness = fitness
        self.geneFactory= geneFactory
        self.individualFactory = individualFactory
        self.maxIter= maxIter
        self.selector=selector
        self.fit
        self.max_fit
