__author__ = 'samanthamellin'
import numpy as np
# I assumed that every numebr we see las .25h for since we are recording
# data with such time interval thus we

storm_id, storm_pressure, years, time = np.loadtxt('time_spinup.txt').T #Transposed for easier unpacking
# curr_id corresponds to current id we comparing the others to when going through the loop
curr_id = storm_id[0]
# used calcuation duration of spin up
curr_spin_duration = 0.00
# tem variable to track number of spin up for each storm
#num_spinup_for1strom = 0
temp_time = []
# This has the average time spent by storm in spin up
spin_time_array = []
spin_year = []
spin_id = []
for i in range(len(storm_id)):
    if(curr_id == storm_id[i]):
        if((storm_pressure[i] <= 1000) and (storm_pressure[i] >= 970)):
            curr_spin_duration = curr_spin_duration + .25
                #print "zeros"
                #print curr_spin_duration
        else:
            if((storm_pressure[i-1] <= 1000) and (storm_pressure[i-1] >= 970)):
        #num_spinup_for1storm = num_spinup_for1storm + 1
                temp_time.append(curr_spin_duration)
        #print curr_spin_duration
                #print temp_time
                curr_spin_duration = 0
    else:
        curr_id = storm_id[i]
        if(len(temp_time) == 0):
            print "storm id =", storm_id[i-1], "has no spin up"
        else:
            spin_time_array.append( sum(temp_time) / len(temp_time) )
            spin_year.append(years[i-1])
            spin_id.append(storm_id[i-1])
            temp_time = []


print "these are the year where we have spin up",spin_year
print " "
print "these are the spin up IDs",spin_id
print " "
print "these are the times coresponding to each spin up",spin_time_array
print " "

np.savetxt('spinyears.txt', spin_year)
np.savetxt('spinIDs.txt', spin_id)
np.savetxt('spinTime.txt', spin_time_array)
# we'll use these to calculate time of spin up to campare.
total_time_1950_1970 = 0
total_time_1990_2010 = 0
for i in range(len(spin_year)):
    if( (spin_year[i]<= 1970) and (spin_year[i] >= 1950)):
        total_time_1950_1970 = total_time_1950_1970 + spin_time_array[i]
    if( (spin_year[i]<= 2010) and (spin_year[i] >= 1990)):
        total_time_1990_2010 = total_time_1990_2010 + spin_time_array[i]
print "total spin time 1950 to 1970 = ", total_time_1950_1970
print " "
print "total spin time 1990 to 2010 = ", total_time_1990_2010
print " "