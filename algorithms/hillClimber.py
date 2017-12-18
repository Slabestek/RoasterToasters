from random import randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import score
import csv


def climbHill(rngSchedule, activities, i, courses, students):

    with open('hillClimb' + str(i) + 'iter.csv', 'w', newline = '') as csvfile:
        scoreWriter = csv.writer(csvfile)

        randObj = 2
        oldScore = score(rngSchedule, courses, activities, students)
        for _ in range(i):

            randList = []
            for j in range(randObj):
                rDay = randint(0, (days - 1))
                rTime = randint(0, (timeslots - 1))
                rRoom = randint(0, (rooms - 1))
                randList.append(rngSchedule[rDay][rTime][rRoom])

            swapRoomSlot(randList[0], randList[1], rngSchedule)

            newScore = score(rngSchedule, courses, activities, students)

            if newScore > oldScore:
                scoreWriter.writerow([newScore])
                oldScore = newScore
                # print(score2, _)
            else:
                scoreWriter.writerow([oldScore])
                swapRoomSlot(randList[0], randList[1], rngSchedule)

    return rngSchedule
