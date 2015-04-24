__author__ = 'samanthamellin'
import numpy as np
# I assumed that every numebr we see las .25h for since we are recording
# data with such time interval thus we

storm_id, years, time, category = np.loadtxt('cat3andabove.txt').T #Transposed for easier unpacking
# curr_id corresponf to curent id we comparing the others to when going through the loop
curr_id = storm_id[0]
# used calcuation duration at a level
curr_level_duration = 0.00
# tem variable to track number of spin up for each storm
#num_spinup_for1strom = 0
temp_time = []
# This has the average time spent by stom in spin up
level_time = []
level_year = []
level_id = []
level_cat = []
for i in range(len(storm_id)):
    # checks if the category is at least 3
    if(category[i] >= 3):
    	if(curr_id == storm_id[i]):
	    curr_level_duration = curr_level_duration + .25

	else:
            curr_id = storm_id[i]
	    level_time.append(curr_level_duration)
	    level_year.append(years[i-1])
	    level_id.append(storm_id[i-1])
            curr_level_duration = 0

print "these are the year where we have ",level_year
print " "
print "these are the spin up IDs",level_id
print " "
print "these are the times coresponding to each spin up",level_time
print " "

np.savetxt('spinyears_cat3.txt', level_year)
np.savetxt('spinIDs_cat3.txt', level_id)
np.savetxt('spinTime_cat3.txt', level_time)
# we'll use these to calculate time of spin up to campare.


