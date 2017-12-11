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

        rDay1 = randint(0, (days - 1))
        rTime1 = randint(0, (timeslots - 1))
        rRoom1 = randint(0, (rooms - 1))
        object2 = rngSchedule[rDay1][rTime1][rRoom1]

        v, e, d, s = validSchedule(rngSchedule), extraStudent(rngSchedule), doubleStudent(rngSchedule), scheduleSpread(rngSchedule)
        score1 = v + e + d + s


        swapRoomSlot(object1, object2, rngSchedule)

        v2, e2, d2, s2 = validSchedule(rngSchedule), extraStudent(rngSchedule), doubleStudent(rngSchedule), scheduleSpread(rngSchedule)
        score2 = v2 + e2 + d2 + s2

        if score2 > score1:
            print('score:', score2, i)
        else:
            swapRoomSlot(object1, object2, rngSchedule)
            i -= 1

    return rngSchedule
