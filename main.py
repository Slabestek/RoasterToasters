'''
In the main file, we run the algorithms, create the schedules and run the
visualization. Createobjects is a function defined in init.py where all
the class-objects are made. Emptyschedule does what it says, it creates an
empty schedule. We enroll students in their courses and activities, whereafter
we create a random schedule. The algorithms are run at the end. They can be
commented out if you only want to run a certain algorithm. The numbers in their
arguments are the number of iterations. Below that is the code for Flask.
Flask is used to visualize a random schedule, by default it takes rngSchedule
as input. You can run this in your terminal with "FLASK_APP=main.py flask run".
It serves on 127.0.0.1:5000.
'''
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
from algorithms.hillClimber import climbHill
from algorithms.simulatedAnnealing import annealedSim
from modules.score import score
from math import exp
from algorithms.randomWalk import randomWalk

courses, students, rooms, activities = createObjects()

scheduleList = emptySchedule(days, timeslots, numRooms)

enrollStudent(students)
fillActivities(courses)
rngSchedule = randomSchedule(scheduleList, days, timeslots, numRooms, activities, rooms)

climbHill(rngSchedule, activities, 100, courses, students)
annealedSim(rngSchedule, activities, courses, students)
randomWalk(rngSchedule, activities, 100, courses, students)


app = Flask(__name__)

@app.route("/")
def roosterPrint():

	coursePrint = rngSchedule

	return render_template("rooster4.html", coursePrint = coursePrint, numRooms = numRooms,
		days = days, timeslots = timeslots)
