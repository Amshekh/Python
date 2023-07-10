#!/usr/bin/python

jack = [1001, 'Jack', 25000]

print jack

print jack[0],
print jack[1],
print jack[2]

jack[2] += 5000

print jack[2]
print jack
del jack[2]
print jack
#print jack[2]

deptno = input('Enter deptno: ')
jack.append(deptno)
print jack
jack.reverse()
print jack




















