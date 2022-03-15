# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:02:43 2022

@author: JOE
"""
#import numpy model

import numpy as np

#Defined some functions for activation

def indexof(tar,li):
    index = 0
    for item in li:
        if item == tar:
            return index
        index += 1
    return None

def relu(x):
    if x>0:
        return x
    else:
        return 0
    
def tanh(x):
    return np.exp(x)-np.exp(-x)/np.exp(x)-np.exp(-x)

def sigmoid(x):
    return 1/(np.exp(x)+1)

def softmax(x,li):
    index = indexof(x,li) 
    lisoft = np.exp(li)/sum(np.exp(li))
    return lisoft[index]

def switch(name):
    dic = {"relu":relu,"tanh":tanh,"sigmoid":sigmoid,"softmax":softmax}
    return dic[name]

class layer:
    def __init__(self,InputShape,OutputShape,ActivationFunction):
        if ActivationFunction == None:
            self.ActivationFunction = relu
            self.act = "relu"
        else:
            self.act = ActivationFunction
            self.ActivationFunction = switch(ActivationFunction)
        self.InputShape  = InputShape
        self.NumberOfNenural = OutputShape
        self.array = []
        ''' initialize metrix '''
        for i in range (0,self.NumberOfNenural):
            x = [np.random.randn()]
            for j in range(0,self.InputShape):
                x.append(np.random.randn())
            self.array.append(np.array(x))
    def compute(self,inputarr):
        #compute this layer output
        newarr = [1]
        for item in inputarr:
            newarr.append(item)
        self.outlist = []
        for i in range(0,self.NumberOfNenural):
            x = 0
            for j in range(0,self.InputShape+1):
                x += newarr[j]*self.array[i][j]
            self.outlist.append(self.ActivationFunction(x))
        return self.outlist
    
    def show(self):
        print("activation function:")
        print("\'"+self.act+"\'")
        print("weight metrix is")
        for row in self.array:
            for item in row:
                print(round(item,4),end = " ")
            print()
        print("\n---------------------------\n")
        
class   NeuralNetwork:
    def __init__(self,NumberOfInput,NumberOfOutput,NeuralList,OutputFuction):
        #initialize metrix neural number and Activation function
        self.sequence  = []
        cnt = 0
        for item in NeuralList:
            if cnt == 0:
                Input = NumberOfInput
            output = item
            self.sequence.append(layer(Input, output , "relu"))
            Input = item
            cnt += 1
        if OutputFuction == None:
            if NumberOfOutput == 1:
                ActivationFunction = "sigmoid"
            else:
                ActivationFunction = "softmax"
        else:
            ActivationFunction = OutputFuction
        self.sequence.append(layer(Input, NumberOfOutput ,ActivationFunction ))
    
    def predict(self,xlist,res):
        #predict the result of inputdata and return correct or not
        out = self.compute(xlist)
        index = 0
        for item in out:
            if item == res[index]:
                continue
            else:
                return False
            index += 1
        return True
    
    def testaccuracy(self,inputdata,label):
        #caculate accuracy of inputdatas
        corr = 0
        error = 0
        for index in range(len(inputdata)):    
            var = self.predict(inputdata[index], label[index])
            if var:
                corr += 1
            else :
                error += 1
            index += 1
        self.accuracy = corr/(corr+error)
    
    def compute(self,xlist):
        #compute inputdata to get the output
        out = []
        inputarr = xlist
        for item in self.sequence:
            out = item.compute(inputarr)
            inputarr = out
        return out
    
    def show(self):
        #showing informations of the neural network
        for i in range(len(self.sequence)):        
            print(str(i+1)+" th layer")
            self.sequence[i].show()
            
    def train(self,rate):
        #trainning neural network 
        pass

#test class 
testnet = NeuralNetwork(4, 2, [5,2,3,2], "sigmoid")
testnet.show()
'''
print(testnet.compute([1,2,6,3]))
print(testnet.predict([1,2,6,3], [0.586681,0.5205,0.0092704]))
'''
inputdata = [[1,2,3,4],
             [2,1,4,4],
             [3,3,1,2],
             [4,4,1,3],
             [2,1,3,4],
             [6,1,4,2],
             [1,2,3,6]]
label = [[0.2,0.3],
         [1.1,2.2],
         [3.2,0.055],
         [0.44,0.02],
         [0.033,0.0001],
         [0.123,0.00456],
         [0.1,0.2]]
testnet.testaccuracy(inputdata, label)
print(testnet.accuracy)
