#importing libraries
import numpy as np
#Funtion that loads and filters out all invalid data and returns a 3xn matrix of valid data

def dataLoad(filename):
    #Making a matrix from txt file
    mat1=np.loadtxt(filename)
    #defining an original value for t in order to count what row we are on
    t=0
    #setting data as an arbitrary array with same no of columns as matrix mat1
    data=np.array([-1,-1,-1])
    for row in mat1:
    #for loop to go through the 3 elements of each row
        t=t+1
        datarowisvalid=True
        #all below if statements set datarowisvalid=false if the values do not meet the given specifications e.g. GrowthRate is negative.
        if row[0]<=10 or row[0]>=60:
           datarowisvalid=False
           print('Error in row',t,'Temperature out of range')
        if row[1]<0:
            datarowisvalid=False
            print('Error in row',t,'Growth Rate out of range')
        if row[2]!=1 and row[2]!=2 and row[2]!=3 and row[2]!=4:
            datarowisvalid=False
            print('Error in row',t,'Bacteria out of range')
        if datarowisvalid:
#takes every row where the datarowisvalid=true and stacks it in a matrix
            #takes every row where the datarowisvalid=true and vertically stacks it in a matrix
            data=np.vstack((data,row))
    #sets data to a matrix that doesn't include the first row of arbitrary 1s
    data=data[1:,:]
    return data
print(dataLoad('testforreals.txt'))
