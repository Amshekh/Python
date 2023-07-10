from ctypes import *

inv = CDLL('./libinv.so')

class FixedDeposit(Structure):
	_fields_ = [('id', c_long), ('amount', c_double), ('period', c_long)]
inv.InitFixedDeposit.argtypes = [c_double, c_long, POINTER(FixedDeposit)]

amt = input('Amount: ')
prd = input('Period: ')
fd = FixedDeposit()
inv.InitFixedDeposit(amt, prd, byref(fd))
print 'Fixed-Deposit ID:', fd.id

Scheme = CFUNCTYPE(c_float, c_double, c_long)
inv.GetMaturityValue.argtypes = [POINTER(FixedDeposit), Scheme]
inv.GetMaturityValue.restype = c_double
mv = inv.GetMaturityValue(byref(fd), 
		Scheme(lambda x, y: 7.5 if y < 3 else 8.5))
print 'Maturity-Value: %.2f' % mv
















