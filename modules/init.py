
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

# moet eigenlijk createObjects heten
def createObjects():

	courseReader()
	studentReader()
	roomReader()

	# make course objects
	courses = {}
	for course in csvCourse:
		courses[course[0]] = Course(course[0], course[1], course[2], course[3],
			course[4], course[5], course[6])

	# make students objects
	students = {}
	for student in csvStudents:
		courseList = []
		for j in range(5):
			if not student[j + 3] == '':
				courseList.append(courses[student[j + 3]])
		students[student[2]] = Student(student[0], student[1], student[2],
			courseList)

	# make room objects
	rooms = []
	for room in csvRooms:
		room[0] = Room(room[0], room[1])
		rooms.append(room[0])

	# make activity objects
	activities = []
	for course in courses:
		l = int(courses[course].lecture)
		s = int(courses[course].seminars)
		p = int(courses[course].practicals)
		if l > 0:
			for i in range(l):
				activities.append(Activity(course, 'lecture', l, i + 1))
		if s > 0:
			for i in range(s):
				activities.append(Activity(course, 'seminar', s, i + 1))
		if p > 0:
			for i in range(p):
				activities.append(Activity(course, 'practical', p, i + 1))
	actCount = 0
	count = 0
	for course in courses:
		l = int(courses[course].lecture)
		s = int(courses[course].seminars)
		p = int(courses[course].practicals)
		for i in range(l + s + p):
			courses[course].activities.append(activities[i + count])
		# print(courses[course].activities)
		# actCount += len(courses[course].activities)
		count += i + 1

	# print(actCount)

	objectList = (courses, students, rooms, activities)
	return objectList


def enrollStudent(students):

	for student in students:
		courseList = students[student].course
		# print(courseList)
		for course in courseList:
			course.enrollCourse(students[student])
		# print(len(course.studentNumbers))


def fillActivities(courses):

	for course in courses:
		seminarCount = 0
		practicalCount = 0
		students = []
		for k, v in courses[course].studentNumbers.items():
			students.append(v)
		# print(students)
		activities = courses[course].activities
		for activity in activities:
			# print(seminarCount, practicalCount)
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
			# print(activity)
			# print(activity.studentNumbers)





def courseReader():
	# read in csv of courses
	with open(coursesFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvCourse.append(row)

	# print(csvCourse[0])
	return csvCourse

def studentReader():
	# read in csv of students

	with open(studentsFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvStudents.append(row)

	# print (csvStudents)

def roomReader():
	# read in csv of rooms
	with open(roomsFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvRooms.append(row)

	# print (len(csvRooms))


# if __name__ == "__main__":
# 	main()
