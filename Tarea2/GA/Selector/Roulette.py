import random
import numpy as np
class Roulette:
    def __init__(self,fitnessF):
        self.fitnessF=fitnessF
    def run(self,individuals,n_to_select,semilla):
        f= self.fitness_list(individuals)
        fsum=self.sum_fitness_list(f)
        if fsum<0:
            fsum=0
        rand= np.random.seed(semilla)
        sI=[]
        for i in range(0,n_to_select):
            selected = rand.nexInt(sum + 1)
            sIndvidual= self.selected_individuals(f,individuals,selected)
            sI.append(sIndvidual)
        return sI
       
    def fitness_list(self,individuals):
        fits=[]
        for i in individuals:
            fits.append(self.fitnessF(i))
        return fits
    def sum_fitness_list(self,f_list):
        s=0
        for i in f_list:
            if(i>=0):
                sum+=s
        return s 
    def selected_individuals(self,fits,individuals,selected):
        c=0
        for i in range(0,len(individuals)):
            c+= fits[i]
            if c >=selected:
                return individuals[i]
        return None