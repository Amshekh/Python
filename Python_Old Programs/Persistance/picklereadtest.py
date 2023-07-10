#!/usr/bin/python

import pickle

empfile = open('emp.pkl', 'r')

salesDept = pickle.load(empfile)

for emp in salesDept:
	print emp[0], '\t', emp[1]

empfile.close()













