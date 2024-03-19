# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:06:38 2024

@author: alper
"""

# import random

# a = 0
# b = 2
# N = 10000
# s = 0

# for i in range(N):
#     u1 = random.random()
#     x = 2 * u1
#     h = b**2
#     u2 = random.random()
#     y = h*u2
    
#     if (y-x**2) <= 0:
#         s = s+1
        
# I = h*(b-a)*s/N

 #%% 

# import random

# a = 0
# b = 2
# N = 10000
# f = 0

# for i in range(N):
#     u = random.random()
#     x = 2*u
#     f=f+x**2

# I = (b-a)*(1/N)*f


#%%

# import random
# import math

# def f1(x):
#       return (math.cos(50*x)+math.sin(20*x))**2

# def f2(x):
#       return (math.exp(math.exp(x)))

# def f3(x):
#      return (1-x**2)**((3/2))
 
# def f4(x):
#     return ((x**(-1/2))/(math.exp(x))+1)
 
# a = 0
# b = 1
# N = 10000
# f = 0

# for i in range(N):
#     x = random.random()
#     f = f+f4(x)
    
# I = (b-a)*(1/N)*f

#%%

import random
import math

def f1(x):
      return (math.cos(50*x)+math.sin(20*x))**2

def f2(x):
      return (math.exp(math.exp(x)))

def f3(x):
     return (1-x**2)**((3/2))
 
def f4(x):
    return (x**(-1/2))/(math.exp(x)+1)

def f5(x):
    return (math.exp(x+x**2))

def f6(x):
    return abs(x)+math.sin(x)
 
a = -1
b = 1
N = 10000
f = 0

for i in range(N):
    u = random.random()
    x = a+(b-a)*u
    f = f+f6(x)
    
I = (b-a)*(1/N)*f

##
