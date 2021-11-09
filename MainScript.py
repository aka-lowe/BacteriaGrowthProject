


#Importing Libraries
import numpy as np
import os.path 

#importing functions
from DataLoadFunction import dataLoad
from StatisticsFunction import dataStatistics
from PlottingFunction import dataPlot


#hi
def print_menu(): 
    print(20*"-","Welcome to the action menu!",20*"-")
    print("1. Load Data")
    print("2. Filter Data")
    print("3. Display Statistics")
    print("4. Generate Plots")
    print("5. Quit")
    print (67*"-")

loop=True

while loop:
    print_menu()
    selection = input("Please select from above [1-5]")
    if selection==1:
        print("Load Data has been selected")
        filename=input('Please enter the name of the file you wish to use: ')
        data=dataLoad(filename)
    elif selection==2:
        print("Filter Data has been selected")
        filename=input('Please enter the name of the file you wish to use: ')
        data=dataLoad(filename)
    elif selection==3:
        print("Display Statistics has been selected")
        filename=input('Please enter the name of the file you wish to use: ')
        data=dataLoad(filename)  
    elif selection==4:
        print("General Plots has been selected")
        filename=input('Please enter the name of the file you wish to use: ')
        data=dataLoad(filename)  
    elif selection==5:
        print("Quit has been selected")
        loop=False 
    else:
        print("Please choose a number from 1-5. Press any key to try again.")
    