class Activity:
	def __init__(self, studentNumbers = {}, category, course):
		self.category = category
		self.course = course

	def __repr__(self):
		return self.course + self.category

	def enrollActivity(classObject):
		self.studentNumbers[classObject.studentNumber] = classObject