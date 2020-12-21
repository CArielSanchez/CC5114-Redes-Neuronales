import random
from GA.gaLinear import *
from GA.Selector.Roulette import *
from arbol import *
import numpy as np
import matplotlib.pyplot as plt

# Class to find the binary form of a int number

class FitLinear:

    # Contructor of a Binary, receives:
    # number_to_convert: Its the number that we would like to convert
    # number_genes: Its the umber of genes used(length of the secret word)
    # pop_size: Its the population size

    def __init__(self,set_of_points,number_genes,pop_size):
        self.set_points = set_of_points
        self.set_operations= ['+','-', '*','/']
        self.n_genes=number_genes ## EL largo del set de numeros?
        self.pop_size=pop_size
        self.maxNum = 10
        self.maxInt = 21474836
        
    
    
    # Gets the fitness of an individual (of a set of bits)
    # (x,y) = (4,6)

    def fitness_tree(self, indv): ## Si evaluate tiene division por 0, podriamos tirarlo a infinito
        try:
            fit = []
            for i in (self.set_points):
                value = indv.evaluatePoint(indv.getRaiz(),i[0])
                fit.append(abs(value-i[1]))
            fitness = self.maxInt - np.mean(fit)
        except ZeroDivisionError:
            fitness = 0
        finally:
            return fitness
        
    # Generate a gen (from [0,1])

    def gen_factory(self):
        lists=list(range(self.maxNum))
        lists.append('x')
        value1 = random.choice(lists)
        value2 = random.choice(lists)
        operation = random.choice(self.set_operations)
        leaf1 = Hoja(value1)
        leaf2 = Hoja(value2)
        nodo = Nodo(operation,leaf1,leaf2)
        return nodo


    # Generate an individual

    def sequence_bit_factory(self):

        raiz = self.gen_factory()
        arbol = Arbol(raiz)
        # n_hojas = 2
        # while n_hojas<len(self.n_genes):
        #     nodo = self.gen_factory()
        #     arbol.addRandomNodo(arbol.getRaiz(), nodo)
        #     n_hojas +=1

        return arbol

    #Run the Genetical Algoritm, returns de best individual, his fits, and a list of the max. fitness over each iteration

    def runGA(self):
        selector = Roulette(self.fitness_tree)
        print("Puntos a encontrar", self.set_points)
        ga = GeneticAlgoritm(self.pop_size,mutationRate=0.2,fitness=self.fitness_tree,geneFactory=self.gen_factory,individualFactory= self.sequence_bit_factory,maxIter=1000,selector=selector,terminationCondition = lambda f : f == self.maxInt, setsPoints  = self.set_points, setsOperations = self.set_operations,maxNum = self.maxNum)
        best_indv,max_fit,fitnessList= ga.run()
        print("Fit Value: ", max_fit)
        print("Best Individual", best_indv.imprimir(best_indv.getRaiz()))
        return max_fit,best_indv,fitnessList

linear = FitLinear([[1,2],[2,6],[3,12],[4,20],[5,30]],2,10)
linear.runGA()

# hoja1 = Hoja('x')
# hoja2 = Hoja(1)
# nodo = Nodo()

# linear.fitness_tree
# arbol = des.sequence_bit_factory()
# print(arbol.imprimir(arbol.getRaiz()))
# des.runGA()
#print(des.fitness_tree(arbol))
#FitnessStudy(1000,25)

