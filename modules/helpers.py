from random import shuffle as shuffle

def swapRoomSlot(activity1, activity2, scheduleList):

    day1 = activity1.day
    day2 = activity2.day
    timeslot1 = activity1.timeslot
    timeslot2 = activity2.timeslot
    room1 = activity1.roomIndex
    room2 = activity2.roomIndex

    activity1.roomChange(activity2, room2, day2, timeslot2)
    activity2.roomChange(activity1, room1, day1, timeslot1)
    temp = scheduleList[day2][timeslot2][room2]
    scheduleList[day2][timeslot2][room2] = scheduleList[day1][timeslot1][room1]
    scheduleList[day1][timeslot1][room1] = temp

def randomSchedule(scheduleList, days, timeslots, rooms, activities):
    counter = 0
    shuffle(activities)
    for day in range(days):
    	for timeslot in range(timeslots):
    		for room in range(rooms):
    			scheduleList[day][timeslot][room] = activities[counter]
    			counter += 1
    			if scheduleList[day][timeslot][room] == None:
    				break
    			else:
    				scheduleList[day][timeslot][room].roomChange(
    					rooms[room], room, day, timeslot)
