import ctypes

dij = ctypes.CDLL('./libdij.so')

m = input('Enter first integer: ')
n = input('Enter second integer: ')

print 'G.C.D =', dij.GreatestDivisor(m, n)


