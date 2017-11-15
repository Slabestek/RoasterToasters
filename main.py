# from classRoom import TODO
from reader import csvCourse
# from classStudent import TODO
# from courseCounter import TODO
import scheduleRange

# make empty list 
scheduleList = []

course = courseReader("courses.csv")
courseCounter = 0

# for item in course:
# 	seminar = course[item].practical
# print seminar

courseItems = course.items()
# print courseItems

# for key, value in itertools.
print course['Heuristieken 1'].lecture


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