# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys
from pyparsing import delimited_list

#Basic Array-------------------------------------------------------------------------------------
#Array - 1D
num1 = np.array([1,2,3])
print("should be 1,2,3: ", num1)
print("\n")                                             #Empty space

#Array - 2D
num2 = np.array([[1,2,3], [9,8,7,6,5,4]])
print("This should be 1,2,3\t9,8,7: ", num2)
print("\n")                                             #Empty space

#Get Dimension
print("How many dimensions does num1 have: ", num1.ndim)
print("\n")                                             #Empty space

#Get shape
print("Whats the shape of num2: ", num2.shape)
print("\n")                                             #Empty space

#get Type
print("Type: ", num1.dtype)                             #in num1 you can add /,dtype = 16/ to make the output be int16 
print("\n")                                             #Empty space

#Get size
print("Int Size: ", num1.itemsize)                      #Will output 4 since the int type is 32 by default
print("\n")                                             #Empty space
print("Amount of elements: ", num1.size)
print("\n")                                             #Empty space

#Total size
print("Total size: ",num1.nbytes)                       #size *itemsize
print("\n")                                             #Empty space