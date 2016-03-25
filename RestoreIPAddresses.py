# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:09:29 2015

@author: yzy
"""
ans = []
def insertPoint(strL,strR,curSum,sum):
    if curSum == sum:
        str = strL + strR
        ansStr = str.split('.')
        num = map(int,ansStr)
        boo = True
        if max(num) <= 256:
            for subS in ansStr:
                if subS[0]=='0' and len(subS)>1:
                    boo = False
            if boo == True:
                ans.append(str)
                
    else:
        for i in range(1,len(strR)):
            insertPoint(strL+strR[:i]+'.',strR[i:],curSum+1,sum)
            
ip = "241323010"
insertPoint('',ip,0,3)
print ans
    