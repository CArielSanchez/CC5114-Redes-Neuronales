import random
from GA.ga import *
from GA.Selector.Roulette import *
import sys
class City:
    def __init__(self,name,latitude,longitude):
        self.name=name
        self.latitude=latitude
        self.longitude=longitude
    def getDistance(self,toCity):
        
    
class TravelingSalesman:
    def __init__(self,citys,number_genes,pop_size):
        self.citys=citys
        self.n_genes=number_genes
        self.pop_size=pop_size    
        self.maxNum=sys.maxsize
        
    def fitness_bits(self, indv):
        result=0
        for i in range(0,len(indv)-1):
            result+=indv[i].getDistance(indv[i+1])
        return self.maxNum - result
        
    def gen_factory(self,citys):
        r = random.randint(0,len(citys)-1)
        return citys[r]

    def sequence_bit_factory(self):
        elected_citys=[]
        copy_citys= self.citys.copy()
        for i in range(self.n_genes):
            elected_city =self.gen_factory(copy_citys)
            copy_citys.remove(elected_city)
            elected_citys.append(elected_city)
        return elected_citys

    def runGA(self):
        selector = Roulette(self.fitness_bits)
        print("Numero a Convertir", self.n_convert)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_bits,geneFactory=self.gen_factory,individualFactory= self.sequence_bit_factory,maxIter=1000,selector=selector,terminationCondition = lambda f : f == self.maxNum)
        fitPop, population,best_indv,avg_fit,max_fit= ga.run()

        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv)


a = Binary(4,3,10)
a.runGA()
