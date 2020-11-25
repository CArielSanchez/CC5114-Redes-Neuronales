import random
class binary:
    def __init__(self,number_to_convert,number_genes):
        self.n_convert=number_to_convert
        self.n_genes=number_genes

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
        ga= GA(pop_size,mutationRate=0.1,fitness=fitness_bits,individual_factory= self.sequence_bit_factory(),gene_factory=self.gen_factory(),termination_condition = lambda f : f == 0, silent =False,max_iter=10)
        best_fitness_list,avg_list,best_indv = ga.run()
        print(''.join(best_individual))