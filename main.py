import jinja2
from flask import Flask, render_template
import random
from modules.helpers import swapRoomSlot as swapRoomSlot
from modules.init import createObjects as createObjects
from modules.init import enrollStudent as enrollStudent
from modules.init import fillActivities as fillActivities
from terminaltables import AsciiTable
from modules.scheduleRange import days, timeslots, dayStrings
from modules.scheduleRange import rooms as numRooms
from algorithms.hillClimber import climbHill as climbHill
from modules.helpers import randomSchedule

# create the classes and put the returned object in a variable
courses, students, rooms, activities = createObjects()

# make empty matrix
scheduleList = [[[None] * numRooms for i in range(timeslots)] for j in range(days)]
noneList = [None] * 11
activities.extend(noneList)

# for activity in activities:
# 	print(activity)

# print(len(activities))

# table = AsciiTable(scheduleList)
# print(table.table)

enrollStudent(students)
fillActivities(courses)

climbHill(scheduleList, activities, 10)

randomSchedule(scheduleList, days, timeslots, numRooms, activities, rooms)


# Run Flask in terminal:
# FLASK_APP=main.py flask run
# http://127.0.0.1:5000/

app = Flask(__name__)

@app.route("/")
def roosterPrint():

	coursePrint = scheduleList

	return render_template("rooster4.html", coursePrint = coursePrint, numRooms = numRooms, 
		days = days, timeslots = timeslots)
