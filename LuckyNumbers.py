# https://www.hackerearth.com/codexplodEasy/algorithm/lucky-numbers-8/
# Lucky Numbers
		
for i in range(input()):
	neg, arr = input(), map(int, raw_input().split())
	temp,ans =arr[neg-1], 1
	for i in reversed(range(neg-1) ):
		if arr[i] > temp:
			temp = arr[i]/
			ans +=1
	print ans
	  
"""
a =[0,1,2,3,4,5,6,7,8,9,10]
for i in reversed(range(len(a))):
	print a[i],
"""