import csv

class Student:
	def __init__(self, lastName, firstName, studentNumber, course = [],
				activities = {}):
		self.lastName = lastName
		self.firstName = firstName
		self.studentNumber = studentNumber
		self.course = course
		self. activities = activities

	def __repr__(self):
		name = self.firstName + ' ' + self.lastName
		return name

	def assignActivity(self, activity, course):
		if not course in self.activities:
			self.activities[course] = []
			self.activities[course].append(activity)
		else:
			self.activities[course].append(activity)


'''
myList = []

with open('studentenenvakken.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		myList.append(row)

print myList[1][0]
Yanick = student(myList[1][0],myList[1][1],myList[1][2])
print Yanick.course
'''
