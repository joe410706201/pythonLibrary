import numpy as np

def isprime(x):
    Max = int(pow(x,0.5))+1
    for i in range(2,Max+1):
        if x%i == 0:
            return False
    return True

def pickprime(size):
    i = size+1
    while(not isprime(i)):
        i += 1
    return i

def picker(xBound,BiasBound):
    x = np.random.randint(1,xBound)
    b = np.random.randint(0,BiasBound)
    return x,b

def function(poly,x):
    return poly.compute(x)

class poly:
    def __init__(self,coefs):
        self.fun = coefs

    def compute(self,x):
        return x*self.fun[0]+self.fun[1]
           

class hashtable:
    def __init__(self,size,poly):
        ''' initialize '''
        self.fun = function
        self.prime = pickprime(size*3+1)
        self.poly = poly
        self.size = size
        self.dic ={}
        self.keylist = []

    def hash(self,value):
        ''' hash function for get key '''
        key = (self.fun(self.poly,value)%self.prime)%self.size
        return key
    
    def insert(self,value):
        ''' insert value to hashtable '''
        key = self.hash(value)
        if self.haskey(key):
            self.dic[key].append(value)
        else:
            self.dic[key] = []
            self.dic[key].append(value)
            self.keylist.append(key)
            self.keylist.sort()

    def delete(self,value):
        ''' delete value from hashtable '''
        key = self.hash(value)
        if self.haskey(key) == False:
            raise KeyError("key not found Error")
        else:
            for item in self.dic[key]:
                if item == value:
                    self.dic[key].remove(value)
                    if len(self.dic[key]) == 0:
                        self.keylist.remove(key)
                        self.keylist.sort()
                    return
            raise ValueError("no such value")

    def haskey(self,key):
        ''' key is in hashtable or not'''
        for item in self.keylist:
            if item == key:
                return True
        return False

    def find(self,value):
        ''' find the value in hashtable '''
        key = self.hash(value)
        if self.haskey(key) == False:
            raise KeyError("key not found Error")
        else:
            for item in self.dic[key]:
                if item == value:
                    return "value "+str(value)+" has been found in dictionary with index "+str(key)
            raise ValueError("no such value")

    def showfunction(self):
        ''' show function in hashtable '''
        print("function is")
        print("f(x) = "+str(self.poly.fun[0])+"x + "+str(self.poly.fun[1]) )
        

    def show(self):
        ''' showing infomations about hashtable '''
        self.showfunction()
        print("max size:",self.size)
        print("curr size:",len(self.keylist))
        print("prime:",self.prime)
        for item in self.keylist:
            cnt = 0
            print(item,end = ":")
            for values in self.dic[item]:
                if cnt == 0:
                    print(values,end = "")
                    cnt = 1
                else:
                    print("->",values,end = "")
            print()

