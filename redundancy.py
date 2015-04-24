__author__ = 'samanthamellin'
import numpy as np

stormID, data = np.loadtxt('Presure_min.txt').T
# unpack correctly in python 1st row, 2ndrow = my file
#tell it to hold years
pressure = []
#tells it to old the number of ourrhances at the end
numHurr = []
curr_press = data[0]  #stbrbetibl
curr_id = stormID[0]
tracker = 1  #we will use this function (TO BE DEFINED) to count the number of happens
for i in range(len(data)):  #look though the data
    if (curr_press == data[i]):
        if (curr_id != stormID[i]):
            # != not  equal to
            tracker = tracker + 1  #for each new ID we will add a count to our tracker num Hurr
            curr_id = stormID[i]
    else:
        pressure.append(data[i - 1])
        numHurr.append(tracker)  #append numHurr with the tracker number
        tracker = 1
        curr_press = data[i]
        curr_id = stormID[i]

pressure.append(data[len(data) - 1])
numHurr.append(tracker)

print pressure
print numHurr

np.savetxt('pressure.txt', pressure)
np.savetxt('occ_press.txt', numHurr)