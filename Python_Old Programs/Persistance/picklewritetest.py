#!/usr/bin/python

import pickle

jack = [1001, 25000]
jill = [1002, 35000]
john = [1003, 45000]
jeff = [1004, 55000]

salesDept = [jack, jill, john, jeff]

empfile = open('emp.pkl', 'w')

pickle.dump(salesDept, empfile)

empfile.close()













