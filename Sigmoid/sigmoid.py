import numpy as np
from random import randint
import math
#Create a perceptron:
#opcional weigth,bias and lr(weigth of learning)
class Sigmoid:
    def __init__(self,w=[],b=0,lr=0.1):
        self.w=w
        self.b=b
        self.lr=lr
        self.large=len(w)
    def set_lr(self,lr):
        self.lr=lr
    def set_b(self,b):
        self.b=b
    def set_w(self,w):
        self.w=w

    #Set a perceptron on ramdom values
    #large: large of the input recived for the perceptron.
    def random_init(self,large):
        self.large=large
        w=[]
        for x in range(0,large):
            w.append(randint(-2,2))
        b = (randint(-2,2))
        self.set_b(b)
        self.set_w(w)

    
    #Ejecuta un perceptron
    #input: data recived by the perceptron
    def run(self,input):
        #Multiplica el input con sus pesos
        w_mult_input= np.multiply(self.w,input)
        sumatory= sum(w_mult_input) + self.b
        r = 1/(1 + math.exp(-sumatory))
        return r
    #Algoritm of learning
    #real_output: ouput real
    #disered_output: output disered
    #input: data recived by the perceptron
    def learn(self,real_output,disered_output,input):
        diff=disered_output-real_output
        self.w = np.add(self.w , (np.array(input) * self.lr * diff))
        self.b= self.b + (self.lr * diff)