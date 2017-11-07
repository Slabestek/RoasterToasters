import csv

class room:
	def __init__(self, name, cap):
		self.name = name
		self.cap = cap

	def __repr__(self):
		return self.name
	
myList = []
	
with open('rooms.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		myList.append(row) 

a104 = room(myList[2], myList[3])
a106 = room(myList[4], myList[5])

print myList
print a104
print a106
zalen = [a104,a106]
print zalen
