from random import randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import (
    extraStudent, validSchedule,
    doubleStudent, scheduleSpread, bonusPoints
)
import csv


def climbHill(rngSchedule, activities, i):

    with open('hillClimb' + str(i) + 'iter.csv', 'w', newline = '') as csvfile:
        scoreWriter = csv.writer(csvfile)

        randObj = 2
        for _ in range(i):

            randList = []
            for j in range(randObj):
                rDay = randint(0, (days - 1))
                rTime = randint(0, (timeslots - 1))
                rRoom = randint(0, (rooms - 1))
                randList.append(rngSchedule[rDay][rTime][rRoom])
            # print(randList)

            # rDay = randint(0, (days - 1))
            # rTime = randint(0, (timeslots - 1))
            # rRoom = randint(0, (rooms - 1))
            # object1 = rngSchedule[rDay][rTime][rRoom]
            #
            # rDay1 = randint(0, (days - 1))
            # rTime1 = randint(0, (timeslots - 1))
            # rRoom1 = randint(0, (rooms - 1))
            # object2 = rngSchedule[rDay1][rTime1][rRoom1]

            v, e, d, s, b = validSchedule(rngSchedule), extraStudent(rngSchedule), doubleStudent(rngSchedule), scheduleSpread(rngSchedule), bonusPoints(courses, activities)
            score1 = v + e + d + s + b

            swapRoomSlot(randList[0], randList[1], rngSchedule)

            v2, e2, d2, s2, b2 = validSchedule(rngSchedule), extraStudent(rngSchedule), doubleStudent(rngSchedule), scheduleSpread(rngSchedule), bonusPoints(courses, activities)
            score2 = v2 + e2 + d2 + s2 + b2

            if score2 > score1:
                scoreWriter.writerow([score2])
                # print(score2, _)
            else:
                scoreWriter.writerow([score1])
                swapRoomSlot(randList[0], randList[1], rngSchedule)
                # print(score1, _)
                # print('swapback', object1.room, object2.room)
                # print(object1.room, object2.room)
                # print(i)

    return rngSchedule
