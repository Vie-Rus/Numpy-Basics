# Numpy Basics - written by V I E R U S
# May 31, 2022
# install 'pip install numpy' with cmd
# Uses Fixed types, contiguous memeory
#----------------------------------------------------------------------
#Imports
import numpy as np
import sys

from pyparsing import delimited_list

#Basics-------------------------------------------------------------------------------------
#Basic array - 1D
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


#Initializing--------------------------------------------------------------------------------------
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
num8 = np.full_like(num2, 4)
print("Full like Matrix: \n",num8)
print("\n")                                             #Empty space


#Random decimal number matrix
num9 = np.random.rand(2,3)                              #np.random.random_sample -> will be able to take in shape
print("Random decimal Matrix: \n",num9)
print("\n")                                             #Empty space


#Random int matrix
num10 = np.random.randint(7, size=(2,3))                #7 is highest element aka starting value, you can add low and high starting values
print("Random int Matrix: \n",num10)
print("\n")                                             #Empty space


#identity matrix, square shape
num11 = np.identity(4)
print("Identity Matrix: \n",num11)
print("\n")                                             #Empty space


#Repeat array
num12 = np.array([[1,2,3]])
num12Repeat = np.repeat(num12, 3, axis=0)
print("This will repeat: \n",num12Repeat)
print("\n")                                             #Empty space


#Variables-----------------------------------------------------------------------------------------
#Copy vars
num13 = np.array([1,2,3])
num14 = num13.copy()                                    #Without copy the changes to num14 will also change num13
num14[0] = 9
print(num14)
print("\n")                                             #Empty space


#Mathematics---------------------------------------------------------------------------------------
#Adding > replace + with *, -, /
num15 = np.array([1,2,3,4])
num15 += 4                                    
print(num15)
print("\n")                                             #Empty space


#Adding arrays together
num16 = np.array([9,0,7,0])
num17 = num15 + num16
print(num17)
print("\n")                                             #Empty space


#power
num16 **2
print("This goes to the power of two: ", num16)
print("\n")                                             #Empty space


#sin> replace sin with cos
num18 = np.sin(num16)
print("This will find the sin: ", num18)
print("\n")                                             #Empty space


#combine different shapes
num19 = np.full((3,2),4)
num20 = np.ones((2,4))
numCombine = np.matmul(num19, num20)
print("This will combine different shapes and elements: ", numCombine)
print("\n")                                             #Empty space


#find Determinant
num21 = np.identity(9)
numDeter = np.linalg.det(num21)
print("This will find determinant: ", numDeter)
print("\n")                                             #Empty space


#Statistics----------------------------------------------------------------------------------------
num22 = np.array([[1,2,3], [9,8,7]])

#Find min > replace min with max to find max
numMin = np.min(num22)                                  #add axis=1 to find in min/max in differnent rows
print("This will print min: ", numMin)


#Find sum
numSum = np.sum(num22)
print("This will print out the sum: ", numSum)          #Adding axis will add values going downwards
print("\n")                                             #Empty space


#Reorganzing---------------------------------------------------------------------------------------
#reorganze
num22 = np.array([[1,2,3], [9,8,7]])
numReorg = num22.reshape((6,1))                         #((rows, columns, amount of dimensions))
print(numReorg)
print("\n")                                             #Empty space
           

#Vertically stacking
num23Pt1 = np.array([1,2,3])
num23Pt2 = np.array([9,8,7,])
num23 = np.vstack([num23Pt1, num23Pt2, num23Pt1])       #you can add as many as you want, has to have same amount of values
print("Vertical stacking: ", num23)
print("\n")                                             #Empty space


#horizontal stacking
num23Pt1 = np.array([1,2,3])
num23Pt2 = np.array([9,8,7,])
num24 = np.hstack([num23Pt1, num23Pt2])
print("Horizontal stacking: ", num24)
print("\n")                                             #Empty space


#arange
num25 = np.arange(7)                                    #prints range up to 7 intergers starting at 0
print(num25)

#update later
    #Files---------------------------------------------------------------------------------------------
    
    #Advance index/boolean masking---------------------------------------------------------------------
