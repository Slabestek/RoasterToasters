import csv
import collections

# source: https://stackoverflow.com/questions/9247241/python-algorithm-of-counting-occurrence-of-specific-word-in-csv

course1 = collections.Counter()
with open('studentenenvakken.csv') as input_file:
	for row in csv.reader(input_file, delimiter = ','):
		course1[row[3]] += 1
		course1[row[4]] += 1
		course1[row[5]] += 1
		course1[row[6]] += 1
		course1[row[7]] += 1

print "Number of students in course: %s" % course1['Calculus 2']
print course1.most_common()
