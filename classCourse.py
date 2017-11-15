import csv

class Course:
	def __init__(self, name, lecture = 0, seminar = 0, seminarCap = 0, practical = 0, 
				practicalCap = 0, studentNumbers = {}, activities = [],  seminars = 0, 
				practicals = 0, students = 0):
		self.name = name
		self.lecture = lecture
		self.seminar = seminar
		self.seminarCap = seminarCap
		self.practical = practical
		self.practicalCap = practicalCap
		self.studentNumbers = studentNumbers
		self.students = students
		# werkt nog niet goed, bij 1 practitcal zijn er 0 practicals
		if int(seminar) > 0:
			if students > int(seminarCap):
				remainder = students % seminarCap
				if remainder == 0:
					seminars = (students / seminarCap) * seminar
				else:
					seminars = (((students - remainder) / seminarCap) + 1) * seminar
		if int(practical) > 0:			
			if students > int(practicalCap):
				remainder = students % practicalCap
				if remainder == 0:
					practicals = (students / practicalCap) * practical
				else:
					practicals = (((students - remainder) / practicalCap) + 1) * practical
		self.seminars = seminars
		self.practicals = practicals
					
			

	def __repr__(self):
		return self.name

	#def enroll(self, studentNumber):
	#	self.studentNumbers['studentNumber'] = ""


def courseReader(file):

	csvRows = []



