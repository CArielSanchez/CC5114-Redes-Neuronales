import numpy as np

def sigmoid(z):
	return 1/(1 + np.exp(-z))



# Produce a neural network randomly initialized
#To do: revision matriz n° bias y w
def initialize_parameters(n_x, n_h, n_y):
	W1 = np.random.randn(n_h, n_x)
	b1 = np.zeros((n_h, 1))
	W2 = np.random.randn(n_y, n_h)
	b2 = np.zeros((n_y, 1))

	parameters = {
	"W1": W1,
	"b1" : b1,
	"W2": W2,
	"b2" : b2
	}
	return parameters

# Evaluate the neural network
def forward_prop(X, parameters):
  W1 = parameters["W1"]
  b1 = parameters["b1"]
  W2 = parameters["W2"]
  b2 = parameters["b2"]
  # Z value for Layer 1
  Z1 = np.dot(W1, X) + b1
  # Activation value for Layer 1
  A1 = np.tanh(Z1)

  # Z value for Layer 2
  Z2 = np.dot(W2, A1) + b2
  # Activation value for Layer 2

  A2 = sigmoid(Z2)

  cache = {
    "A1": A1,
    "A2": A2
  }
  return A2, cache

# Evaluate the error (i.e., cost) between the prediction made in A2 and the provided labels Y 
# We use the Mean Square Error cost function
def calculate_cost(A2, Y,m):
  # m is the number of examples
  cost = np.sum((0.5 * (A2 - Y) ** 2).mean(axis=1))/m
  sub_a2=np.squeeze(A2)
  sub_y=sub_a2-Y
  c=0
  for x in sub_y:
    if(abs(x)<0.5):
      c+=1
  accuracy=c/m
  return cost,accuracy

# Apply the backpropagation
def backward_prop(X, Y, cache, parameters,m):
  A1 = cache["A1"]
  A2 = cache["A2"]

  W2 = parameters["W2"]

  # Compute the difference between the predicted value and the real values
  dZ2 = A2 - Y
  dW2 = np.dot(dZ2, A1.T)/m
  db2 = np.sum(dZ2, axis=1, keepdims=True)/m
  # Because d/dx tanh(x) = 1 - tanh^2(x)
  dZ1 = np.multiply(np.dot(W2.T, dZ2), 1-np.power(A1, 2))
  dW1 = np.dot(dZ1, X.T)/m
  db1 = np.sum(dZ1, axis=1, keepdims=True)/m

  grads = {
    "dW1": dW1,
    "db1": db1,
    "dW2": dW2,
    "db2": db2
  }

  return grads

# Third phase of the learning algorithm: update the weights and bias
def update_parameters(parameters, grads, learning_rate):
  W1 = parameters["W1"]
  b1 = parameters["b1"]
  W2 = parameters["W2"]
  b2 = parameters["b2"]

  dW1 = grads["dW1"]
  db1 = grads["db1"]
  dW2 = grads["dW2"]
  db2 = grads["db2"]

  W1 = W1 - learning_rate*dW1
  b1 = b1 - learning_rate*db1
  W2 = W2 - learning_rate*dW2
  b2 = b2 - learning_rate*db2
  
  new_parameters = {
    "W1": W1,
    "W2": W2,
    "b1" : b1,
    "b2" : b2
  }

  return new_parameters

# model is the main function to train a model
# X: is the set (is a matrix)of training inputs
# Y: is the set (is a list) of training outputs
# n_x: number of inputs (this value impacts how X is shaped)
# n_h: number of neurons in the hidden layer
# n_y: number of neurons in the output layer (this value impacts how Y is shaped)
# Retunrs the parameters of the model and the error and accuracy of the model through the epochs
def model(X, Y, n_x, n_h, n_y, num_of_iters, learning_rate):
  
  #list that save the error,accuracy and epoch
  cost_iteration_data=[]
  ##Auxiliar list
  cost_list=[]
  accuracy_list=[]
  i_list=[]

  # m: No. of training examples
  m = X.shape[1] 

  parameters = initialize_parameters(n_x, n_h, n_y)

  for i in range(0, num_of_iters+1):
    a2, cache = forward_prop(X, parameters)
    cost,accuracy = calculate_cost(a2, Y,m)
    grads = backward_prop(X, Y, cache, parameters,m)
    parameters = update_parameters(parameters, grads, learning_rate)
    if(i%100 == 0):
      print('Cost after iteration# {:d}: {:f}'.format(i, cost))
    cost_list.append(cost)
    accuracy_list.append(accuracy)
    i_list.append(i)
  cost_iteration_data.append(cost_list)
  cost_iteration_data.append(accuracy_list)
  cost_iteration_data.append(i_list)

  return parameters,cost_iteration_data

# Make a prediction
# X: represents the inputs
# parameters: represents a model
# the result is the prediction
def predict(X, parameters):
  
  a2, cache = forward_prop(X, parameters)
  yhat = a2
  yhat = np.squeeze(yhat)

  if(yhat >= 0.5):
    y_predict = 1
  else:
    y_predict = 0

  return y_predict


# Set the seed to make result reproducible
np.random.seed(42)