


def greedyRoast(courses, scheduleList, roomObjects):

	for key, course in courses.items():
		day = 0
		timeslots = 4
		prevCategory = ''
		roomIndex = 0
		roomCount = 0
		# als het 5 activiteiten zijn
		# print(day)
		if course.numActivity == 5:
			# stop activiteiten in mon, tue, wed, thu, fri
			# loop door die activiteiten
			# print(day)
			for activity in course.activities:
				# als die activiteit meerdere keren gegeven wordt
				# print(day)
				if activity.label != None and activity.category != 'lecture':
					# stop dan die activiteiten in dezelfde dag
					fullRooms = []
					if activity.category == prevCategory and not day == 0:
						print('blijf op zelfde dag')
						day -= 1
					else:
						day % 5
					# print(day)
					while not hasattr(activity, 'room'):
						bestRoom = None
						for room in roomObjects:
							# if room in fullRooms:
							# 	print('full-1')
							# 	continue
							amountStudents = len(activity.studentNumbers)
							if amountStudents > room.cap:
								print('too small-1')
								continue
							if bestRoom == None:
								bestRoom = room
								roomIndex = roomCount % 7
							elif bestRoom.cap > room.cap:
								bestRoom = room
								roomIndex = roomCount % 7
								print('found a good one-1')
							roomCount += 1

						for timeslot in range(timeslots):
							if bestRoom:
								print('imma put ma room in yo schedhole-1')
								print(day, timeslot, roomIndex)
								if not str(day)+str(timeslot) in bestRoom.full:
									print(day, timeslot, roomIndex)
									scheduleList[day][timeslot][roomIndex] = activity
									scheduleList[day][timeslot][roomIndex].roomChange(room, roomIndex, day, timeslot)
									print('placed activity-1')
									break
								# else:
								# 	print('appending room')
								# 	fullRooms.append(room)
						if timeslot == 3:
							print('einde')
							break

						if roomCount == 0:
							print('roomcount is 0')
							break
					print(prevCategory)

					print('next day')
					day += 1


					prevCategory = activity.category
					# increase counter na gevuld te hebben/ga naar volgende dag
				# als de activiteit maar een keer gegeven wordt
				else:
					# stop dan die activiteit in de dag
					fullRooms = []
					while not hasattr(activity, 'room'):
						bestRoom = None
						for room in roomObjects:
							# if room in fullRooms:
							# 	print('full-2')
							# 	continue
							amountStudents = len(activity.studentNumbers)
							if amountStudents > room.cap:
								print('too small-2')
								continue
							if bestRoom == None:
								bestRoom = room
								roomIndex = roomCount % 7
							elif bestRoom.cap > room.cap:
								print('found a good one-2')
								bestRoom = room
								roomIndex = roomCount % 7
							roomCount += 1

						for timeslot in range(timeslots):
							if bestRoom:
								print(day, timeslot, roomIndex)
								print('imma put ma room in yo schedhole-2')
								if not str(day)+str(timeslot) in bestRoom.full:
									print(day, timeslot, roomIndex)
									scheduleList[day][timeslot][roomIndex] = activity
									scheduleList[day][timeslot][roomIndex].roomChange(room, roomIndex, day, timeslot)
									print('placed activity-2')
									break
								# else:
								# 	print('appending room')
								# 	fullRooms.append(room)
						if timeslot == 3:
							print('einde')
							break

						if roomCount == 0:
							print('roomcount is 0')
							break
					# increase counter / ga naar volgende dag
					day += 1
					day %= 5
					continue
			# zelfde activieit in zelfde dag

		# if course.numActivity == 4:
		# 	# stop activiteiten in mon, tue, thur, fri
		# 	for activity in activities:
		# 		if activity.label != None:
		# 			roomChange(roomObject, roomIndex, day, timeslot)
		# 			day = (day + 1) % 5
		# 			if day == 2:
		# 				continue
		# 		else:
		# 			roomChange(roomObject, roomIndex, day, timeslot)
		# 			day = (day + 1) % 5
		# 			if day == 2:
		# 				continue
		#
		# 	# zelfde activiteit in zelfde dag
		#
		# if course.numActivity == 3:
		# 	# stop activeiten in mon, wed, fri
		# 	for activity in activities:
		# 		if activity.label != None:
		# 			roomChange(roomObject, roomIndex, day, timeslot)
		# 			day = (day + 1) % 5
		# 			if day == 1 or day == 3:
		# 				continue
		# 		else:
		# 			roomChange(roomObject, roomIndex, day, timeslot)
		# 			day = (day + 1) % 5
		# 			if day == 1 or day == 3:
		# 				continue
		# 	# zelfde activiteit in zelfde dag
		#
		# if course.numActivity == 2:
		# 	# stop activiteiten in mon, thur OR tue, fri
		# 	# zelfde activiteit in zelfde dag
		#
		# if course.numActivity == 1:
		# 	# stop activiteiten op plekken die over zijn

	return scheduleList
