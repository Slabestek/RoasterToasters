import csv

class Room:
	def __init__(self, name, cap, full = {}):
		self.name = name
		self.cap = int(cap)
		self.full = full

	def __repr__(self):
		return self.name
