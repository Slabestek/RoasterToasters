class course:
	def __init__(self, name, hcol = 0, wcol = 0, prac = 0, studnrs = {}):
		self.name = name
		self.hcol = hcol
		self.wcol = wcol
		self.prac = prac
		self.studnrs = studnrs

	def enroll(self, studnr):
		self.studnrs.append(studnr)


heuristieken = course("heuristieken", 2, 1, 0)

for i in range(10):
	heuristieken.studnrs = i

print heuristieken



	
