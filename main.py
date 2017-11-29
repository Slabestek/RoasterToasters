
from modules.init import createObjects as createObjects
from modules.init import enrollStudent as enrollStudent
from modules.init import fillActivities as fillActivities
from terminaltables import AsciiTable
from modules.scheduleRange import days, timeslots, classrooms, dayStrings

# create the classes and put the returned object in a variable
courses, students, rooms, activities = createObjects()

# make empty matrix
scheduleList = [[[None] * classrooms for i in range(timeslots)] for j in range(days)]

# for activity in activities:
# 	print(activity)

# print(len(activities))

for day in range(days):
	for timeslot in range(timeslots):
		for classroom in range(classrooms):
			# for amount in range(activityAmount):
			if not activities:
				break
			else:
				scheduleList[day][timeslot][classroom] = activities.pop()

table = AsciiTable(scheduleList)
# print(table.table)
# print(scheduleList)

# students = objectList[1]
# courses = objectList[0]

enrollStudent(students)
fillActivities(courses)
# print(students.items()[1])
# for k, v in students.items():
# 	print(k, v)

