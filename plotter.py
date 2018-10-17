import matplotlib.pyplot as plt
import string
import math
from math import *

def GrabDataFromFiles(src): #grab data from text files formatted as 'time-viewers'
    Watchers = [] #only number of Watchers recorded, timestamps are not required as check is done every 2 secs
    with open(src) as f:
        for line in f:
            Watchers.append(line[20:])   #extracting no of watchers from save file
    return Watchers


#plotter
def Plotter():
    y = []

    #stackoverflow as best way to remove everything but digiits from strings
    all=string.maketrans('','')                        #
    nodigs=all.translate(all, string.digits)            #
    for iter in GrabDataFromFiles("record.txt"):        #
         y.append(int(iter.translate(all, nodigs)))     #
    ###

    timeline = []
    for i in range(len(y)):
        timeline.append(i*2) #creating timestamps

    #calculating some more stats
    average = sum(y)/len(y)
    maximum = int(max(y))
    minimum = int(min(y))

    plt.plot(timeline, y)

    print 'average ' + str(round(average))
    print 'max ' + str(maximum)
    print 'min ' + str(minimum)
    #plotting those stats
    plt.plot((-1, max(timeline)), (average, average), 'r', alpha=0.5, label='max')
    plt.plot((-1, max(timeline)), (maximum, maximum), 'g', alpha=0.3)
    plt.plot((-1, max(timeline)), (minimum, minimum), 'g', alpha=0.3)



    plt.show()
