# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:35:57 2019

@author: DoddC
"""

a=[[1,2,3],[4,5,6]]
print(list(zip(*a)))

A = [['a', 'b'], ['c'], ['d', 'e', 'f']]
B = [inner for outer in A for inner in outer]
print(B)