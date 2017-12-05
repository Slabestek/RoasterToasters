# generate random rooster
# swap function (days, activities)
from random import randint as randint
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.helpers import randomSchedule as randomSchedule
from modules.scheduleRange import days, timeslots, rooms as days, timeslots, rooms
from main import rooms as rooms

def climbHill(scheduleList, activities, iterations):

    # generate a random schedule
    randomSchedule(scheduleList, days, timeslots, rooms, activities)
    for i in range(iterations):
        object1 = scheduleList[randint(0, days)][randint(0, timeslots)][randint(0, rooms)]
        object2 = scheduleList[randint(0, days)][randint(0, timeslots)][randint(0, rooms)]
        print(object1, object2)
        swapRoomSlot(object1, object2, scheduleList)
