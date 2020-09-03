class Perceptron:
    def __init__(self,w1,w2,b):
        self.w1=w1
        self.w2=w2
        self.b=b
    def run(self,input_a,input_b):
        if(self.w1 * input_a + self.w2* input_b + self.b > 0):
            return 1
        else:
            return 0

class Gates:
    def __init__(self):
        self.NAND=Perceptron(-2, -2, 3)
    def Summing_Numbers(self,input_a,input_b):

        first_flag = self.NAND.run(input_a,input_b)

        second_flag_a = self.NAND.run(input_a,first_flag)
        second_flag_b = self.NAND.run(first_flag,input_b)

        r_sum = self.NAND.run(second_flag_a,second_flag_b)
        r_carry_bit = self.NAND.run(first_flag,first_flag)
        return(r_carry_bit,r_sum)

