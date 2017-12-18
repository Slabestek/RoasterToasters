from random import randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms
from modules.score import score
import csv

'''  
Hillclimber algorithm. 
Writes data to a CSV file, generates a random schedule and then starts swapping room slots.
If a swap results in a higher score, the swap stays and it continues to the next swap. If the swap
results in a lower score it 'discards' the swap and continues to the next swap. This way, the
schedule will become better and better eventually.
'''

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
            else:
                scoreWriter.writerow([oldScore])
                swapRoomSlot(randList[0], randList[1], rngSchedule)

    return rngSchedule
