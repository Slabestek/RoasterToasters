# from classRoom import TODO
from reader import courses, students, rooms
# from classStudent import TODO
# from courseCounter import TODO
import scheduleRange

# make empty list 
scheduleList = []

courseCounter = 0

# for item in course:
# 	seminar = course[item].practical
# print seminar

courseItems = courses.items()
# print courseItems

# for key, value in itertools.


for day in days:
# 	# print "dit is day {}".format(day)
	scheduleList.append([])
	for timeslot in timeslots:
		# print "dit is timeslot {}".format(timeslot)
		scheduleList[day].append([])
		for classroom in classrooms:
			# print int(course['{}'.format(courseItems[courseCounter][1])].lecture)
			# if courseCounter < course[-1]:

			# for lecture in range(int(course['{}'.format(courseItems[courseCounter][1])].lecture)):	
			if courseCounter < len(course) - 1:
				scheduleList[day][timeslot].append(courseItems[courseCounter][1])
			courseCounter += 1
			# print courseCounter

print scheduleList