import Box

l, b, h = input('Box dimensions: ')
area = Box.OuterArea(l, b, h)
print 'Outer area =', area

t = input('Box thickness: ')
try:
	volume = Box.InnerVolume(l, b, h, t)
	print 'Box volume =', volume
except Box.DimensionError, de:
	print 'ERROR:', de



