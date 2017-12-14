from random import randint, random
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import (
    extraStudent, validSchedule,
    doubleStudent, scheduleSpread, bonusPoints
)
from math import exp
import csv


def annealedSim(rngSchedule, activities, courses, iters):

    with open('simAnnealing.csv', 'w', newline = '') as csvfile:
        scoreWriter = csv.writer(csvfile)

        temp = 10000
        coolingRate = 0.003
        randObj = 2
        n = 1

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

            v, e, d, s, b = validSchedule(rngSchedule), extraStudent(rngSchedule), doubleStudent(rngSchedule), scheduleSpread(rngSchedule), bonusPoints(courses, activities)
            score1 = v + e + d + s + b

            swapRoomSlot(randList[0], randList[1], rngSchedule)

            v2, e2, d2, s2, b2 = validSchedule(rngSchedule), extraStudent(rngSchedule), doubleStudent(rngSchedule), scheduleSpread(rngSchedule), bonusPoints(courses, activities)
            score2 = v2 + e2 + d2 + s2 + b2
            probability = acceptProbability(score1, score2, temp)
            if probability < random():
                swapRoomSlot(randList[0], randList[1], rngSchedule)
                scoreWriter.writerow(['oldScore', score1, score2, temp])
            else:
                scoreWriter.writerow(['newScore', score1, score2, temp])

            temp *= 1-coolingRate
            itercount += 1

            if itercount == 2000 * n:
                temp = 10000
                n += 1


    return rngSchedule


def acceptProbability(oldScore, newScore, temp):

    if newScore > oldScore:
        return 1.0
    else:
        return (exp((oldScore - newScore) / temp)) - 1
