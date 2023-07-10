import ShMem

text = ShMem.GetString()
if text is None:
	print 'ERROR: Cannot access shared-memory.'
else:
	print 'Shared-text:', text


