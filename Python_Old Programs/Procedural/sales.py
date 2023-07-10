#!/usr/bin/python

jack = {'id':1001, 'name':'Jack', 'salary':25000}
jill = dict(id=1002, name='Jill', salary=35000)

salesDept = {'Jack':jack, 'Jill':jill}

#print "-- Module name: ", __name__

if __name__ == '__main__':

	for key in salesDept:
		print salesDept[key]['salary']




