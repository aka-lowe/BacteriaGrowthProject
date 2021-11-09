#Importing Libraries
import numpy as np
import os.path 

#importing functions
from DataLoadFunction import dataLoad
from StatisticsFunction import dataStatistics
from PlottingFunction import dataPlot
#Import Data
data=dataLoad(filename)

#User Interactions
#Load Data
x1 = input("Would you like to load the data: ")
if x1.lower() == "yes":
    fileName = input("What is the filename of the data file you would like to load: ")
    data=dataLoad(fileName)
elif x1.lower() == "no":
    print("It is not possible to display statistics or generate plots before any data has been loaded. Therefore, to run all of the code, you must load the data.")

#Filter Data
x2 = input("Would you like to filter the data: ")
if x2.lower() == "yes":
#filter by bacteria type
    x21 = input("Would you like to filter by bacteria type: ")
    if x21.lower() == "yes":
        print("Bacteria 1 corresponds to Salmonella enterica.")
        print("Bacteria 2 corresponds to Bacillus cereus.")
        print("Bacteria 3 corresponds to Listeria.")
        print("Bacteria 4 corresponds to Brochothrix thermosphacta.")
        bacteria = input("What numerical value of bacteria would you like to filter the data to: ")
        data1 = []
        for x in data:
            if x[2] == bacteria:
                data1.append(x)
        data = data1
        print(data)
 
#filter by growth rate           
    x22 = input("Would you like to filter by growth rate: ")
    if x22.lower() == "yes":
        minimum = input("What would you like the minimum value of the growth rates to be: ")
        maximum = input("What would you like the maximum value of the growth rates to be: ")
        data1 = []
        for x in data:
            if x[1] >= minimum and x[1] <= maximum:
                data1.append(x)
        data = data1
        print(data)
                
#Display Statistics
x3 = input("Would you like to display statistics: ")
if x3.lower() == "yes":
    statistic = input("Which statistic would you like to display: ")
    if statistic == "Mean Temperature":
        print("This statistic corresponds to finding the mean or average temperature of the data, which is the sum of all the values divided by the number of values. In doing so, we calculate a measurement that best represents the entire set of temperature data pooints, as an average.")
    elif statistic == "Mean Growth Rate":
        print("This statistic corresponds to finding the mean or average growth rate of the data, which is the sum of all the values divided by the number of values. In doing so, we calculate a measurement that best represents the entire set of growth rate data pooints, as an average.")
    if statistic == "Std Temperature":
        print()
    elif statistic == "Std Growth Rate":
        print()
    if statistic == "Rows":
        print()
    elif statistic == "Mean Cold Growth rate":
        print()
    elif statistic == "Mean Hot Growth rate":
        print()
    print(dataStatistics(data, statistic))
    
#Generate Plots  
x4 = input("Would you like to generate plots: ")
if x4.lower() == "yes":    
       
data=0
#function to display menu of options
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
    selection = int(input("Please select a number (1-5) from above:"))
    if selection==1:
        print("Load Data has been selected")
        filename=input('Please enter the name of the file you wish to use: ')
        data=dataLoad(filename)
        print('Data Loaded successfully!')
    elif selection==2:
        print("Filter Data has been selected")
        if data==0:
            print('Error please load data first!')
        else:
            filename=input('Please enter the name of the file you wish to use: ')
            data=dataLoad(filename)  
    elif selection==3:
        print("Display Statistics has been selected")
        if data==0:
           print('Error please load data first!')
        else:
            filename=input('Please enter the name of the file you wish to use: ')
            data=dataLoad(filename)  
    elif selection==4:
        print("General Plots has been selected")
        if data==0:
           print('Error please load data first!')
        else:
            filename=input('Please enter the name of the file you wish to use: ')
            data=dataLoad(filename)  
    elif selection==5:
        print("Quit has been selected")
        loop=False 
    else:
        print("Please choose a number from 1-5. Press any key to try again.")
