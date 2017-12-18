import collections

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


def doubleStudent(students):
	score = 0
	# collisions = 0
	for key, student in students.items():
		activities = student.activities
		dayTime = []
		for activity in activities:
		# 	print(student, activity)
			numActivity = len(activities)
			if numActivity > 1:
				dayTime.append(str(activity.day) + str(activity.timeslot))
		counter = collections.Counter(dayTime)
		for count in counter.values():
			if count > 1:
				# print(count)
				score -= count



		# print(student.course)
	# print('coll', collisions)
	return score

def doubleStudent2(rngSchedule):

	score = 0
	for day in range(5):
		for timeslot in range(4):
			for classroom in range(7):
				if rngSchedule[day][timeslot][classroom].label:
					for student in rngSchedule[day][timeslot][classroom].studentNumbers:
						for classroom1 in range(7):
							if classroom == classroom1:
								continue
							if rngSchedule[day][timeslot][classroom1].label:
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
					if activity.category != activity2.category:
						if activity != activity2:
							if activity.day == mon and activity2.day == thu:
								score += 20
							elif activity2.day == mon and activity.day == thu:
								score += 20
							if activity.day == tue and activity2.day == fri:
								score += 20
							elif activity2.day == tue and activity.day == fri:
								score += 20
		if course.numActivity == 3:
			for activity in course.activities:
				for activity2 in course.activities:
					for activity3 in course.activities:
						if activity.category != activity2.category and activity2.category != activity3.category and activity.category != activity3.category:
							if activity != activity2 and activity2 != activity3 and activity != activity3:
								if activity.day == mon and activity2.day == wed and activity3 == fri:
									score += 20
		if course.numActivity == 4:
			for activity in course.activities:
				for activity2 in course.activities:
					for activity3 in course.activities:
						for activity4 in course.activities:
							if activity.category != activity2.category and activity2.category != activity3.category and activity.category != activity3.category:
								if activity.category != activity.category and activity2.category != activity4.category and activity3.category != activity4.category:
									if activity != activity2 and activity2 != activity3 and activity != activity3:
										if activity != activity and activity2 != activity4 and activity3 != activity4:
											if activity.day == mon and activity2.day == tue and activity3 == thu and activity4 == fri:
												score += 20
	return score / 2

def score(rngSchedule, courses, activities, students):
    score = 0
    score += bonusPoints(courses, activities)
    score += scheduleSpread(rngSchedule)
    score += extraStudent(rngSchedule)
    score += doubleStudent(students)
    score += validSchedule(rngSchedule)

    return score
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
