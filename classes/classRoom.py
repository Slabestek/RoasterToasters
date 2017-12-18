import csv
'''
This class contains information on rooms. It stores whether or not the room
is full, as well as it's capacity.
'''
class Room:
	def __init__(self, name, cap, full = {}):
		self.name = name
		self.cap = int(cap)
		self.full = full

	def __repr__(self):
		return self.name
