import random
from GA.ga import *
from GA.Selector.Roulette import *
class Binary:
    def __init__(self,number_to_convert,number_genes,pop_size):
        self.n_convert=number_to_convert
        self.n_genes=number_genes
        self.pop_size=pop_size
        self.maxNum = 2**(self.n_genes)
    

    def fitness_bits(self, indv):
        result=0
        exp = 1
        for i in indv[::-1]:
            result += int(i) * exp
            exp *= 2
        return self.maxNum - abs(self.n_convert - result )
        
    def gen_factory(self):
        if(random.random() > 0.5):
            return '1'
        else:
            return '0'

    def sequence_bit_factory(self):
        r=[]
        for i in range(self.n_genes):
            r.append(self.gen_factory()) 
        return r

    def runGA(self):
        selector = Roulette(self.fitness_bits)
        print("Numero a Convertir", self.n_convert)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_bits,geneFactory=self.gen_factory,individualFactory= self.sequence_bit_factory,maxIter=1000,selector=selector,terminationCondition = lambda f : f == self.maxNum)
        fitPop, population,best_indv,avg_fit,max_fit= ga.run()

        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv)


a = Binary(4,3,10)
a.runGA()
