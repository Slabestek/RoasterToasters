import csv

csvCourse = []
csvStudents = []
csvRooms = []
 
coursesFile = 'courses.csv' 
studentsFile = 'studentenenvakken.csv' 
roomsFile = 'rooms.csv'  

# read in csv of courses
with open(coursesFile, 'r') as f:
	next(f)
	reader = csv.reader(f)
	for row in reader:
		csvCourse.append(row)

print (len(csvCourse))

# read in csv of courses
with open(studentsFile, 'r', encoding = 'ISO-8859-1') as f:
	next(f)
	reader = csv.reader(f)
	for row in reader:
		csvStudents.append(row)

print (len(csvStudents))		

with open(roomsFile, 'r') as f:
	next(f)
	reader = csv.reader(f)
	for row in reader:
		csvRooms.append(row) 	

print (len(csvRooms))		

