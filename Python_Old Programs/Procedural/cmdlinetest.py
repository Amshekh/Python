#!/usr/bin/python

import sales
import sys

if len(sys.argv) > 1:
	key = sys.argv[1]
	print sales.salesDept[key]['id'], '\t', sales.salesDept[key]['salary']
	exit()

for key in sales.salesDept:
	print key, '=>', sales.salesDept[key]['id'], '\t', sales.salesDept[key]['salary']
	

