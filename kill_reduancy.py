__author__ = 'samanthamellin'

import numpy as np

stormID, pressure = np.loadtxt('Presure_min.txt').T

pressure=[]
ID=[]

curr_press = pressure[0]
curr_ID = stormID[0]
for i in range(len(stormID)):
    if curr_ID == stormID[i]:
        curr_ID == stormID[i+1]
    else:
        pressure.append(pressure[i])
        ID.append(stormID[i])
        curr_press=pressure[i]
        curr_ID=stormID[i]

pressure.append(pressure[i])
ID.append(stormID[i])

print pressure
print ID