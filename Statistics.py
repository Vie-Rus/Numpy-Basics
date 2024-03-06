# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys
from pyparsing import delimited_list

#Statistics----------------------------------------------------------------------------------------
num22 = np.array([[1,2,3], [9,8,7]])

#Find min > replace min with max to find max
numMin = np.min(num22)                                  #add axis=1 to find in min/max in differnent rows
print("This will print min: ", numMin)

#Find sum
numSum = np.sum(num22)
print("This will print out the sum: ", numSum)          #Adding axis will add values going downwards
print("\n")                                             #Empty space