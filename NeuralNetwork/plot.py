
import NeuralNetwork
import matplotlib.pyplot as plt
data_1 = NeuralNetwork.cost_iteration_data
print(data_1[1])
def print_cost(data):
    
    plt.plot(data[1],data[0],'ro')
    plt.show()
    return 0
print_cost(data_1)