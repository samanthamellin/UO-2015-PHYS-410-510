__author__ = 'samanthamellin'
import numpy as np
# I assumed that every numebr we see las .25h for since we are recording
# data with such time interval thus we

storm_id, latitude, longitude, year = np.loadtxt('lat_and_long.txt').T  # Transposed for easier unpacking
# curr_id corresponds to current id we comparing the others to when going through the loop
curr_id = storm_id[0]
# sets the latitude
curr_lat = 0
# set the longitude
curr_long = 0
#
finalid = []
finalyear = []

for i in range(len(storm_id)):
    if (curr_id == storm_id[i]):
        if ((latitude[i] <= 30.0) and (latitude[i] >= 25.0)):
            curr_long = abs(longitude[i])
            if ((curr_long <= 80.0) and (curr_long >= 75.0)):
                finalid.append(storm_id[i])
                finalyear.append(year[i])
        else:
            curr_id = storm_id[i + 1]
    else:
        curr_id = storm_id[i + 1]

#print "these are the years where we move though 'finalyear'", finalyear
#print " "
#print "these are the spin up IDs 'finalid' ", finalid
#print " "
years = []
# tells it to old the number of ourrhances at the end
numHurr = []
curr_year = year[0]  #stbrbetibl
curr_id = finalid[0]
tracker = 1  #we will use this function (TO BE DEFINED) to count the number of happens
for i in range(len(finalyear)):  #look though the data
    if (curr_year == finalyear[i]):
        if (curr_id != finalid[i]):
            # != not  equal to
            tracker = tracker + 1  #for each new ID we will add a count to our tracker num Hurr
            curr_id = finalid[i]
    else:
        years.append(finalyear[i - 1])
        numHurr.append(tracker)  #append numHurr with the tracker number
        tracker = 1
        curr_year = finalyear[i]
        curr_id = finalid[i]

years.append(finalyear[len(finalyear) - 1])
numHurr.append(tracker)

print years
print numHurr

np.savetxt('years.txt', years)
np.savetxt('occurances.txt', numHurr)
