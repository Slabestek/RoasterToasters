def validSchedule(rngSchedule):
	score = 0
	count = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if rngSchedule[day][timeslot][classroom]:
					count += 1
					if count == 129:
						score += 1000
	return score


def doubleStudent(rngSchedule):
	# score = 0
	# for key, student in students.items():
	# 	for key, course1 in student.courses.items():
	# 		print(course1)
	# 		# if student.course.numActivity > 1:
	# 		score += 1
	# 	print(score)	
	# 	# print(student.course)
	# print(score)	

	score = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if rngSchedule[day][timeslot][classroom]:
					for student in rngSchedule[day][timeslot][classroom].studentNumbers:
						score += 1
						for classroom1 in range(7):
							if rngSchedule[day][timeslot][classroom1]:
								for students in rngSchedule[day][timeslot][classroom1].studentNumbers:
									if student == students:
										score -= 1
	return score


def extraStudent(rngSchedule):
	score = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				studentLength = len(rngSchedule[day][timeslot][classroom].studentNumbers)
				roomCap = int(rngSchedule[day][timeslot][classroom].room.cap)
				if studentLength > roomCap:
					score -= studentLength - roomCap
	return score


def scheduleSpread(rngSchedule):
	score = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if rngSchedule[day][timeslot][classroom]:
					category1 = rngSchedule[day][timeslot][classroom].category
					for timeslot1 in range(4):
						for classroom1 in range(7):
							if rngSchedule[day][timeslot1][classroom1]:
								category2 = rngSchedule[day][timeslot1][classroom1].category
								if rngSchedule[day][timeslot][classroom].course == rngSchedule[day][timeslot1][classroom1].course:
									if rngSchedule[day][timeslot][classroom] != rngSchedule[day][timeslot1][classroom1]:
										if category1 == 'lecture' and category2 == 'lecture':
											score -= 10
										if category1 == 'lecture' and category2 == 'seminar':
											score -= 10
										if category1 == 'lecture' and category2 == 'practical':
											score -= 10
										if category1 == 'seminar' and category2 == 'practical':
											score -= 10
	return score


def bonusPoints(courses, activities):
	score = 0
	mon = 0
	tue = 1
	wed = 2
	thu = 3
	fri = 4
	for key, course in courses.items():
		if course.numActivity == 2:
			for activity in course.activities:
				for activity2 in course.activities:
					# if activity.category != activity2.category:
					if activity.day == mon and activity2.day == thu or activity2.day == mon and activity.day == thu:	
						score += 20
					if activity.day == tue and activity2.day == fri or activity2.day == tue and activity.day == fri:	
						score += 20	
		if course.numActivity == 3:
			for activity in course.activities:
				for activity2 in course.activities:
					for activity3 in course.activities:
						# if activity.category != activity2.category and activity2.category != activity3.category and activity.category != activity3.category:
						if activity.day == mon and activity2.day == wed and activity3 == fri:
							score += 20
		if course.numActivity == 4:
			print(course)
			for activity in course.activities:
				for activity2 in course.activities:
					for activity3 in course.activities:
						for activity4 in course.activities:
							if activity.day == mon and activity2.day == tue and activity3 == thu and activity4 == fri:
								score += 20			
	print(score/ 2)				


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
			

