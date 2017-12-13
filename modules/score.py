def validSchedule(scheduleList):
	score1 = 0
	count = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if scheduleList[day][timeslot][classroom]:
					count += 1
					if count == 129:
						score1 += 1000
	return score1


def doubleStudent(scheduleList):
	score2 = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if scheduleList[day][timeslot][classroom]:
					for student in scheduleList[day][timeslot][classroom].studentNumbers:
						score2 += 1
						for classroom1 in range(7):
							if scheduleList[day][timeslot][classroom1]:
								for students in scheduleList[day][timeslot][classroom1].studentNumbers:
									if student == students:
										score2 -= 1
	return score2


def extraStudent(scheduleList):
	score3 = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				studentLength = len(scheduleList[day][timeslot][classroom].studentNumbers)
				roomCap = int(scheduleList[day][timeslot][classroom].room.cap)
				if studentLength > roomCap:
					score3 -= studentLength - roomCap
	return score3


def scheduleSpread(rngSchedule):
	score4 = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				print(rngSchedule[day][timeslot][classroom])
				if rngSchedule[day][timeslot][classroom]:
					category1 = rngSchedule[day][timeslot][classroom].category
					for timeslot1 in range(4):
						for classroom1 in range(7):
							if rngSchedule[day][timeslot1][classroom1]:
								category2 = rngSchedule[day][timeslot1][classroom1].category
								if rngSchedule[day][timeslot][classroom].course == rngSchedule[day][timeslot1][classroom1].course:
									if rngSchedule[day][timeslot][classroom] != rngSchedule[day][timeslot1][classroom1]:
										if category1 == 'lecture' and category2 == 'lecture':
											score4 -= 10
										if category1 == 'lecture' and category2 == 'seminar':
											score4 -= 10
										if category1 == 'lecture' and category2 == 'practical':
											score4 -= 10
										if category1 == 'seminar' and category2 == 'practical':
											score4 -= 10
	print(score4)

def bonusPoints(courses, activities):
	score = 0
	mon = 0
	tue = 1
	wed = 2
	thu = 3
	fri = 4
	# for day in range(5):
	# 	for timeslot in range(4):
	# 		for classroom in range(7):
	# 			activity = rngSchedule[day][timeslot][classroom]
	# 			if rngSchedule[day][timeslot][classroom].amount != 0:
	# 				if activity.numActivity == 2:
	count = 0
	for key, course in courses.items():
		# print(course)
		if course.numActivity == 2:
			for activity in course.activities:
				if activity.day == 0 or activity.day == 3:
					score += 20
				if activity.day == 1 or activity.day == 4:
					score += 20
		if course.numActivity == 3:
			for activity in course.activities:
				if activity.day == 0 or activity.day == 2 or activity.day == 4:
					score += 20
		if course.numActivity == 4:
			for activity in course.activities:
				if activity.day == 0 or activity.day == 1 or activity.day == 3 or activity.day == 4:
					score += 20					
		


	print(score)				


		# 	count += 1
		# 	# print(count)
		# print(activity)	
		# print(count)
	# print(count)

	# 		print(activity)
	# 		print(activity.day)
	# 		if activity.day == 1:
	# 			score +=1
	# print(score)			



			# print(activities.day) 


			# if course.activities != 'No Class':
			# 	print(course.activities.day)
				



	# 		score += 1

	# print(score)



			# for day in range(5):
			# 	for timeslot in range(4):
			# 		for classroom in range(7):
			# 			if rngSchedule[0][timeslot][classroom] and rngSchedule[3][timeslot][classroom]:
			# 				score += 20
			# 			elif rngSchedule[1][timeslot][classroom] and rngSchedule[4][timeslot][classroom]:	
			# 				score +=20
		








	# 					if rngSchedule[mon][timeslot][classroom]:
	# 						print(rngSchedule[mon][timeslot][classroom])
	# 						print(rngSchedule[mon][timeslot][classroom].numActivity)

	# print(score)		


						

						# if rngSchedule[mon][timeslot][classroom] and rngSchedule[thu][timeslot][classroom]:
							# score += 1
					


					# if rngSchedule[day][timeslot][classroom].numActivity == 3:

					# if rngSchedule[day][timeslot][classroom].numActivity == 4:	


					
	# print(score)						






	# 				countAct = 0
	# 				print(scheduleList[day][timeslot][classroom])
	# 				print(scheduleList[day][timeslot][classroom].amount)
					# for courses in scheduleList[day][timeslot][classroom].course:
					# 	category = scheduleList[day][timeslot][classroom].category
					# 	if category == 'lecture':
					# 		countAct += 1
					# 	if category == 'seminar':
					# 		countAct += 1
					# 	if category == 'practical':
					# 		countAct += 1
					# 	print(scheduleList[day][timeslot][classroom].course)
					# 	print(countAct)

					# 	if countDay == countAct - 1
					# 		score -= 10
						# for day in range(5):
					# 	activityCheck = scheduleList[day][timeslot][classroom]
					# 	if activityCheck:
					# 		if activity == activityCheck:
								# countAct += 1
							# if countAct



					# score -= 10
