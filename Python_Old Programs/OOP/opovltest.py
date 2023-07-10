#!/usr/bin/python

class Interval:

	__minutes = 0
	__seconds = 0

	def __init__(self, minutes, seconds):
		self.__minutes = minutes + (seconds / 60)
		self.__seconds = seconds % 60

	def Print(self):
		print self.__minutes, ":", self.__seconds

	def __add__(self, other):
		m = self.__minutes + other.__minutes
		s = self.__seconds + other.__seconds
		return Interval(m, s)

	def __str__(self):
		return "%sm,%ss" % (self.__minutes, self.__seconds)

if __name__ == '__main__':
	
	a = Interval(7, 30)
	a.Print()
	print a		# a.__class__.__str__(a)
	b = Interval(8, 20)
	b.Print()
	
	c = a + b
	c.Print()

















