import random
from GA.ga_tsp import *
from GA.Selector.Roulette import *
import sys,math
import matplotlib.pyplot as plt

# Class of one City

class City:

    # Contructor for a City, receives:
    # name: Name of the city
    # latitude: Latitude of the city
    # longitude: Longitude of the city
    # maxpos: Max position of a coordinate on a random city

    def __init__(self,name,latitude=0,longitude=0,maxpos=1000):
        self.name=name
        self.latitude=latitude
        self.longitude=longitude
        self.maxpos=maxpos
        
    # Get the euclidean distance between self city and an other city

    def getDistance(self,toCity):
        lat_city,long_city = toCity.getCoordinate()
        dist = math.sqrt(( self.latitude - lat_city)**2 + (self.longitude - long_city)**2)
        return dist
    # Get the distance between the coordinate (0,0) and the city

    def getDistanceZero(self):
        dist = math.sqrt(( self.latitude)**2 + (self.longitude )**2)
        return dist

    # Generate a random latitud and longitude of the city

    def toRandom(self):
        self.latitude=random.randint(0,self.maxpos)
        self.longitude=random.randint(0,self.maxpos)
    
    # Get the coordinate of the city

    def getCoordinate(self):
        return self.latitude,self.longitude
    
    # Get the name of the city

    def getName(self):
        return self.name

# Class for the Traveling Salesman Problem

class TravelingSalesman:

    # Contructor of the Traveling Salesman Problem, using Genetical Algoritm, receives:
    # citys: A sets of cities
    # number_genes: The number of genes for a set of cities (n° of cities)
    # pop_size: The size of the population

    def __init__(self,citys,number_genes,pop_size):
        self.citys=citys
        self.n_genes=number_genes
        self.pop_size=pop_size    
        self.maxNum=0

    # Initialize the max. number to normalize the fitness

    def initMaxNum(self):
        dist=0
        for c in self.citys:
            distanciazero=c.getDistanceZero()
            if dist < distanciazero:
                dist=distanciazero
        self.maxNum=self.n_genes*dist*10       

    # Gets the fitness of an individual (of a set of cities)   

    def fitness_city(self, indv):
        result=0
        for i in range(0,len(indv)-1):
            result+=indv[i].getDistance(indv[i+1])
        return (self.maxNum - result)/self.maxNum
        
    # Generate a gen (from a set of cities)

    def gen_factory(self,citys= 0):
        if citys== 0:
            citys=self.citys
        r = random.randint(0,len(citys)-1)
        return citys[r]
    
    # Generate an individual

    def sequence_city(self):
        elected_citys=[]
        copy_citys= self.citys.copy()
        for i in range(self.n_genes):
            elected_city =self.gen_factory(copy_citys)
            copy_citys.remove(elected_city)
            elected_citys.append(elected_city)
        return elected_citys

    # Run the Genetical Algoritm, returns de best individual, his fits, and a list of the max. fitness over each iteration

    def runGA(self):
        self.initMaxNum()
        selector = Roulette(self.fitness_city)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_city,geneFactory=self.gen_factory,individualFactory= self.sequence_city,maxIter=1000,selector=selector,terminationCondition = lambda f : f >= 0.98)
        best_indv,max_fit,fitnessList= ga.run()
        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv)
        return max_fit,best_indv,fitnessList

# Variation of the max. fitness over the epoch

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

# Varation of the n° of the iterations using differents population size

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

#FitnessStudy(5,10)
#PopulationStudy(5,5,50)

