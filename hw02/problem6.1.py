# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 11:03:48 2014

@author: madeleine
"""
def compare(x,y):   #this code is really just a glorified if statement.
    if x==y:
        return 1
    elif x > y:
        return 0
    else:
        return -1
        
print compare(1,1)
print compare(1,0)
print compare(0,1)
