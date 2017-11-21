class Activity:
	def __init__(self, course, category, amount, studentNumbers = {}):
		self.category = category
		self.course = course
		self.amount = int(amount)

	def __repr__(self):
		return self.course + ' (' + self.category + ')'

	def enrollActivity(classObject):
		self.studentNumbers[classObject.studentNumber] = classObject