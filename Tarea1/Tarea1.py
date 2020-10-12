import __init__
import NeuralNetwork.NeuralNetwork as nn
import numpy as np
#For ploting
import matplotlib.pyplot as plt

#For data procesing to read csv files
import pandas as pd

#Auxiliar functions

##Last prediction: plot 2 differents graphs,MSE vs EPOCH and ACCURACY vs EPOCH.
##data: list with 3 differents lists, MSE list, EPOCH list and ACCURACY list
def last_prediction_cost(data):
    plt.plot(data[2],data[0],'ro')
    plt.title("MSE vs EPOCH")
    plt.xlabel("N°EPOCH")
    plt.ylabel("MSE")
    plt.show()
    plt.plot(data[2],data[1],'ro')
    plt.title("ACCURACY vs EPOCH")
    plt.xlabel("N°EPOCH")
    plt.ylabel("ACCURACY")
    plt.show()
    return 0


##normalization: function to normalizate columns from a dataset.
##dataset: the dataset to normalizate
def normalization(dataset):
    for column in dataset.columns:##ver como sacar columna
        dh = dataset[column].max()
        dl = dataset[column].min()
        nh = 1
        nl = 0
        dataset[column] = dataset[column].apply(lambda x: (((x-dl)*(nh-nl))/(dh-dl))+nl) #funcion de normalizacion
    return dataset

##matrixConfusion: Confusion matrix to analize a neural network from a prediction and the desired results.
##Y_predicted: list of data predicted on the neural nerwork
##Y_expected:  list of data expected  from the prediction

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

#One hot encoding of categorical columns
categorical = ['WindGustDir','WindDir9am','WindDir3pm']

dataset = pd.get_dummies(dataset,columns = categorical,drop_first=True)

#Normalizate Dataset

dataset=normalization(dataset)

#Split the dataset

porcentaje = 0.8
dataTrain = dataset[:int((len(dataset))*porcentaje)]
dataTest = dataset[int((len(dataset))*porcentaje):]


#Input y Output

#Train Dataset
##Convert a dataframe(dataset) to numpy array, for be used in NeuralNetwork.

x_train = dataTrain.drop(labels = ['RainTomorrow'],axis = 1).to_numpy()
y_train = dataTrain['RainTomorrow'].to_numpy()

#Test Dataset
x_test = dataTest.drop(labels = ['RainTomorrow'],axis = 1).to_numpy()
y_test = dataTest['RainTomorrow'].to_numpy()

#Transpose de matrix to be used in the neural network order by columns
x_train=np.transpose(x_train)


# Set the hyperparameters
n_x = len(x_train)     #No. of neurons in first layer
n_h = n_x  #No. of neurons in hidden layer
n_y = 1     #No. of neurons in output layer


#The number of times the model has to learn the dataset
number_of_iterations = 10
learning_rate = 0.01

#Train model
trained_parameters , data_plot = nn.model(x_train, y_train, n_x, n_h, n_y, number_of_iterations, learning_rate)

#Plot cost and Accuracy
last_prediction_cost(data_plot)

#Testing
predicted_p=[]
c=0
print("================Testing==================")
for x in x_test:
    c+=1
    print("Running test Number:"+ str(c))
    data_predict=np.transpose(np.array([x]))
    predicted_parameters = nn.predict(data_predict, trained_parameters)
    predicted_p.append(predicted_parameters)

#Show Matrix Confusion of the test Dataset

print("===================Confusion Matrix===========================")
matrixConfusion(predicted_p,y_test)
