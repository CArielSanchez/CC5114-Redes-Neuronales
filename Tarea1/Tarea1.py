import __init__
import NeuralNetwork.NeuralNetwork as nn
import numpy as np

#For ploting
import matplotlib.pyplot as plt

#For data procesing to read csv files
import pandas as pd

#Auxiliar functions
def normalization(dataset):
    for column in dataset.columns:##ver como sacar columna
        dh = dataset[column].max()
        dl = dataset[column].min()
        nh = 1
        nl = 0
        dataset[column] = dataset[column].apply(lambda x: (((x-dl)*(nh-nl))/(dh-dl))+nl) #funcionde normalizacion
    return dataset

def matrixConfusion(Y_predicted,Y_expected):
     
    #Predicted Raining and Raining corrects (equals)
    raining00 = 0
    #Predicted Raining positive and Not Raining
    raining01 = 0
    #Predicted raining negative and Raining
    raining10 = 0
    #Predicted raining negative and Not Raining (equals)
    raining11 = 0

    for x in range(len(Y_predicted)):
        if Y_predicted[x] == Y_expected[x]:
            if Y_predicted[x] == 1:
                raining00+=1
            else:
                raining11+=1
        else:
            if Y_predicted[x] == 1:
                raining01+=1
            else:
                raining10+=1


    df = pd.DataFrame({'.':['Predicted Raining', 'Predicted Not Raining','Total Expected'], 
    'Raining':[raining00,raining01,(raining00+raining01)],
    'Not Raining':[raining10,raining11,(raining10+raining11)], 
    'Total Predicted':[(raining00+raining10),(raining01+raining11),' ']}, 
    columns = ['.','Raining', 'Not Raining','Total Predicted'])

    print(df)
    return df

#Load dataset

dataset = pd.read_csv('Tarea1/weatherAUS.csv')


#Need to processing the data
#First we eliminate the columns with an amount of NA and predict if rain today
dataset.drop(labels = ['Date','Location','Evaporation','Sunshine','Cloud3pm','Cloud9am','RISK_MM'],axis = 1,inplace = True)
dataset['RainToday'].replace({'No':0,'Yes':1},inplace = True)
dataset['RainTomorrow'].replace({'No':0,'Yes':1},inplace = True)


dataset.dropna(inplace = True)


categorical = ['WindGustDir','WindDir9am','WindDir3pm']

dataset = pd.get_dummies(dataset,columns = categorical,drop_first=True)

dataset=normalization(dataset)

#Dividimos el dataset

porcentaje = 0.8
dataTrain = dataset[:int((len(dataset))*0.8)]
dataTest = dataset[int((len(dataset))*0.8):]


#Input y Output

x_train = dataTrain.drop(labels = ['RainTomorrow'],axis = 1).to_numpy()
y_train = dataTrain['RainTomorrow'].to_numpy()


print(x_train)

x_test = dataTest.drop(labels = ['RainTomorrow'],axis = 1).to_numpy()
y_test = dataTest['RainTomorrow'].to_numpy()

# Set the hyperparameters
n_x = len(x_train[0])     #No. of neurons in first layer
n_h = 2*n_x    #No. of neurons in hidden layer
n_y = 1     #No. of neurons in output layer

print(n_x)
#The number of times the model has to learn the dataset
number_of_iterations = 100
learning_rate = 0.01

trained_parameters = nn.model(np.transpose(x_train), y_train, n_x, n_h, n_y, number_of_iterations, learning_rate)


probando = np.transpose(x_test[0])

y_predict = nn.predict(probando, trained_parameters)

print('Neural Network prediction for example ({:d}, {:d}) is {:d}'.format(
    x_test[0], y_test[0], y_predict))

matrixConfusion([1,0,0],[0,0,1])
