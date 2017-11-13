import csv

class Room:
	def __init__(self, name, cap):
		self.name = name
		self.cap = cap

	def __repr__(self):
		return self.name

#csv inlezen in python

#voor elke student een object maken
	#waarden van elke student toevoegen aan object

myList = []
	
with open('rooms.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		myList.append(row) 


