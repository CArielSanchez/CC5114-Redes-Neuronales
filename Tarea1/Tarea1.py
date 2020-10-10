import __init__
import NeuralNetwork.NeuralNetwork as nn
import numpy as np
#For ploting
import matplotlib.pyplot as plt

#For data procesing to read csv files
import pandas as pd

#Auxiliar functions
def last_prediction_cost(data):
    plt.plot(data[1],data[0],'ro')
    plt.show()
    return 0


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
    'Raining':[raining00,raining10,(raining00+raining10)],
    'Not Raining':[raining01,raining11,(raining01+raining11)], 
    'Total Predicted':[(raining00+raining01),(raining10+raining11),' ']}, 
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
dataTrain = dataset[:int((len(dataset))*porcentaje)]
dataTest = dataset[int((len(dataset))*porcentaje):]


#Input y Output

x_train = dataTrain.drop(labels = ['RainTomorrow'],axis = 1).to_numpy()
y_train = dataTrain['RainTomorrow'].to_numpy()




x_test = dataTest.drop(labels = ['RainTomorrow'],axis = 1).to_numpy()
y_test = dataTest['RainTomorrow'].to_numpy()

x_train=np.transpose(x_train)


# Set the hyperparameters
n_x = len(x_train)     #No. of neurons in first layer
n_h = n_x  #No. of neurons in hidden layer
n_y = 1     #No. of neurons in output layer



#The number of times the model has to learn the dataset
number_of_iterations = 1000
learning_rate = 0.1

trained_parameters , data_plot = nn.model(x_train, y_train, n_x, n_h, n_y, number_of_iterations, learning_rate)
#last_prediction_cost(data_plot)
predicted_p=[]
c=0
for x in x_test:
    c+=1
    print(c)
    data_predict=np.transpose(np.array([x]))
    predicted_parameters = nn.predict(data_predict, trained_parameters)
    predicted_p.append(predicted_parameters)


matrixConfusion(predicted_p,y_test)
