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


	# 			array.append(activity)
	# 			if len(array) == 128:
	# 				score = 1000
	# 				print(len(array))
	# print(score)


def doubleStudent(scheduleList):
	score2 = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if scheduleList[day][timeslot][classroom]:
					for student in scheduleList[day][timeslot][classroom].studentNumbers:
						# print(student)
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
				if scheduleList[day][timeslot][classroom].label:
					studentLength = len(scheduleList[day][timeslot][classroom].studentNumbers)
					roomCap = int(scheduleList[day][timeslot][classroom].room.cap)
					if studentLength > roomCap:
						score3 -= studentLength - roomCap
	return score3


def scheduleSpread(scheduleList):

	score4 = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if scheduleList[day][timeslot][classroom]:
					category1 = scheduleList[day][timeslot][classroom].category
					score4 += 10
					for timeslot1 in range(4):
						for classroom1 in range(7):
							if scheduleList[day][timeslot1][classroom1]:
								category2 = scheduleList[day][timeslot1][classroom1].category
								if scheduleList[day][timeslot][classroom].course == scheduleList[day][timeslot1][classroom1].course:
									if category1 == 'lecture' and category2 == 'lecture':
										score4 -= 10
									if category1 == 'lecture' and category2 == 'seminar':
										score4 -= 10
									if category1 == 'lecture' and category2 == 'practical':
										score4 -= 10
									if category1 == 'seminar' and category2 == 'practical':
										score4 -= 10
	return score4

# def bonusPoints


	# score = 0
	# countAct = 0
	# for day in range(5):
	# 	for timeslot in range(4):
	# 		for classroom in range(7):
	# 			if scheduleList[day][timeslot][classroom]:

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
