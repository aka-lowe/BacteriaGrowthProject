import numpy as np
import matplotlib.pyplot as plt


def dataPlot(data):
    #sorting data according to temperature
    srt = np.argsort(data[:,0])
    switch = srt[::-1]
    data = data[switch]
    #plotting the bar    
    salmonella=0
    bacillus=0
    listeria=0
    brocothrix=0
    for i in data:
        if i[2] ==1:
            salmonella=salmonella+1
        if i[2] ==2:
            bacillus=bacillus+1
        if i[2] ==3:
            listeria=listeria+1
        if i[2] == 4:
            brocothrix=brocothrix+1
    dataPoints = {'Salomenlla enterica':salmonella,"Bacillus cereus":bacillus, "Listeria":listeria, "Brocothrix thermosphacta":brocothrix}
    bacteriaNames = list(dataPoints.keys())
    bacteriaNumbers = list(dataPoints.values())
    plt.bar(bacteriaNames, bacteriaNumbers, color ='maroon', width = 0.4)
    plt.xlabel("Bacteria names")
    plt.ylabel("No. of bacteria")
    plt.title("Amount of bacteria in experiment")
    plt.show()   
    #plotting the scatter
    Temperature1=[]
    Growth1=[]
    Temperature2=[]
    Growth2=[]
    Temperature3=[]
    Growth3=[]
    Temperature4=[]
    Growth4=[]
    for i in data:
        if i[2]==1:
           Temperature1.append(i[0])
           Growth1.append(i[1])
        if i[2]==2:
           Temperature2.append(i[0])
           Growth2.append(i[1])
        if i[2]==3:
           Temperature3.append(i[0])
           Growth3.append(i[1])
        if i[2]==4:
           Temperature4.append(i[0])
           Growth4.append(i[1])
    plt.plot(Temperature1,Growth1, 'r-',label='Salmonella')
    plt.plot(Temperature2,Growth2,'b-',label='Bacillus')
    plt.plot(Temperature3,Growth3,'g-',label='Listeria')
    plt.plot(Temperature4,Growth4,'y-',label='Brocothrix')
    plt.xlabel('Temperature')
    plt.ylabel('Growth Rate')
    plt.xlim(10,60)
    plt.ylim(0, 1)
    plt.title('Growth rate vs Temp')
    plt.legend(loc="upper right")
    plt.show()