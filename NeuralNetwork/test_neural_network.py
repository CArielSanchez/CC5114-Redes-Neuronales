import unittest
from NeuralNetwork import *
#Testea diferentes perceptrones.
class Test_Perceptron(unittest.TestCase):
   
    def test_Neural_Network(self):
        np.random.seed(42)

        # The 4 training examples by columns
        X = np.array([[0, 0, 1, 1],
                    [0, 1, 0, 1]])

        # The outputs of the XOR for every example in X
        Y = np.array([0, 1, 1, 0])

        # Set the hyperparameters
        n_x = 2     #No. of neurons in first layer
        n_h = 4     #No. of neurons in hidden layer
        n_y = 1     #No. of neurons in output layer

        #The number of times the model has to learn the dataset
        number_of_iterations = 10000
        learning_rate = 0.01

        # define a model 
        trained_parameters, cost_iteration = model(X, Y, n_x, n_h, n_y, number_of_iterations, learning_rate)

        # Test 2X1 vector to calculate the XOR of its elements. 
        # You can try any of those: (0, 0), (0, 1), (1, 0), (1, 1)
        X_test = np.array([[0], [1]])
        y_predict = predict(X_test, trained_parameters)

        self.assertEqual(y_predict, 1)
        

if __name__=="__main__":
    unittest.main()