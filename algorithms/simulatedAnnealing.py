from random import randint, random
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import score
from math import exp
import csv


def annealedSim(rngSchedule, activities, courses, iters, students):

    with open('simAnnealing.csv', 'w', newline = '') as csvfile:
        scoreWriter = csv.writer(csvfile)

        oldScore = score(rngSchedule, courses, activities, students)
        temp = 10000
        coolingRate = 0.003
        randObj = 2
        tempJumps = 1

        # calc score1
        itercount = 0
        while itercount < iters:

            randList = []
            for i in range(randObj):
                rDay = randint(0, (days - 1))
                rTime = randint(0, (timeslots - 1))
                rRoom = randint(0, (rooms - 1))
                randList.append(rngSchedule[rDay][rTime][rRoom])

            # rDay1 = randint(0, (days - 1))
            # rTime1 = randint(0, (timeslots - 1))
            # rRoom1 = randint(0, (rooms - 1))
            # object2 = rngSchedule[rDay1][rTime1][rRoom1]

            swapRoomSlot(randList[0], randList[1], rngSchedule)

            newScore = score(rngSchedule, courses, activities, students)

            probability = acceptProbability(oldScore, newScore, temp)
            if probability < random():
                swapRoomSlot(randList[0], randList[1], rngSchedule)
                scoreWriter.writerow([oldScore, temp, probability])
            else:
                scoreWriter.writerow([newScore, temp, probability])
                oldScore = newScore

            temp *= 1-coolingRate
            itercount += 1

            if itercount == 1000 * tempJumps:
                temp = 10000
                tempJumps += 1


    return rngSchedule


def acceptProbability(oldScore, newScore, temp):

    if newScore > oldScore:
        return 1.0
    else:
        return 1 / (1 + (exp((newScore - oldScore) / temp)))
