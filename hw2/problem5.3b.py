# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:22:38 2014

@author: madeleine
"""



def check_fermat(a,b,c,n):  
    if n > 2 :                      #the nested if statement could be traded for an and statement
        if ((a**n) + (b**n) == (c**n)):
            print "Holy smokes! Fermat was wrong."
        else :
            print "No, that doesn't work."
    else :
        print "That's not right."
        
def user_input():
    a = raw_input("Enter number for 'a'.")      
    b = raw_input("Enter number for 'b'.")
    c = raw_input("Enter number for 'c'.")
    n = raw_input("Enter number for 'n'.")
    a = int(a)                              #seems like there should be a better way to do this.
    b = int(b)
    c = int(c)
    n = int(n)
    
    check_fermat(a,b,c,n)
    
user_input()

