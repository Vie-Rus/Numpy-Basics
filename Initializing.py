# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys
from pyparsing import delimited_list

#Initializing-------------------------------------------------------------------------------------
#0s matrix
num5 = np.zeros((3,2,5))
print("Zero Matrix: \n",num5)
print("\n")                                             #Empty space

#1s matrix
num6 = np.ones((2,3,3))
print("Ones Matrix: \n",num6)
print("\n")                                             #Empty space

#Other number matrix
num7 = np.full((2,3), 5)
print("Full Matrix: \n",num7)
print("\n")                                             #Empty space

#Full_like matrix
num2 = np.array([[1,2,3], [9,8,7,6,5,4]])
num8 = np.full_like(num2, 4)
print("Full like Matrix: \n",num8)
print("\n")                                             #Empty space

#Random decimal number matrix
num9 = np.random.rand(2,3)                              #np.random.random_sample -> will be able to take in shape
print("Random decimal Matrix: \n",num9)
print("\n")                                             #Empty space

#Random int Matrix
num10 = np.random.randint(7, size=(2,3))                #7 is highest element aka starting value, you can add low and high starting values
print("Random int Matrix: \n",num10)
print("\n")                                             #Empty space

#Identity Matrix, Square Shape
num11 = np.identity(4)
print("Identity Matrix: \n",num11)
print("\n")                                             #Empty space

#Repeat Array
num12 = np.array([[1,2,3]])
num12Repeat = np.repeat(num12, 3, axis=0)
print("This will repeat: \n",num12Repeat)
print("\n")                                             #Empty space