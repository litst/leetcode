# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:51:11 2015

@author: yzy
"""
def com(numbers):
    #print numbers
    if len(numbers) == 1:
        ans.append(numbers[0])
    else:
        operLoc = []
        for i in xrange(len(numbers)):
            if numbers[i] in opers:
                operLoc.append(i)
        res = 0
        for i in operLoc:
            if numbers[i] == "+":
                res = numbers[i-1]+numbers[i+1]
            elif  numbers[i] == "-":
                res = numbers[i-1]-numbers[i+1]
            elif  numbers[i] == "*":
                res = numbers[i-1]*numbers[i+1]
            else:
                res = numbers[i-1]/numbers[i+1]
            print res
            if i != len(numbers)-2:
                com(numbers[:i-1]+[res]+numbers[i+2:])
            else:
                com(numbers[:i-1]+[res])
ans = []
opers = ["+","-","*","/"]
input = "15+7-6*24"
numbers = []
if len(input) == 1:
    print [int(input[0])]
else:
    start = 0
    for i in xrange(1,len(input)):
        if input[i] in opers:
            numbers.append(int(input[start:i]))
            numbers.append(input[i])
            start = i+1
    numbers.append(int(input[start:]))
com(numbers)
print ans