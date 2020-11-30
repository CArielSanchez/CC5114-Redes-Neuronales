import random
from GA.ga_tsp import *
from GA.Selector.Roulette import *
import sys,math
import matplotlib.pyplot as plt
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
    def getDistanceZero(self):
        dist = math.sqrt(( self.latitude)**2 + (self.longitude )**2)
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
        self.maxNum=0
    def initMaxNum(self):
        dist=0
        for c in self.citys:
            distanciazero=c.getDistanceZero()
            if dist < distanciazero:
                dist=distanciazero
        self.maxNum=self.n_genes*dist*10          

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
        self.initMaxNum()
        selector = Roulette(self.fitness_city)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_city,geneFactory=self.gen_factory,individualFactory= self.sequence_city,maxIter=1000,selector=selector,terminationCondition = lambda f : f >= 0.98)
        best_indv,max_fit,fitnessList= ga.run()
        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv)
        return max_fit,best_indv,fitnessList


def FitnessStudy(ncitys,popSize):
    citys=[]
    for i in range(0,ncitys):
        city = City('C'+ str(i), 2*i , 2*i )
        citys.append( city )
    nGenes = ncitys
    a = TravelingSalesman(citys,nGenes,popSize)
    maxfit,bestindv,fitnessList = a.runGA()
    iterationsList=list(range(len(fitnessList)))
    plt.plot(iterationsList,fitnessList)
    plt.title("FITNESS vs EPOCH")
    plt.xlabel("N°EPOCH")
    plt.ylabel("FITNESS")
    plt.show()
#FitnessStudy(5,10)
def PopulationStudy(ncitys,popsizeInit,popsizeEnd):
    citys=[]
    for i in range(0,ncitys):
        city = City('C'+ str(i), 2*i , 2*i )
        citys.append( city )
    nGenes = ncitys
    IterationList=[]
    popSizeList=[]
    for popSize in range(popsizeInit,popsizeEnd):
        a = TravelingSalesman(citys,nGenes,popSize)
        maxfit,bestindv,fitnessList = a.runGA()
        IterationList.append(len(fitnessList))
        popSizeList.append(popSize)
    plt.plot(popSizeList,IterationList)
    plt.title("Population Size vs Max.EPOCH")
    plt.xlabel("Size")
    plt.ylabel("N°EPOCH")
    plt.show()
PopulationStudy(5,5,50)

