#!/usr/bin/python

class Employee:
	
	__hours = 0		#_Employee__hours = 0
	__rate = 0		#_Employee__rate = 0

	def __init__(this, hours=50, rate=90):
		this.__hours = hours
		this.__rate = rate
		print 'Employee instance created'

	def GetHours(this):
		return this.__hours

	def SetHours(this, value):
		this.__hours = value

	def GetRate(this):
		return this.__rate

	def SetRate(this, value):
		this.__rate = value

	def GetNetIncome(this):
		income = this.__hours * this.__rate
		ot = this.__hours - 180

		if ot > 0:
			income += 50 * ot

		return income

	def __del__(this):
		print 'Employee instance destroyed'

if __name__ == '__main__':
	
	salesDept = [Employee(), Employee(180, 100), Employee(210, 165), Employee(220, 175)]

	print 'Hours\tRate\tIncome'
	print '---------------------'
	for employee in salesDept:
		print employee.GetHours(), '\t', employee.GetRate(), '\t', employee.GetNetIncome()
	print '---------------------'



















