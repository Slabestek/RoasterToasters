from random import randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import (
    score
)
import csv

'''
Random Walk algorithm.
Generates a random schedule by swapping random room slots without taking the
score into account.
'''
def randomWalk(rngSchedule, activities, i, courses, students):

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

            Score = score(rngSchedule, courses, activities, students)

            swapRoomSlot(randList[0], randList[1], rngSchedule)
            scoreWriter.writerow([Score])

    return rngSchedule
