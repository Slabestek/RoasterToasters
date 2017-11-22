import init
from terminaltables import AsciiTable
from scheduleRange import days, timeslots, classrooms, dayStrings

# make empty matrix 
scheduleList = [[[None] * classrooms for i in range(timeslots)] for j in range(days)]

activities = init.main()[3]

activityList = []
for activity in activities:
	activityList.extend([activity] * activity.amount)

activityAmount = len(activityList)

for day in range(days):
	for timeslot in range(timeslots):
		for classroom in range(classrooms):
			# for amount in range(activityAmount):
			if not activityList:
				break
			else:
				scheduleList[day][timeslot][classroom] = activityList.pop()

table = AsciiTable(scheduleList)
# print(table.table)
# print(tabulate(scheduleList))
# print(scheduleList)

students = init.main()[1]
# courses = init.main()[0]
# init.enrollStudents()

init.enrollStudent(students)
# print(students)

