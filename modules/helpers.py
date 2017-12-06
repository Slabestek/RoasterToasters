import random

def swapRoomSlot(activity1, activity2, scheduleList):

    day1 = activity1.day
    day2 = activity2.day
    timeslot1 = activity1.timeslot
    timeslot2 = activity2.timeslot
    room1 = activity1.roomIndex
    room2 = activity2.roomIndex

    activity1.roomChange(activity2.room, room2, day2, timeslot2)
    activity2.roomChange(activity1.room, room1, day1, timeslot1)
    temp = scheduleList[day2][timeslot2][room2]
    scheduleList[day2][timeslot2][room2] = scheduleList[day1][timeslot1][room1]
    scheduleList[day1][timeslot1][room1] = temp

def randomSchedule(scheduleList, days, timeslots, rooms, activities, roomObj):
    counter = 0

    # random.shuffle(activities)
    l = len(activities)
    length = 0
    nonecount=0
    for day in range(days):
        for timeslot in range(timeslots):
            for room in range(rooms):
                scheduleList[day][timeslot][room] = activities[counter]
                counter += 1
                if counter >= l:
                    break
                if scheduleList[day][timeslot][room] == None:
                    # print(scheduleList[day][timeslot][room])
                    nonecount+=1
                    # break
                else:
                    # print(scheduleList[day][timeslot][room])
                    scheduleList[day][timeslot][room].roomChange(
                        roomObj[room], room, day, timeslot)
            length += len(scheduleList[day][timeslot])

    # print(nonecount, counter)
    # print(l, length)
