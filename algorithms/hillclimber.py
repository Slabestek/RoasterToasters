from random import randint as randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import (
    extraStudent, validSchedule,
    doubleStudent, scheduleSpread
)


def climbHill(rngSchedule, activities, iterations):


    for i in range(iterations):
        rDay = randint(0, (days - 1))
        rTime = randint(0, (timeslots - 1))
        rRoom = randint(0, (rooms - 1))
        object1 = rngSchedule[rDay][rTime][rRoom]

        # print(object1)

        rDay1 = randint(0, (days - 1))
        rTime1 = randint(0, (timeslots - 1))
        rRoom1 = randint(0, (rooms - 1))
        object2 = rngSchedule[rDay1][rTime1][rRoom1]

        swapRoomSlot(object1, object2, rngSchedule)

        e, d, s = extraStudent(rngSchedule), doubleStudent(rngSchedule), scheduleSpread(rngSchedule)
        print(e, d, s)

    return rngSchedule
