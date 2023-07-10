#!/usr/bin/python

empfile = open('emp.txt', 'r')

for line in empfile:
	print line,

empfile.close()


