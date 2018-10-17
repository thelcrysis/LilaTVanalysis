import matplotlib.pyplot as plt
import string

def GrabDataFromFiles(src): #grab data from text files formatted as 'time-viewers'
    Watchers = [] #only number of Watchers recorded, timestamps are not required as check is done every 2 secs
    with open(src) as f:
        for line in f:
            print int(line[20:])
            Watchers.append(line[20:])
    return Watchers



#plotter
y = GrabDataFromFiles("fo.txt")
timeline = []
for i in range(len(y)):
    timeline.append(i*2) #creating timestamps
plt.plot(timeline, y)
plt.show()
