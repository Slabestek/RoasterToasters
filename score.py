import scheduleRange

score = 0

def ValidSchedule(scheduleList):

	# for activity in activities:
	# 	if activity:
	# 		score += 1000


	# for day in days:
	# 	for timeslot in timeslots:
	# 		for classroom in classrooms:



def doubleStudent(scheduleList):
	#for day in days:
		#for timeslot in timeslots:
			#for classroom in classrooms:
				for student in scheduleList[day][timeslot][classroom].studentNumbers:			
					for classroom in classrooms:
						for students in scheduleList[day][timeslot][classroom].studentNumbers:
							if student == students :
								score -= 1
	return score

def ExtraStudent(scheduleList):

	for student in scheduleList [day][timeslot][classroom].studentNumbers:
		for classroom in classrooms:
			if student > seminarCap or student > practicalCap:
				score -= 1
	return score		

def ScheduleSpread1(scheduleList):

		score -= 10
	return score

def ScheduleSpread2(scheduleList):

		score -= 20
	return score	

def ScheduleSpread3(scheduleList):

		score -= 30
	return score	



