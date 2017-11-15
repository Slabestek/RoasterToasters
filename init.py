import csv
from classCourse import Course


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
	Course1 = Course(csvCourse[0][0], csvCourse[0][1], csvCourse[0][2], csvCourse[0][3], 
	csvCourse[0][4], csvCourse[0][5], csvCourse[0][6])
	print(Course1.practicals)
	print(Course1.students)

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

	print (csvCourse)

def studentReader():
	# read in csv of students
	with open(studentsFile, 'r', encoding = 'ISO-8859-1') as f:
		next(f)
		reader = csv.reader(f)
		for row in reader:
			csvStudents.append(row)

	print (len(csvStudents))

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





