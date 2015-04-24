__author__ = 'samanthamellin'
curr_decade = 1900
numb_storm = 0
years_decade = []
ns_decade = []
for i in range(len(years)):
    if( (years[i] >= curr_decade) and (years[i] <= curr_decade + 10)):
        numb_storm = numb_storm + numHurr[i]
    else:
        years_decade.append(curr_decade)
        ns_decade.append(numb_storm)
        curr_decade = curr_decade + 10
        numb_storm = 0
print ns_decade
print years_decade


decade = []
total_deca_hurr = []
hurr_sum = 0
counter = 0
curr_deca_floor = 1900
for i in range(len(years)):
    if ((years[i] <= curr_deca_floor + 10) and (years[i] >= curr_deca_floor)):
        hurr_sum = hurr_sum + numHurr[i]
    counter = counter + 1
else :
    decade.append(curr_deca_floor + 10)
total_deca_hurr.append(hurr_sum)
curr_deca_floor = curr_deca_floor + 10
counter = 0

print decade
print total_deca_hurr

#np.savetxt('decade_year.txt', decade)
#np.savetxt('decade_.txt', decade)





av_deca_time = []
decade = []
time_sum = 0
cocunter = 0
curr_deca_floor = 1900
for i in range(len(level_year)):
    if((level_year[i]<= curr_deca_floor + 10) and (level_year[i] >= curr_deca_floor)):
	time_sum = time_sum + level_time[i]
        counter = counter + 1
    else:
	decade.append(curr_deca_floor+10)
	av_deca_time.append(time_sum/ counter)
	curr_deca_floor = curr_deca_floor + 10
  	counter = 0


print av_deca_time
print decade

#np.savetxt('decade_year.txt', decade)
#np.savetxt('decade_.txt', decade)

