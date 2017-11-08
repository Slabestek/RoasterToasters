import csv

class course:
	def __init__(self, name, lecture = 0, seminar = 0, seminarCap = None, practical = 0, 
				practicalCap = None, studentNumbers = {}, activities = 0, students = 0):
		self.name = name
		self.lecture = lecture
		self.seminar = seminar
		self.seminarCap = seminarCap
		self.practical = practical
		self.practicalCap = practicalCap
		self.studentNumbers = studentNumbers
		self.students = len(studentNumbers)
		if students > seminarCap and seminar > 0:
			remainder = students % seminarCap
			if remainder == 0:
				self.seminars = (students / seminarCap) * seminar
			else:
				self.seminars = (((students - remainder) / seminarCap) + 1) * seminar
		if students > practicalCap and practical > 0:
			remainder = students % practicalCap
			if remainder == 0:
				self.practicals = (students / practicalCap) * practical
			else:
				self.practicals = (((students - remainder) / practicalCap) + 1) * practical
			

	def __repr__(self):
		return self.name

	def enroll(self, studentNumber):
		self.studentNumbers.append(studentNumber)


heuristieken = course("heuristieken")


def courseReader(file):

	csvRows = []

	# read in csv of courses
	with open(file, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvRows.append(row)

	# make a dictionary with a key-value pair for each course
	courses = {row[0]: course(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) 
		for row in csvRows}
	return courses

courses = courseReader('courses.csv')



	
