



def greedyRoast(courses, scheduleList, roomObject):

	for course in courses:
		dayCounter = 0
		if course.numActivity == 5:									# als het 5 activiteiten zijn
			# stop activiteiten in mon, tue, wed, thu, fri
			for activity in activities:								# loop door die activiteiten
				if activity.label != None:							# als die activiteit meerdere keren gegeven wordt
					roomChange(roomObject, roomIndex, dayCounter, timeslot)		# stop dan die activiteiten in dezelfde dag
					dayCounter = (dayCounter + 1) % 5				# increase counter na gevuld te hebben/ga naar volgende dag
				else:												# als de activiteit maar een keer gegeven wordt
					roomChange(roomObject, roomIndex, dayCounter, timeslot)		# stop dan die activiteit in de dag
					dayCounter = (dayCounter + 1) % 5				# increase counter / ga naar volgende dag
			# zelfde activieit in zelfde dag

		if course.numActivity == 4:
			# stop activiteiten in mon, tue, thur, fri
			for activity in activities:
				if activity.label != None:
					roomChange(roomObject, roomIndex, dayCounter, timeslot)
					dayCounter = (dayCounter + 1) % 5
					if dayCounter == 2:
						continue
				else:
					roomChange(roomObject, roomIndex, dayCounter, timeslot)
					dayCounter = (dayCounter + 1) % 5
					if dayCounter == 2:
						continue

			# zelfde activiteit in zelfde dag

		if course.numActivity == 3:
			# stop activeiten in mon, wed, fri
			for activity in activities:
				if activity.label != None:
					roomChange(roomObject, roomIndex, dayCounter, timeslot)
					dayCounter = (dayCounter + 1) % 5
					if dayCounter == 1 or dayCounter == 3:
						continue
				else: 
					roomChange(roomObject, roomIndex, dayCounter, timeslot)
					dayCounter = (dayCounter + 1) % 5
					if dayCounter == 1 or dayCounter == 3:
						continue
			# zelfde activiteit in zelfde dag

		if course.numActivity == 2:
			# stop activiteiten in mon, thur OR tue, fri
			# zelfde activiteit in zelfde dag

		if course.numActivity == 1:
			# stop activiteiten op plekken die over zijn

	return scheduleList