class course:
	def __init__(self, name, lecture = 0, seminar = 0, seminarCap = None, practical = 0, practicalCap = None, studentNumbers = {}):
		self.name = name
		self.lecture = lecture
		self.seminar = seminar
		self.seminarCap = seminarCap
		self.practical = practical
		self.practicalCap = practicalCap
		self.studentNumbers = studentNumbers

	def enroll(self, studentNumber):
		self.studentNumbers.append(studentNumber)


heuristieken = course("heuristieken", 2, 1, 0)

for i in range(10):
	heuristieken.studentNumbers = i

print heuristieken



	
