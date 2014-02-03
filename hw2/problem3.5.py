# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 00:17:49 2014

@author: madeleine
"""

#this is a function to print the grid
#to start off I am going to make two sets of strings that make up the lines of the grid

def make_grid():   #starting the function
        rows = "|"        
        horiz = ("+" + "----" + "+" + "----" + "+")
        side = (rows + "    " + rows + "    " + rows)
        
        print horiz
        print side
        print side
        print side
        print side
        print horiz
        print side
        print side
        print side
        print side
        print horiz


make_grid()


        
        
        
    