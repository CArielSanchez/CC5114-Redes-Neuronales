


#Create a Gym to train a Perceptron or similars
##data_training: data for the training of the perceptron.
class Gym:

    def __init__(self,data_training):
        self.data=data_training
    #Train a perceptron
    ##P: recive the perceptron to train.
    def training_(self,P):
        if(len(self.data)==0):
            return 0
        ## d0: inputs
        ## d1: desired output
        ## P.run(): real output
        for d in self.data:
            P.learn(P.run(d[0]),d[1],d[0])
    
    #Make a evaluation about the presition of a perceptron with a particular data.
    ##P:perceptron
    ##data_test: data test
    def general_exam(self,P,data_test):
        data=[]  
        count=0
        
        for d in data_test:
            d_=[d[0],d[1],P.run(d[0])]    
            if(d_[2] == d[1]):
                count+=1
            data.append(d_)
            
        
        return [(count/len(data)),data]
    #Make a evaluation of the perceptron with the average of the presition.
    ##P:perceptron
    ##datas_test: more than 1 data test
    def average_exam(self,P,datas_test):
        avg=0
        for data_test in datas_test:
            exam= self.general_exam(P,data_test)
            avg+=exam[0]
        return avg/len(datas_test)
