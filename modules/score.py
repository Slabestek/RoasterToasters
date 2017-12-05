# import scheduleRange
from classes.classRoom import Room

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
	for day in range (5):
		for timeslot in range (4):
			for classroom in range (7):
				if scheduleList[day][timeslot][classroom] is None:
					pass
				else:
					for student in scheduleList[day][timeslot][classroom].studentNumbers:
						score += 1		
						for classroom in range(7):
							if scheduleList[day][timeslot][classroom] is None:
								pass
							else:
								for students in scheduleList[day][timeslot][classroom].studentNumbers:
									if student == students:
										score -= 1	
	print(score)				
											# return score	
											
										

def extraStudent(scheduleList):
	score = 0
	for day in range (5):
		for timeslot in range (4):
			for classroom in range (7):
				if scheduleList[day][timeslot][classroom] is None:
					pass
				else:	
					if len(scheduleList[day][timeslot][classroom].studentNumbers) > int(scheduleList[0][0][0].room.cap):
						score -= 1
	print(score)		

# # def ScheduleSpread1(scheduleList):

# 	score = 0
# 	countCourse = 0
# 	countAct = 0

# 	for day in range (5):
# 		for course in courses:
# 			for activities in activity:




# 		score -= 10
# 	return score

# def ScheduleSpread2(scheduleList):

# 		score -= 20
# 	return score	

# def ScheduleSpread3(scheduleList):

# 		score -= 30
# 	return score	



