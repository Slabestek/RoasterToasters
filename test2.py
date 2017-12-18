# import jinja2
from flask import Flask, render_template


# Run Flask in terminal:
# FLASK_APP=test2.py flask run
# http://127.0.0.1:5000/

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

@app.route("/")
def roosterPrint():

	# coursePrint = scheduleList[day][timeslot][room]
    # return render_template("rooster.html", coursePrint = coursePrint)
    return render_template("rooster.html")


if __name__ == '__main__':
	# app.debug = True
	app.run(debug=True)
	# app.run(port=5000)



