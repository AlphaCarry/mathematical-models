# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:21:34 2024

@author: alper
"""

import random 
import numpy as np
p = np.array([0.4, 0.3, 0.2, 0.1])
s = np.array([1, 2, 3, 4])
u = random.random()




if 0 <= u <= 0.4:
    x=1
elif 0.4 <= u <= 0.7:
    x=2
elif 0.7 <= u <= 0.9:
    x=3
elif 0.9 <= u <= 1:
    x=4
    
def indistopla(i):
 s = sum(p[0:i-1])
 return s

