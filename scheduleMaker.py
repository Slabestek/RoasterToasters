# from classRoom import TODO
from classCourse import courseReader
# from classStudent import TODO
# from courseCounter import TODO

# make empty list 
scheduleList = []

days = range(5)
timeslots = range(4)
classrooms = range(7)
course = courseReader("courses.csv")
courseCounter = 0

for item in course:
	seminar = course[item].practical
print seminar

courseItems = course.items()
# print courseItems

for day in days:
# 	# print "dit is day {}".format(day)
	scheduleList.append([])
	for timeslot in timeslots:
		# print "dit is timeslot {}".format(timeslot)
		scheduleList[day].append([])
		for classroom in classrooms:
			# if courseCounter < course[-1]:
			if courseCounter < len(course) - 1:
				scheduleList[day][timeslot].append(courseItems[courseCounter][1])
			courseCounter += 1


print scheduleList