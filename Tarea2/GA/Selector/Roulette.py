import random
import numpy as np

# Class for selection on Genetic Algoritm

class Roulette:

    # Constructor receives a Fitness Function

    def __init__(self,fitnessF):
        self.fitnessF=fitnessF
        
    # Run roulette algoritm receivins a set of individuals.

    def run(self,individuals):
        f= self.fitness_list(individuals)
        fsum=self.sum_fitness_list(f)
        selected = np.random.randint(fsum + 1)
        sIndividual= self.selected_individuals(f,individuals,selected)
        return sIndividual

    # Create a fitness list of a set of individuals
       
    def fitness_list(self,individuals):
        fits=[]
        for i in individuals:
            fits.append(self.fitnessF(i))
        return fits

    # Returns a sum of the fitness in a fitness list

    def sum_fitness_list(self,f_list):
        s=0
        for i in f_list:
                s+=i
        return s 

    # Select a individual using a Roulette algoritm over certains parameters.
    
    def selected_individuals(self,fits,individuals,selected):
        c=0
        for i in range(0,len(individuals)):
            c+= fits[i]
            if c >=selected:
                return individuals[i]
        return None