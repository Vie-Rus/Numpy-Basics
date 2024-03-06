# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys
from pyparsing import delimited_list

#Reorganzing---------------------------------------------------------------------------------------
num22 = np.array([[1,2,3], [9,8,7]])
numReorg = num22.reshape((6,1))                         #((rows, columns, amount of dimensions))
print(numReorg)
print("\n")                                             #Empty space
           
#Vertically Stacking
num23Pt1 = np.array([1,2,3])
num23Pt2 = np.array([9,8,7,])
num23 = np.vstack([num23Pt1, num23Pt2, num23Pt1])       #you can add as many as you want, has to have same amount of values
print("Vertical stacking: ", num23)
print("\n")                                             #Empty space

#Horizontal Stacking
num23Pt1 = np.array([1,2,3])
num23Pt2 = np.array([9,8,7,])
num24 = np.hstack([num23Pt1, num23Pt2])
print("Horizontal stacking: ", num24)
print("\n")                                             #Empty space

#Arange
num25 = np.arange(7)                                    #prints range up to 7 intergers starting at 0
print(num25)
