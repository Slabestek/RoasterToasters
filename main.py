# from classRoom import TODO
import init
# from classStudent import TODO
# from courseCounter import TODO
from scheduleRange import days, timeslots, classrooms, dayStrings

# make empty list 
scheduleList = []

# edit loop zodat 1 de liststructuur bouwt en een andere loop die list vult
for day in days:
	# scheduleList.append(dayStrings[day])
	scheduleList.append([])
	for timeslot in timeslots:
		scheduleList[day].append([])

activities = init.main()[3]

activityList = []
for activity in activities:
	activityList.extend([activity] * activity.amount)

activityAmount = len(activityList)

for day in days:
	for timeslot in timeslots:
		for classroom in classrooms:
			# for amount in range(activityAmount):
			if not activityList:
				break
			else:
				scheduleList[day][timeslot].append(activityList.pop())


print (scheduleList)
# vul scheduleList met activities
# print(init.main()[3])
