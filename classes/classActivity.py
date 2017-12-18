'''
This class contains attributes and methods for activities.
The __init__ has default values for all attributes that are initialized, so
we can make empty activity objects
'''
class Activity:
	def __init__(self, course = 'No Class', category = '',
				amount = 0, label = None):
		self.category = category
		self.course = course
		self.amount = int(amount)
		self.studentNumbers = {}
		self.label = label

	'''
	The __repr__ defines what we want to print when the classobject is printed.
	It will consist of the course name, its category and a number which signifies
	which version of the course it is. With lectures, lecture 1 to 3 are followed
	by everybody, but seminars and practicals numbered from 1 to 3 contain different
	 students because they are only taken once.
	'''
	def __repr__(self):
		multipleInstance = 2
		if self.course == 'No Class':
			return self.course
		elif self.amount < multipleInstance:
			return self.course.name + ' (' + self.category + ')'
		else:
			return self.course.name + ' (' + self.category + ' ' + str(self.label) + ')'

	'''
	This function enters students in the activity object. When that happens,
	students also get the activity in their list of activities.
	'''
	def enrollActivity(self, studentObject):
		self.studentNumbers[studentObject.studentNumber] = studentObject
		studentObject.activities.append(self)

	'''
	This function sets the room, timeslot and day on which an activity is given.
	It also tells the room that it is now full.
	'''
	def roomChange(self, roomObject, roomIndex, day, timeslot):
		self.room = roomObject
		self.roomIndex = roomIndex
		self.day = day
		self.timeslot = timeslot
		roomObject.full[str(day) + str(timeslot)] = True
