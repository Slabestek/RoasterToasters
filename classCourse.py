import csv

class course:
	def __init__(self, name, lecture = 0, seminar = 0, seminarCap = None, practical = 0, 
				practicalCap = None, studentNumbers = {}):
		self.name = name
		self.lecture = lecture
		self.seminar = seminar
		self.seminarCap = seminarCap
		self.practical = practical
		self.practicalCap = practicalCap
		self.studentNumbers = studentNumbers

	def __repr__(self):
		return self.name

	def enroll(self, studentNumber):
		self.studentNumbers.append(studentNumber)


heuristieken = course("heuristieken")


def courseReader(file):

	myList = []

	# read in csv of courses
	with open(file, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			myList.append(row)

	# make a dictionary with a key-value pair for each course
	courseDict = {row[0]: course(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) 
		for row in myList}

	return courseDict





	
