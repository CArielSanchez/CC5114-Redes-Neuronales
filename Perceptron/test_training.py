from perceptron_gym import Perceptron_Gym 
from random import randint
from perceptron import Perceptron

###Generate binary pairs, to be evaluated on diferents functions.
# name_func: Recive the type of the function "and,or,nand"
# iterations: number of data disired
def gen_bin_data(name_fun,iterations):
    data=[]
    A=randint(0,1)
    B=randint(0,1)
    dato=[A,B]
    d_output=0
    if(name_fun=="and"):
        d_output=int(dato[0] and dato[1])
    if(name_fun=="or"):
        d_output=int(dato[0] or dato[1])
    if(name_fun=="nand"):
        d_output=int(False==(dato[0] and dato[1]))
    data.append(dato)
    data.append(d_output)
    return data
###Generate data to be evaluated on a perceptron.
# func: Recive a function  to separate date
# iterations: number of data disired
def gen_data(func,iterations):
    data=[]
    for i in range(0,iterations):
        x=randint(-50,50)
        y=randint(-50,50)
        limit = func(x)
        dato=[x,y]
        desired_output=0
        if y > limit:
            desired_output=1
        data.append([dato,desired_output])
    return data




P = Perceptron()
P.random_init(2)

data1=gen_data(lambda x: x + 10 ,0)
data2=gen_data(lambda x: x +10 ,2)
data3=[]
n=1000

for i in range(0,n):
    data3.append(gen_data(lambda x: x + 10,1000))

Gym_P = Perceptron_Gym(data1)
Gym_P.training_(P)
j=Gym_P.general_exam(P,data2)
av=Gym_P.average_exam(P,data3)

