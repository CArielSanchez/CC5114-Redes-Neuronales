from random import random,randint
from perceptron import Perceptron
##
def f_lin(x,mult,sum):
    return x*mult+sum
##
def training_1(P):
    x=randint(-100,100)
    y=randint(-100,100)
    r=x*2
    if y>r:
        P.learn(0,1,[x,y])
    if y<r:
        P.learn(1,0,[x,y])

def testing_1(P):
   
    x=randint(-50,50)
    y=randint(-50,50)
    r=P.run([x,y])
    
    if(y > x*2):
        return int(r==1)
            
    else:
        return int(r==0)
            

############################################ Exp ###############################################################################
def exp(n_training,n_test,p_lr=0.1):
    idem=0
    
    ##Crear un perceptron aleatorizado
    P = Perceptron()
    P.random_init(2)
    P.set_lr(p_lr)

    while(n_training):
        n_training -= 1
        training_1(P)
   
    while(n_test):
        n_test -= 1
        idem += testing_1(P)
    return idem
n=1000
c=0
while(n):
    n-=1
    c+=exp(1,100)                
print(c/1000)
    
