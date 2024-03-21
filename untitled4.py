# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:01:49 2024

@author: alper
"""
import random
import numpy as np

p = 0.3
n = 2
t = 1000
x = []

for i in range (t):
    y = []
    for i in range(n):
        u = random.random()
        if u <= 1-p:
            y.append(0)
        else:
            y.append(1)
    x.append(sum(y))

mu = np.mean(x)
V = np.var(x)