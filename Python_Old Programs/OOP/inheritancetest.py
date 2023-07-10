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

#***************************************************************************

def IncomeTax(emp):	# double IncomeTax(const Employee& emp)
	income = emp.GetNetIncome()
		   # emp.__class__.GetNetIncome(self)
	excess = income - 20000
	if excess > 0:
		return excess * 0.1
	else:
		return 0

if __name__ == '__main__':
	
	jack = Employee(190, 100)
	jill = SalesPerson(190, 100, 100000)

	print "Jack's income is ", jack.GetNetIncome()
	print "Jill's income is ", jill.GetNetIncome()

	print "Jack's tax amount is ", IncomeTax(jack)
	print "Jill's tax amount is ", IncomeTax(jill)
	















