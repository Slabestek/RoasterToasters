import random
import jinja2
from flask import Flask, render_template
from classes.classActivity import Activity
from modules.helpers import (
    swapRoomSlot, randomSchedule as
    swapRoomSlot, randomSchedule
)
from modules.init import (
    createObjects, enrollStudent, fillActivities, emptySchedule
)
from terminaltables import AsciiTable
from modules.scheduleRange import (
    days, timeslots
)
from modules.scheduleRange import rooms as numRooms
from algorithms.hillClimber import climbHill as climbHill
from modules.score import (
    extraStudent, validSchedule,
    doubleStudent, scheduleSpread
)

# create the classes and put the returned object in a variable
courses, students, rooms, activities = createObjects()


# make empty schedule
scheduleList = emptySchedule(days, timeslots, numRooms)

enrollStudent(students)
fillActivities(courses)
rngSchedule = randomSchedule(scheduleList, days, timeslots, numRooms, activities, rooms)

climbHill(rngSchedule, activities, 2)


app = Flask(__name__)

@app.route("/")
def roosterPrint():

	coursePrint = rngSchedule

	return render_template("rooster4.html", coursePrint = coursePrint, numRooms = numRooms,
		days = days, timeslots = timeslots)

# FLASK_APP=test.py flask run
