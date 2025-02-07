import numpy as np
from random import randint
#Create a perceptron:
#opcional weigth,bias and lr(weigth of learning)
class Perceptron:
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

        if(sum(w_mult_input) + self.b > 0):
            return 1
        else:
            return 0
    #Algoritm of learning
    #real_output: ouput real
    #disered_output: output disered
    #input: data recived by the perceptron
    def learn(self,real_output,disered_output,input):
        diff=disered_output-real_output
        self.w = np.add(self.w , (np.array(input) * self.lr * diff))
        self.b= self.b + (self.lr * diff)

  
##Create a conj. of Perceptrons
class Gates:
    def __init__(self):
        self.NAND=Perceptron([-2, -2], 3)
    def Summing_Numbers(self,input_a,input_b):

        first_flag = self.NAND.run([input_a,input_b])

        second_flag_a = self.NAND.run([input_a,first_flag])
        second_flag_b = self.NAND.run([first_flag,input_b])

        r_sum = self.NAND.run([second_flag_a,second_flag_b])
        r_carry_bit = self.NAND.run([first_flag,first_flag])
        return(r_carry_bit,r_sum)
