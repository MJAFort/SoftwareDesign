# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:03:41 2014

@author: madeleine
"""

#creating a function to check fermat
def check_fermat(a,b,c,n):
    if n > 2 :
        if ((a**n) + (b**n) == (c**n)):         #nested if statement could be traded for an and.a
            print "Holy smokes! Fermat was wrong."
        else :
            print "No, that doesn't work."
    else :
        print "That's not right."   #added another option
        
check_fermat(1,2,3,1)  #checking myself