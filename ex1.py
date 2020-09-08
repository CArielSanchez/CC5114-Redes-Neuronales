import numpy as np
from random import randint
class Perceptron:
    def __init__(self,w=[],b=0,lr=0.1):
        self.w=w
        self.b=b
        self.lr=lr
        self.large=len(w)
    def run(self,input):
        #Multiplica el input con sus pesos
        w_mult_input= np.multiply(self.w,input)

        if(sum(w_mult_input) + self.b > 0):
            return 1
        else:
            return 0
    def learn(self,real_output,disered_output,input):
        diff=disered_output-real_output
        self.w = np.add(self.w , (np.array(input) * self.lr * diff))
        self.b= self.b + (self.lr * diff)

    def random_init(self,large):
        self.large=large
        self.w=[]
        self.b=0
        for x in range(0,large):
            self.w.append(randint(-2,2))
        self.b = (randint(-2,2))

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

