import csv

class Course:
	def __init__(self, name, lecture = 0, seminar = 0, seminarCap = 0, practical = 0, 
				practicalCap = 0, students = 0, studentNumbers = {}, activities = [],  seminars = 0, 
				practicals = 0):
		self.name = name
		self.lecture = lecture
		self.seminar = int(seminar)
		try:
			self.seminarCap	= int(seminarCap)
		except:
			pass	
		self.practical = int(practical)
		try:
			self.practicalCap = int(practicalCap)
		except:
			pass	
		self.studentNumbers = studentNumbers
		self.students = int(students)
		# werkt nog niet goed, bij 1 practitcal zijn er 0 practicals
		if self.seminar > 0:
			if self.students > self.seminarCap:
				remainder = self.students % self.seminarCap
				if remainder == 0:
					seminars = (self.students / self.seminarCap) * self.seminar
				else:
					seminars = (((self.students - remainder) / self.seminarCap) + 1) * self.seminar
		if self.practical > 0:			
			if self.students > self.practicalCap:
				remainder = self.students % self.practicalCap
				if remainder == 0:
					practicals = (self.students / self.practicalCap) * self.practical
				else:
					practicals = (((self.students - remainder) / self.practicalCap) + 1) * self.practical
		self.seminars = seminars
		self.practicals = practicals
					
			

	def __repr__(self):
		return self.name

	#def enroll(self, studentNumber):
	#	self.studentNumbers['studentNumber'] = ""


def courseReader(file):

	csvRows = []



