import csv

class Course:
	def __init__(self, name, lecture = 0, seminar = 0, seminarCap = 0, practical = 0, 
				practicalCap = 0, studentAmount = 0, studentNumbers = {}, activities = [],  seminars = 0, 
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
		self.studentAmount = int(studentAmount)
		
		if self.seminar > 0:
			if self.studentAmount > self.seminarCap:
				remainder = self.studentAmount % self.seminarCap
				if remainder == 0:
					seminars = (self.studentAmount / self.seminarCap) * self.seminar
				else:
					seminars = (((self.studentAmount - remainder) / self.seminarCap) + 1) * self.seminar
		if self.practical > 0:			
			if self.studentAmount > self.practicalCap:
				remainder = self.studentAmount % self.practicalCap
				if remainder == 0:
					practicals = (self.studentAmount / self.practicalCap) * self.practical
				else:
					practicals = (((self.studentAmount - remainder) / self.practicalCap) + 1) * self.practical
		self.seminars = seminars
		self.practicals = practicals

	def __repr__(self):
		return self.name

	def enrollCourse(self, classObject):
		self.studentNumbers[classObject.studentNumber] = classObject



