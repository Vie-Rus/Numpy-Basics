# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys
from pyparsing import delimited_list

#Variables-----------------------------------------------------------------------------------------
#Copy vars
num13 = np.array([1,2,3])
num14 = num13.copy()                                    #Without copy the changes to num14 will also change num13
num14[0] = 9
print(num14)
print("\n")                                             #Empty space