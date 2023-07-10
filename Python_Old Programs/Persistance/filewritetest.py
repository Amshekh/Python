#!/usr/bin/python

jack = [1001, 25000]
jill = [1002, 35000]
john = [1003, 45000]
jeff = [1004, 55000]

salesDept = [jack, jill, john, jeff]

empfile = open('emp.txt', 'w')

for emp in salesDept:
	print >> empfile, emp[0], '\t', emp[1]

empfile.close()


