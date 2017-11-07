import csv

class room:
	def __init__(self, name, cap):
		self.name = name
		self.cap = cap
	
	my_list = []
	
	with open('rooms&cap.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			my_list.append(row[0], row[1])