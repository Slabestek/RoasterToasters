import csv

'''
This class contains information on students. Their activities are saved in a
list, which is filled by enrollActivity in classActivity.py.
'''
class Student:
	def __init__(self, lastName, firstName, studentNumber, course = []):
		self.lastName = lastName
		self.firstName = firstName
		self.studentNumber = studentNumber
		self.course = course
		self.activities = []

	def __repr__(self):
		name = self.firstName + ' ' + self.lastName
		return name
