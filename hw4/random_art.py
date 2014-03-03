# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import random
import math

def build_random_function(min_depth, max_depth):
    """Here is the function that will dictate the form of the created art.
       It will use recursion and have at least one prod, sin_pi, cos_pi, 
       and an (x,y).
    """
    xylist = [["X"],["Y"]]
    if max_depth <= 1:
        return xylist[random.randint(0,1)]
    
    f = build_random_function(min_depth-1,max_depth-1)
    g = build_random_function(min_depth-1,max_depth-1)
    prod = ["prod",f,g]
    cos_pi = ["cos_pi",f]
    sin_pi = ["sin_pi",f]
    cube = ["^3",f]
    half = ["*.5",f]
    square = ["^2",f]
    funclist = [prod,cos_pi,cube,half,square,sin_pi,["X"],["Y"]]
    if min_depth > 1:
        return funclist[random.randint(0,5)]
    elif min_depth <= 1:
        return funclist[random.randint(0,7)]
print build_random_function(2,10)     
   
def evaluate_random_function(f, x, y):
    """ LATIDA"""
    func = f[0]
    if func == "X":
        return x
    if func == "Y":
        return y
    if func == "prod":
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if func == "cos_pi":
        return math.cos(math.pi*evaluate_random_function(f[1],x,y))
    if func == "sin_pi":
        return math.sin(math.pi*evaluate_random_function(f[1],x,y))
    if func == "^3":
        return evaluate_random_function(f[1],x,y)**3
    if func == "^2":
        return evaluate_random_function(f[1],x,y)**2
    if func == "*.5":
        return evaluate_random_function(f[1],x,y)*.5
    else:
        print func


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        We map an imput location to an output location...
    """
    input_interval_start = float(input_interval_start)
    input_interval_end = float(input_interval_end)
    output_interval_start = float(output_interval_start)
    output_interval_end = float(output_interval_end)
    delta1 = input_interval_end - input_interval_start
    delta2 = output_interval_end - output_interval_start
    return (val-input_interval_start)*delta2/delta1
    
def makeinart(sizex,sizey,min_depth,max_depth,number):
    sizex = int(sizex)
    sizey = int(sizey)
    red_func = build_random_function(min_depth,max_depth)
    blue_func = build_random_function(min_depth,max_depth)
    green_func = build_random_function(min_depth,max_depth)
    im = Image.new("RGB",(sizex,sizey))
    for i in range(sizex):
        x = remap_interval(i,0.0,float(sizey),-1.0,1.0)
        for j in range(sizey):
            y = remap_interval(j,0.0,float(sizey),-1.0,1.0)
            red = evaluate_random_function(red_func,x,y)
            blue = evaluate_random_function(blue_func,x,y)
            green = evaluate_random_function(green_func,x,y)
            rmap = remap_interval(red,-1.0,1.0,0,255)
            bmap = remap_interval(blue,-1.0,1,0,255)
            gmap = remap_interval(green,-1.0,1.0,0,255)
            im.putpixel((i,j),(int(rmap),int(gmap),int(bmap)))
    im.save("image" + str(number) + ".bmp")
makeinart(2000,500,0,25,22)