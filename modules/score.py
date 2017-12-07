def validSchedule(scheduleList):
	score = 0
	array = []
	countAct = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				activity = scheduleList[day][timeslot][classroom]
				array.append(activity)
				if len(array) == 129:
					score = 1000	
	print(score)
	print(countAct)				


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
	print(score)				
								

def extraStudent(scheduleList):
	score = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if scheduleList[day][timeslot][classroom]:	
					studentLength = len(scheduleList[day][timeslot][classroom].studentNumbers)
					roomCap = int(scheduleList[day][timeslot][classroom].room.cap)	
					if studentLength > roomCap:
						score -= studentLength - roomCap	
	print(score)		


def scheduleSpread1(scheduleList):

	score = 0
	countAct = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				activity = scheduleList[day][timeslot][classroom]
				if activity:
					for day in range(5):
						activityCheck = scheduleList[day][timeslot][classroom]
						if activityCheck:
							if activity == activityCheck:
								countAct += 1
								# if countAct 



					# score -= 10
					
		


# def ScheduleSpread2(scheduleList):

# 		score -= 20
# 	return score	

# def ScheduleSpread3(scheduleList):

# 		score -= 30
# 	return score	



