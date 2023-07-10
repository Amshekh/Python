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
		   # emp.vptr[0](emp)
	excess = income - 20000
	if excess > 0:
		return excess * 0.1
	else:
		return 0

def AverageSales(dept):
	total = 0
	count = 0
	for e in dept:
		if isinstance(e, SalesPerson):
			total += e.GetSales()
			count += 1

	return total / count

if __name__ == '__main__':
	
	salesDept = [Employee(180, 100), Employee(120, 60), SalesPerson(180, 100, 100000), Employee(190, 150), SalesPerson(225, 175, 200000)]

	for emp in salesDept:
		print emp.GetHours(), '\t', emp.GetRate(), '\t', emp.GetNetIncome()

	print 'Average sales = ', AverageSales(salesDept)















