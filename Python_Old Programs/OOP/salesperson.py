#!/usr/bin/python

from employee import Employee

class SalesPerson(Employee):

	__sales = 0

	def __init__(self, hours, rate, sales):	# Employee(hours, rate)
		Employee.__init__(self, hours, rate)
		self.__sales = sales
		print 'SalesPerson instance created'

	def GetSales(self):
		return self.__sales

	def SetSales(self, value):
		self.__sales = value

	def GetNetIncome(self):
		income = Employee.GetNetIncome(self)
		income += self.__sales / 100
		return income

	def __del__(self):
		print 'SalesPerson instance destroyed'
		Employee.__del__(self)

if __name__ == '__main__':
	
	jack = Employee(180, 100)
	jill = SalesPerson(180, 100, 50000)

	print "Jack's income is ", jack.GetNetIncome()
	print "Jill's income is ", jill.GetNetIncome()
		















