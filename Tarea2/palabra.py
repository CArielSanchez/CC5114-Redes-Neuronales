import random
import string
from GA.ga import *
from GA.Selector.Roulette import *
import matplotlib.pyplot as plt
class SecretWord:
    def __init__(self,secretWord,number_genes,pop_size):
        self.secretWord = secretWord
        self.n_genes = number_genes
        self.pop_size = pop_size
        

    def fitness_char(self, indv): #tengo que entregar negativo?
        charIguales = 0
        for i in range(self.n_genes):
            if(indv[i]== self.secretWord[i]):
                charIguales+=1

        charNormalizado = charIguales/self.n_genes
        return charNormalizado
        
    def gen_factory(self):
        return random.choice(string.ascii_lowercase)

    def sequence_char_factory(self):
        r=[]
        for i in range(self.n_genes):
            r.append(self.gen_factory()) 
        return r

    def runGA(self):
        selector = Roulette(self.fitness_char)
        print("Palabra a Encontrar", self.secretWord)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_char,geneFactory=self.gen_factory,individualFactory= self.sequence_char_factory,maxIter=10000,selector=selector,terminationCondition = lambda f : f == 1)
        best_indv,max_fit,fitnessList= ga.run()
        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv)
        return max_fit,best_indv,fitnessList
    
# word = "amarillo"
# popSize = 100
# nGenes = len(word)
# a = SecretWord(word,nGenes,popSize)
# a.runGA()
def FitnessStudy(word,popSize):
    nGenes = len(word)
    a = SecretWord(word,nGenes,popSize)
    maxfit,bestindv,fitnessList = a.runGA()
    iterationsList=list(range(len(fitnessList)))
    plt.plot(iterationsList,fitnessList)
    plt.title("FITNESS vs EPOCH")
    plt.xlabel("N°EPOCH")
    plt.ylabel("FITNESS")
    plt.show()

def PopulationStudy(word,popsizeInit,popsizeEnd):
    nGenes = len(word)
    IterationList=[]
    popSizeList=[]
    for popSize in range(popsizeInit,popsizeEnd):
        a = SecretWord(word,nGenes,popSize)
        maxfit,bestindv,fitnessList = a.runGA()
        IterationList.append(len(fitnessList))
        popSizeList.append(popSize)
    plt.plot(popSizeList,IterationList)
    plt.title("Population Size vs Max.EPOCH")
    plt.xlabel("Size")
    plt.ylabel("N°EPOCH")
    plt.show()
word = "amarillo"
PopulationStudy(word,10,100)
