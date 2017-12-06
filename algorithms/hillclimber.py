# generate random rooster
# swap function (days, activities)
from random import randint as randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.init import createObjects as createObjects

objectList = createObjects()
roomObj = objectList[2]
print(roomObj)

def climbHill(scheduleList, activities, iterations):

    # generate a random schedule
    randomSchedule(scheduleList, days, timeslots, rooms, activities, roomObj)


    for i in range(iterations):
        object1 = None
        while object1 == None:
            rDay = randint(0, (days - 1))
            rTime = randint(0, (timeslots - 1))
            rRoom = randint(0, (rooms - 1))
            print(rDay, rTime, rRoom)
            object1 = scheduleList[rDay][rTime][rRoom]
        print(object1)
        object2 = None
        while object2 == None:
            rDay1 = randint(0, (days - 1))
            rTime1 = randint(0, (timeslots - 1))
            rRoom1 = randint(0, (rooms - 1))
            print(rDay1, rTime1, rRoom1)
            object2 = scheduleList[rDay1][rTime1][rRoom1]
        print(object2)
        print(scheduleList[object1.day][object1.timeslot])
        print(scheduleList[object2.day][object2.timeslot])
        swapRoomSlot(object1, object2, scheduleList)
        print(scheduleList[object1.day][object1.timeslot])
        print(scheduleList[object2.day][object2.timeslot])
