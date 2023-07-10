#!/usr/bin/python

jack = [1001, 'Jack', 25000]

key = 0

key = raw_input('Enter key: ')

if key == 'id':
	print jack[0]
elif key == 'name':
	print jack[1]
elif key == 'salary':
	print jack[2]
else:
	print 'Bad key!'


