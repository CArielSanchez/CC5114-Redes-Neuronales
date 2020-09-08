from random import random,randint
from ex1 import Perceptron
P = Perceptron()
P.random_init(2)
def example_learn(P):
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    r=x+2
    if y>r:
        P.learn(0,1,[x,y])
    if y<r:
        P.learn(1,0,[x,y])
n=10000
while(n):
    n -= 1
    example_learn(P)

print(P.run([6,6]))
