import csv

class student:
	def __init__(self, lastName, firstName, studentNumber, course = []):
		self.lastName = lastName
		self.firstName = firstName
		self.studentNumber = studentNumber
		self.course = course

	def __repr__(self):
		name = self.firstName + ' ' + self.lastName
		return name
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
