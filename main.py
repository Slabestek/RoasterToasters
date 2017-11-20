# from classRoom import TODO
import init
# from classStudent import TODO
# from courseCounter import TODO
from scheduleRange import days, timeslots, classrooms

# make empty list 
scheduleList = []

# edit loop zodat 1 de liststructuur bouwt en een andere loop die list vult
for day in days:
	scheduleList.append([])
	for timeslot in timeslots:
		scheduleList[day].append([])

print (scheduleList)
# vul scheduleList met activities
print(init.main()[3])
