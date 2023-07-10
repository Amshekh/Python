#!/usr/bin/python

jack = {'id':1001, 'salary':25000}
jill = {'id':1002, 'salary':35000}
john = dict(id=1003, salary=45000)

salesDept = {'Jack':jack, 'Jill':jill, 'John':john} 

def Add(first, *args):

	sum = first
	for val in args:
		sum += val
	return sum

def AddKeys(**keyargs):

	sum = 0
	for key in keyargs:
		sum += keyargs[key]
	return sum

def AppendRecord(key, **dictvalues):

	salesDept[key] = dict(dictvalues)

if __name__ == '__main__':
	
	print 'Result = ', Add(10, 20, 30)
	print 'Result = ', Add(10, 20, 30, 40)
	print 'Result = ', AddKeys(first=10, second=20, third=30, fourth=40)
	AppendRecord('Jeff', id=1004, salary=55000)

	for key in salesDept:
		print key, '=>', salesDept[key]['id'], '\t', salesDept[key]['salary']
















