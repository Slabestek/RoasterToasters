from random import randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import (
    extraStudent, validSchedule,
    doubleStudent, scheduleSpread, bonusPoints
)
import csv


def climbHill(rngSchedule, activities, i, courses, students):

    with open('randomWalk' + str(i) + 'iter.csv', 'w', newline = '') as csvfile:
        scoreWriter = csv.writer(csvfile)

        bestSch = []
        randObj = 2
        for _ in range(i):

            randList = []
            for j in range(randObj):
                rDay = randint(0, (days - 1))
                rTime = randint(0, (timeslots - 1))
                rRoom = randint(0, (rooms - 1))
                randList.append(rngSchedule[rDay][rTime][rRoom])

            v, e, d, s, b = validSchedule(rngSchedule), extraStudent(rngSchedule), doubleStudent(rngSchedule, students), scheduleSpread(rngSchedule), bonusPoints(courses, activities)
            score1 = v + e + d + s 

            swapRoomSlot(randList[0], randList[1], rngSchedule)
            scoreWriter.writerow([score1])
            
    # scoreWriter.writerow([rngSchedule])
    return rngSchedule