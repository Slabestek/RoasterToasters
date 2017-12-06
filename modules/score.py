# import scheduleRange
# from classes.classRoom import Room
# from modules.init import createObjects

# score = 0

# def ValidSchedule(scheduleList):

# 	# for activity in activities:
# 	# 	if activity:
# 	# 		score += 1000


# 	# for day in days:
# 	# 	for timeslot in timeslots:
# 	# 		for classroom in classrooms:



def doubleStudent(scheduleList):

	score = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if scheduleList[day][timeslot][classroom]:
					for student in scheduleList[day][timeslot][classroom].studentNumbers:
						score += 1				
						for classroom in range(7):
							if scheduleList[day][timeslot][classroom]:
								for students in scheduleList[day][timeslot][classroom].studentNumbers:
									if student == students:
										score -= 1
							else:
								pass		
				else:
					pass					
										
	print(score)				
								

def extraStudent(scheduleList):
	score = 0
	array = []
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if scheduleList[day][timeslot][classroom]:	
					studentLength = len(scheduleList[day][timeslot][classroom].studentNumbers)
					array.append(scheduleList[day][timeslot][classroom].room)
					print(len(array))
					roomCap = int(scheduleList[day][timeslot][classroom].room.cap)	
					if studentLength > roomCap:
						score -= studentLength - roomCap
				else:
					pass		

	print(score)		


def scheduleSpread1(scheduleList):

	score = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				for activity in activities:
					score -= 10
			




# for i in courses:
# 	counter =+ 1
# 	for j in counter[i]:

	# score = 0
	# countCourse = 0
	# countAct = 0

	# for day in range (5):
		




# 		score -= 10
# 	return score

# def ScheduleSpread2(scheduleList):

# 		score -= 20
# 	return score	

# def ScheduleSpread3(scheduleList):

# 		score -= 30
# 	return score	



