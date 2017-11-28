
from modules.init import createClasses as createClasses
from modules.init import enrollStudent as enrollStudent
from terminaltables import AsciiTable
from modules.scheduleRange import days, timeslots, classrooms, dayStrings

# create the classes and put the returned object in a variable
objectList = createClasses()

# make empty matrix 
scheduleList = [[[None] * classrooms for i in range(timeslots)] for j in range(days)]

activities = objectList[3]

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
# print(scheduleList)

students = objectList[1]
courses = objectList[0]

enrollStudent(students)
print(len(courses['Kansrekenen 2'].studentNumbers))

