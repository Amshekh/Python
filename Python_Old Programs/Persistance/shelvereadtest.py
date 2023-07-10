#!/usr/bin/python

import shelve

salesDept = shelve.open('emp.shl', 'r')

for key in salesDept:
	print key, '=>', salesDept[key]['id'], '\t', salesDept[key]['salary']

salesDept.close()













