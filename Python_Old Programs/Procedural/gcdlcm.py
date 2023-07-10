def GCD(first, second):
	
	while first != second:
		if first > second: 
			first -= second
		else:
			second -= first
	
	return first

def LCM(first, second):

	g = GCD(first, second)
	
	return first * second / g

	



















