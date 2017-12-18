import csv
from classes.classCourse import Course
from classes.classStudent import Student
from classes.classRoom import Room
from classes.classActivity import Activity

csvCourse = []
csvStudents = []
csvRooms = []


coursesFile = './data/courses.csv'
studentsFile = './data/studentenenvakken.csv'
roomsFile = './data/rooms.csv'

'''
The emptySchedule function creates an empty matrix. The activities can be added later. 
'''
def emptySchedule(days, timeslots, numRooms):

	scheduleList = [[[None] * numRooms for i in range(timeslots)] for j in range(days)]

	return scheduleList

'''
The function createObjects makes courses, students, rooms and activities objects. 
'''
def createObjects():

	courseReader()
	studentReader()
	roomReader()

	courses = {}
	for course in csvCourse:
		courses[course[0]] = Course(course[0], course[1], course[2], course[3],
			course[4], course[5], course[6])

	students = {}
	for student in csvStudents:
		courseList = []
		for j in range(5):
			if not student[j + 3] == '':
				courseList.append(courses[student[j + 3]])
		students[student[2]] = Student(student[0], student[1], student[2],
			courseList)

	rooms = []
	for room in csvRooms:
		room[0] = Room(room[0], room[1])
		rooms.append(room[0])

	activities = []
	for key, course in courses.items():
		l = int(courses[key].lecture)
		s = int(courses[key].seminars)
		p = int(courses[key].practicals)
		if l > 0:
			for i in range(l):
				activities.append(Activity(course, 'lecture', l, i + 1))
		if s > 0:
			for i in range(s):
				activities.append(Activity(course, 'seminar', s, i + 1))
		if p > 0:
			for i in range(p):
				activities.append(Activity(course, 'practical', p, i + 1))
	for _ in range(11):
		act = Activity()
		activities.append(act)
	actCount = 0
	count = 0
	for course in courses:
		l = int(courses[course].lecture)
		s = int(courses[course].seminars)
		p = int(courses[course].practicals)
		for i in range(l + s + p):
			courses[course].activities.append(activities[i + count])
		count += i + 1

	objectList = (courses, students, rooms, activities)
	return objectList


'''
The function enrollStudent adds all students registered for a course.
'''
def enrollStudent(students):

	for student in students:
		courseList = students[student].course
		for course in courseList:
			course.enrollCourse(students[student])


'''
The function fillActivities fills the activities with students.
'''
def fillActivities(courses):

	for course in courses:
		seminarCount = 0
		practicalCount = 0
		students = []
		for k, v in courses[course].studentNumbers.items():
			students.append(v)
		activities = courses[course].activities
		for activity in activities:
			if activity.category == 'lecture':
				for student in students:
					activity.enrollActivity(student)
			if activity.category == 'seminar':
				for i in range(courses[course].seminarCap):
					if i + seminarCount < len(students):
						activity.enrollActivity(students[i + seminarCount])
					else:
						break
				seminarCount += i + 1
			if activity.category == 'practical':
				for i in range(courses[course].practicalCap):
					if i + practicalCount < len(students):
						activity.enrollActivity(students[i + practicalCount])
					else:
						break
				practicalCount += i + 1


'''
The courseReader function reads in courses.csv, where information about the courses is stored.  
'''
def courseReader():

	with open(coursesFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvCourse.append(row)

	return csvCourse

'''	
The courseReader function reads in studentenenvakken.csv, where the information
about all the students is stored.
'''
def studentReader():

	with open(studentsFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvStudents.append(row)

'''
The courseReader function reads in rooms.csv, where the rooms with the capacity are stored.
'''
def roomReader():
	
	with open(roomsFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvRooms.append(row)

