import random
import string
from GA.ga import *
from GA.Selector.Roulette import *
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
        fitPop, population,best_indv,avg_fit,max_fit= ga.run()

        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv)

word = "gato"
popSize = 10
nGenes = len(word)
a = SecretWord(word,nGenes,popSize)
a.runGA()
