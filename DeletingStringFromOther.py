a, b = list(raw_input()),list(raw_input())
for i in b:
	if i in a:
		a.remove(i)
print ''.join(a) 