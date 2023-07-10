#!/usr/bin/python

jack = {'id':1001, 'name':'Jack', 'salary':25000}
jill = dict(id=1002, name='Jill', salary=35000)

#key = raw_input('Enter key: ')

#print jack[key]
print jack
print jill

id = input('Enter id: ')
name = raw_input('Enter name: ')
salary = input('Enter salary: ')

jeff = dict(id=id, name=name, salary=salary)
print jeff

for key in jack:
	print key, '=>', jack[key]










