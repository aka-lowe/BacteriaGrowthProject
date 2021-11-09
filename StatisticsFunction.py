import numpy as np
import matplotlib.pyplot as plt




def dataStatistics(data, statistic):
    if statistic == 'Mean Temperature':
    #takes the mean of the 0th column     
        result = data[:,0].mean()
    if statistic == 'Mean Growth rate': 
        result = data[:,1].mean()
    if statistic == 'Std Temperature':
        result = data[:,0].std()
    if statistic == 'Std Growth rate':
        result = data[:,1].std()
    if statistic == 'Rows':
        result = len(data)
    if statistic == 'Mean Cold Growth rate':
    #coldData is a new array where all temps are less than 20    
        coldData = data[data[:,0]< 20]
    #gets the mean of the growth rate of the new array where all temps are less than 20    
        result = coldData[:,1].mean()
    if statistic == 'Mean Hot Growth rate':
        hotData = data[data[:,0]>50]
        result = hotData[:,1].mean()
    return result