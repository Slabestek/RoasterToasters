# import scheduleRange


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
						for classroom in range(7):
							if scheduleList[day][timeslot][classroom] is None:
								pass
							else:
								for students in scheduleList[day][timeslot][classroom].studentNumbers:
									if student == students:
										score -= 1	
	print(score)				
											# return score	
											
										

# def ExtraStudent(scheduleList):

	# for student in scheduleList [day][timeslot][classroom].studentNumbers:
	# 	for classroom in classrooms:
	# 		if student > seminarCap or student > practicalCap:
	# 			score -= 1
	# print(score)		

# def ScheduleSpread1(scheduleList):

# 		score -= 10
# 	return score

# def ScheduleSpread2(scheduleList):

# 		score -= 20
# 	return score	

# def ScheduleSpread3(scheduleList):

# 		score -= 30
# 	return score	



