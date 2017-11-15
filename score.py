import scheduleRange

def doubleStudent(scheduleList):
	for day in days:
		for timeslot in timeslots:
			for classroom in classrooms:
				for student in scheduleList[day][timeslot][classroom].studentNumbers:			
					for classroom in classrooms:
						for students in scheduleList[day][timeslot][classroom].studentNumbers:
							if student == students :
								score -= 1
	return score



# score = 0

# if rooster = 128
# 	score = 1000
# 	for (elke activiteit (i in range 128?)):

# 		if student dubbel
# 			score -1

# 		if student te veel
# 			score -1

# 	elke activiteit vergelijken op verdeling week

# 		if verdeeld
# 			score + 20

# 		if x - 1 
# 			score - 10

# 		if x - 2
# 			score - 20

# 		if x - 3
# 			score - 30		

# return score

