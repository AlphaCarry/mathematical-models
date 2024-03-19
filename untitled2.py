# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:26:40 2024

@author: alper
"""


# x = 0
# x1 = 23 
# x2 = 66

# for i in range(14):
#   x = (x +(3*x1+5*x2))/100


x = [23,66]
sayilar = [x[0]/100, x[1]/100]

for n in range(2,14):
    x.append((3*x[n-1]+5*x[n-2])%100)
    sayilar.append(x[n]/100)