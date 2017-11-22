import csv

class Room:
	def __init__(self, name, cap):
		self.name = name
		self.cap = cap

	def __repr__(self):
		return self.name
