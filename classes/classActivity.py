class Activity:
	def __init__(self, course, category, amount, label = None):
		self.category = category
		self.course = course
		self.amount = int(amount)
		self.studentNumbers = {}
		self.label = label

	def __repr__(self):
		if self.amount < 2:
			return self.course + ' (' + self.category + ')'
		else:
			return self.course + ' (' + self.category + ' ' + str(self.label) + ')'

	def enrollActivity(self, studentObject):
		self.studentNumbers[studentObject.studentNumber] = studentObject

	def roomChange(self, roomObject, dayIndex, timeslot):
		self.room = roomObject
		self.day = dayIndex
		self.timeslot = timeslot
