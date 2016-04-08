'''Dated 14/9/15
   Bit Manipulation 

https://www.hackerearth.com/code-monk-bit-manipulation/algorithm/monks-choice-of-numbers-1/description/
   '''


for i in range( input()) :
	n, k = map( int, raw_input().split())
	array = map( int, raw_input().split())
	ans, temp = 0, []
	for val in array :
		temp.append( bin(val).count("1"))
	temp.sort( reverse = True)
	for i in range(k):
		ans+=temp[i]
	print ans
	