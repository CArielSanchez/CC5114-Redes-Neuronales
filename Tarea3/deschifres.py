import random
from GA.ga import *
from GA.Selector.Roulette import *
from arbol import *

import matplotlib.pyplot as plt

# Class to find the binary form of a int number

class Deschiffres:

    # Contructor of a Binary, receives:
    # number_to_convert: Its the number that we would like to convert
    # number_genes: Its the umber of genes used(length of the secret word)
    # pop_size: Its the population size

    def __init__(self,target_number,set_of_numbers,number_genes,pop_size):

        self.target=target_number
        self.set_numbers = set_of_numbers
        self.set_operations= ['+','-', '*']
        self.n_genes=number_genes ## EL largo del set de numeros?
        self.pop_size=pop_size
        self.maxInt = 21474836
        
    
    
    # Gets the fitness of an individual (of a set of bits)

    def fitness_tree(self, indv):
        value = indv.evaluate(indv.getRaiz())

        return self.maxInt - abs(self.target -  value)
        
    # Generate a gen (from [0,1])

    def gen_factory(self):
        value1 = random.choice(self.set_numbers)
        value2 = random.choice(self.set_numbers)
        operation = random.choice(self.set_operations)
        leaf1 = Hoja(value1)
        leaf2 = Hoja(value2)
        nodo = Nodo(operation,leaf1,leaf2)
        return nodo


    # Generate an individual

    def sequence_bit_factory(self):

        raiz = self.gen_factory()
        arbol = Arbol(raiz)
        n_hojas = 2
        while n_hojas<len(self.set_numbers):
            nodo = self.gen_factory()
            arbol.addRandomNodo(arbol.getRaiz(), nodo)
            n_hojas +=1

        return arbol

    #Run the Genetical Algoritm, returns de best individual, his fits, and a list of the max. fitness over each iteration

    def runGA(self):
        selector = Roulette(self.fitness_tree)
        print("Numero a Obetener", self.target)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.2,fitness=self.fitness_tree,geneFactory=self.gen_factory,individualFactory= self.sequence_bit_factory,maxIter=1000,selector=selector,terminationCondition = lambda f : f == self.maxInt)
        best_indv,max_fit,fitnessList= ga.run()
        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv.imprimir(best_indv.getRaiz()))
        return max_fit,best_indv,fitnessList

des = Deschiffres(10,[1,2,3,4],4,10)
# arbol = des.sequence_bit_factory()
# print(arbol.imprimir(arbol.getRaiz()))
des.runGA()

#FitnessStudy(1000,25)