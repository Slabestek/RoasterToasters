import random
from copy import deepcopy as deepcopy

'''
This swap function swaps two random activities in a schedule.
'''
def swapRoomSlot(activity1, activity2, scheduleList):

    day1 = activity1.day
    day2 = activity2.day
    timeslot1 = activity1.timeslot
    timeslot2 = activity2.timeslot
    room1 = activity1.roomIndex
    room2 = activity2.roomIndex
    roomObj1 = activity1.room
    roomObj2 = activity2.room

    activity1.roomChange(roomObj2, room2, day2, timeslot2)
    activity2.roomChange(roomObj1, room1, day1, timeslot1)
    temp = scheduleList[day2][timeslot2][room2]
    scheduleList[day2][timeslot2][room2] = scheduleList[day1][timeslot1][room1]
    scheduleList[day1][timeslot1][room1] = temp

'''
The randomSchedule function can create a random schedule when called. Activities are placed at 
random in a schedule matrix. 
'''
def randomSchedule(scheduleList, days, timeslots, rooms, activities, roomObj):

    random.shuffle(activities)
    lengthActivities = len(activities)
    rngSchedule = deepcopy(scheduleList)

    counter = 0
    acounter = 0
    for day in range(days):
        for timeslot in range(timeslots):
            for room in range(rooms):
                rngSchedule[day][timeslot][room] = activities[counter]
                counter += 1
                if counter > lengthActivities:
                    return rngSchedule
                else:
                    acounter += 1
                    rngSchedule[day][timeslot][room].roomChange(
                        roomObj[room], room, day, timeslot)
    return rngSchedule

