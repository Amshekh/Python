#!/usr/bin/python

class Employee:
	
	__hours = 0		#_Employee__hours = 0
	__rate = 0		#_Employee__rate = 0

	def __init__(this):
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
	
	jack = Employee()	# jack.__init__(jack)
	jill = jack

	jack.SetHours(180)	#jack.__class__.SetHours(jack, 180)
	jack.SetRate(100)	#jack.__class__.SetRate(jack, 100)

	print 'Hours = ', jack.GetHours()
	print 'Rate = ', jack.GetRate()
	print 'Income = ', jack.GetNetIncome()
					 # jack.__class__.GetNetIncome(jack)

	jill = 0
	print 'jill lost reference'
	jack = 0
	print 'jack lost reference'
	print 'Before GC'
# jack.__del__(jack)












