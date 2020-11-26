import random
from GA.ga_tsp import *
from GA.Selector.Roulette import *
import sys,math
class City:
    def __init__(self,name,latitude=0,longitude=0,maxpos=1000):
        self.name=name
        self.latitude=latitude
        self.longitude=longitude
        self.maxpos=maxpos
        
    def getDistance(self,toCity):
        lat_city,long_city = toCity.getCoordinate()
        dist = math.sqrt(( self.latitude - lat_city)**2 + (self.longitude - long_city)**2)
        return dist
    def toRandom(self):
        self.latitude=random.randint(0,self.maxpos)
        self.longitude=random.randint(0,self.maxpos)
    def getCoordinate(self):
        return self.latitude,self.longitude
    def getName(self):
        return self.name
class TravelingSalesman:
    def __init__(self,citys,number_genes,pop_size):
        self.citys=citys
        self.n_genes=number_genes
        self.pop_size=pop_size    
        self.maxNum=1000

    def fitness_city(self, indv):
        result=0
        for i in range(0,len(indv)-1):
            result+=indv[i].getDistance(indv[i+1])
        return (self.maxNum - result)/self.maxNum
        
    def gen_factory(self,citys= 0):
        if citys== 0:
            citys=self.citys
        r = random.randint(0,len(citys)-1)
        return citys[r]

    def sequence_city(self):
        elected_citys=[]
        copy_citys= self.citys.copy()
        for i in range(self.n_genes):
            elected_city =self.gen_factory(copy_citys)
            copy_citys.remove(elected_city)
            elected_citys.append(elected_city)
        return elected_citys

    def runGA(self):
        selector = Roulette(self.fitness_city)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_city,geneFactory=self.gen_factory,individualFactory= self.sequence_city,maxIter=10gi00,selector=selector,terminationCondition = lambda f : f == self.maxNum)
        fitPop, population,best_indv,avg_fit,max_fit= ga.run()

        print("Fit Value: ", max_fit)
        for b_i in best_indv:
            print("City", b_i.getName(), b_i.getCoordinate())

citys=[]
ncitys=3
for i in range(0,ncitys):
    city = City('C'+ str(i), 2*i , 2*i )
    citys.append( city )

a = TravelingSalesman(citys,ncitys,10)
a.runGA()
