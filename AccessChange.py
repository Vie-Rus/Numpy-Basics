# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys
from pyparsing import delimited_list

#Access/Change-------------------------------------------------------------------------
#Specific element row,column
num3 = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print("This will get the second row, fourth number: ", num3[1,4])
print("\n")                                             #Empty space

#Specific Row
print("Prints everything in the first row: ", num3[0, :]) #Reverse for column
print("\n")                                             #Empty space

#Get [Startindex:endindex:stepsize]
print("Skips number: \n",num3[0,1:7:2])                 #or you can do num3[0, 1:-1:2]
print("\n")                                             #Empty space

#Changes numbers
num3[0,3] = 96
print("This will change the first row, fourth number to 96: \n", num3[0,:])
print("\n")                                             #Empty space

num3[:,3] = 100
print("This will change both rows fourth number to 100: \n",num3)
print("\n")                                             #Empty space

#3D array
num4 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(num4)
print("\n")                                             #Empty space

#Get specific element in 3D
print("This should print 4: \n", num4[0,1,1])
print("\n")                                             #Empty space

#Replace an element
num4[:,1,:] = [[6,9], [1,3]]
print("This will change the second rows elements:\n ", num4 )
print("\n")                                             #Empty space