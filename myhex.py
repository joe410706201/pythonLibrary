# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:42:38 2022

@author: JOE
"""
def getInt(hexbit):
    dic = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,
           "C":12,"D":13,"E":14,"F":15}
    try:
        dic[hexbit]
    except:
        print("key not found")
        return -1
    return dic[hexbit]

def getChar(inputNumber):
    res = hex(inputNumber)
    return res[2].upper()

def DecToHex(inputNumber):#decimal number to hexadecimal string
    i = 0
    while (pow(16,i)<= inputNumber):
        i += 1
    num = i-1;
    arr = ""
    expo = num
    for i in range(num+1):
        coef = inputNumber // pow(16,expo)
        inputNumber -= coef*pow(16,expo)
        arr += (getChar(coef))
        expo -= 1
    return arr

def HexToDec(inputNumber):#hexadecimal string to decimal number
    res = 0
    index = 0
    maxpow = len(inputNumber)-1
    while (maxpow >= 0):
        if getInt(inputNumber[index]) == -1:
            raise ValueError("Not a hex bit")
        res += getInt(inputNumber[index])*pow(16,maxpow)
        maxpow -= 1
        index += 1
    return res

def mutihexs(hexs): #mutiply hexadecimal strings to another hexadecimal string  
    for item in hexs:
        if type(item) != str:
            raise ValueError("invaild value")
    num = 1
    for item in hexs:
        num *= HexToDec(item.upper().replace("0X",""))
    res = DecToHex(num)
    return res
