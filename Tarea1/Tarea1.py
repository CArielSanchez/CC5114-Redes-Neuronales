import __init__
import NeuralNetwork.NeuralNetwork

#For ploting
import matplotlib.pyplot as plt

#For data procesing to read csv files
import pandas as pd

def normalization(dataset):
    for column in dataset.columns:##ver como sacar columna
        dh = dataset[column].max()
        dl = dataset[column].min()
        nh = 1
        nl = 0
        dataset[column] = dataset[column].apply(lambda x: (((x-dl)*(nh-nl))/(dh-dl))+nl) #funcionde normalizacion
    return dataset



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

print(dataset.head())

for column in dataset.columns:##ver como sacar columna
        print(column)
        print(dataset[column].max())
        print(dataset[column].min())
        print('/n')




