# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys
from pyparsing import delimited_list

#Mathematics--------------------------------------------------------------------------------------
#Adding > Replace + with *, -, /
num15 = np.array([1,2,3,4])
num15 += 4                                    
print(num15)
print("\n")                                             #Empty space

#Adding Arrays Together
num16 = np.array([9,0,7,0])
num17 = num15 + num16
print(num17)
print("\n")                                             #Empty space

#Power
num16 **2
print("This goes to the power of two: ", num16)
print("\n")                                             #Empty space

#sin> Replace sin with cos
num18 = np.sin(num16)
print("This will find the sin: ", num18)
print("\n")                                             #Empty space

#Combine Different Shapes
num19 = np.full((3,2),4)
num20 = np.ones((2,4))
numCombine = np.matmul(num19, num20)
print("This will combine different shapes and elements: ", numCombine)
print("\n")                                             #Empty space

#Find Determinant
num21 = np.identity(9)
numDeter = np.linalg.det(num21)
print("This will find determinant: ", numDeter)
print("\n")                                             #Empty space