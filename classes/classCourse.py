import csv

'''
This class contains all information on a course. Capacities of seminars and
practicals are calculated, as well as the actual amount of activities the course
has, when taking in account the capacities. Most defaults are 0 because
sometimes there are no activities of a kind, and we want to know if there are 0
instead of none.
'''
class Course:
	def __init__(self, name, lecture = 0, seminar = 0, seminarCap = 0, practical = 0,
				practicalCap = 0, studentAmount = 0, seminars = 0, practicals = 0):
		self.name = name
		self.lecture = int(lecture)
		self.seminar = int(seminar)
		self.practical = int(practical)
		self.numActivity = self.lecture + self.seminar + self.practical
		try:
			self.seminarCap	= int(seminarCap)
		except:
			pass
		self.practical = int(practical)
		try:
			self.practicalCap = int(practicalCap)
		except:
			pass
		self.studentNumbers = {}
		self.activities = []
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

	'''
	This function enters students in a dictionary.
	'''
	def enrollCourse(self, classObject):
		self.studentNumbers[classObject.studentNumber] = classObject

	# def addActivities
