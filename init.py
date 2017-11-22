import csv
from classCourse import Course
from classStudent import Student
from classRoom import Room
from classActivity import Activity


csvCourse = []
csvStudents = []
csvRooms = []


 
coursesFile = 'courses.csv' 
studentsFile = 'studentenenvakken.csv' 
roomsFile = 'rooms.csv' 

def main():

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
	for course in courses:
		l = int(courses[course].lecture)
		s = int(courses[course].seminars)
		p = int(courses[course].practicals)
		if l > 0:
			activities.append(Activity(course, 'lecture', l))
		if s > 0:
			activities.append(Activity(course, 'seminar', s))
		if p > 0:
			activities.append(Activity(course, 'practical', p))

	objectList = [courses, students, rooms, activities]
	return objectList


def enrollStudent(students):

	for student in students:
		courseList = students[student].course
		for course in courseList:

			# course.enrollCourse(students[student])
			print(students[student])
		


	# make a dictionary with a key-value pair for each course
	#courses = {row[0]: Course(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) 
	#	for row in csvCourse}
	#return courses


def courseReader():
	# read in csv of courses
	with open(coursesFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvCourse.append(row)

	print(csvCourse[0])
	return csvCourse

def studentReader():
	# read in csv of students

	with open(studentsFile, 'r', encoding = 'ISO-8859-1') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvStudents.append(row)

			# ISO-8859-1   <- OLD ENCODING
			# cp1252    <- NEW ENCODING

	# print (csvStudents)

def roomReader():
	# read in csv of rooms
	with open(roomsFile, 'r') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvRooms.append(row) 	

	print (len(csvRooms))	

if __name__ == "__main__":
	main()
	





