#!/usr/bin/python

import shelve

jack = {'id':1001, 'salary':25000}
jill = {'id':1002, 'salary':35000}
john = {'id':1003, 'salary':45000}
jeff = {'id':1004, 'salary':55000}

salesDept = shelve.open('emp.shl')

salesDept['Jack'] = jack
salesDept['Jill'] = jill
salesDept['John'] = john
salesDept['Jeff'] = jeff

salesDept.close()













