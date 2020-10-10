
import NeuralNetwork
import matplotlib.pyplot as plt
data_1 = NeuralNetwork.cost_iteration_data
print(data_1)
def last_prediction_cost(data):
    
    plt.plot(data[1],data[0],'ro')
    plt.show()
    return 0
last_prediction_cost(data_1)