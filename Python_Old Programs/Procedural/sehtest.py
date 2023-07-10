#!/usr/bin/python

names = ['Jack', 'Jill', 'John', 'Jeff']

def Search(name):

	index = 0
	if len(name) < 4: raise IndexError
	for nm in names:
		if name == nm: 
			return index
		index += 1
	raise KeyError

def Action():
	
	name = raw_input('Enter name: ')
	try:
		index = Search(name)
		print name, 'found at index', index
	except KeyError:
		print 'ERROR: No such name', name

if __name__ == '__main__':
	
		print 'Resource Allocated'

		try:
			Action()
		except:
			print 'Unknown error'
		finally:
			print 'Resource Released'

















