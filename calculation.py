# Python program to test 
# internet speed 

import speedtest 
import time as t
from datetime import datetime
from matplotlib import pyplot as plt


#Initializing speedtest instance
st = speedtest.Speedtest()
#Initializing list to get average time and internet speed 
timelist = []
speedList = []
#Initializing log file
logFile = open("log.txt",'w') 
#helper function for logging
def log(text):
    print(text)
    logFile.write(text+'\n')

#Getting number of rounds from user
rounds = int(input('''For how many rounds do you want to run this test ?
Your Choice: ''')) 
    
log("[STATUS] Starting program....")


for i in range(rounds):
    start = t.time()
    log("[STATUS] Round Number " + str(i+1))
    
    #Getting Date and Time
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log("[INFO] Date and Time: " + str(dt))
    
    #Dividing by 8,000,000 to get speed in MbBs
    speed = st.download()/8000000
    speedList.append(speed)
    log("[INFO] Internet Speed: "+  str(speed) + " MBps.")
    
    #Checking if there is no internet connection
    if(speed==0):
        log("WARN NO INTERNET CONNECTION")
    
    end = t.time()
    timelist.append(end-start)
    log("[INFO] Getting internet speed Time: " + str(end-start) + " seconds.")

avgTime = sum(timelist)/len(timelist)
avgSpeed = sum(speedList)/len(speedList)


#Drawing internet speed graph
log("[STATUS] Drawing Internet speed graph...")
plt.plot(speedList)
log("[STATUS] Saving plot...")
plt.savefig('plot.png')
plt.savefig('plot.pdf')

log("[INFO] Average time to calculate internet speed: " + str(avgTime))
log("[INFO] Average  internet speed: " + str(avgSpeed))

#Exiting program
log("[STATUS] Program done executing")
log("[STATUS] Exiting program")
plt.show()