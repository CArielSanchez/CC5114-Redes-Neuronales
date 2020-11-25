import random
from GA.ga import *
from GA.Selector.Roulette import *
class binary:
    def __init__(self,number_to_convert,number_genes,pop_size):
        self.n_convert=number_to_convert
        self.n_genes=number_genes
        self.pop_size=pop_size

    def fitness_bits(self, indv):
        result=0
        exp = 1
        for i in indv[::-1]:
            result += int(i) + exp
            exp *= 2
        return - abs(self.n_convert - result )
        
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
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.1,fitness=self.fitness_bits,geneFactory=self.gen_factory(),individualFactory= self.sequence_bit_factory,maxIter=100,selector=selector,terminationCondition = lambda f : f == 0)
        best_fitness_list,avg_list,best_indv = ga.run()

        print(''.join(best_indv))