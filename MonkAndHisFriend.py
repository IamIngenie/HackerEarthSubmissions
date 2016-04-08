'''Dated 14/9/15
   Bit Manipulation 

https://www.hackerearth.com/code-monk-bit-manipulation/algorithm/monk-and-his-friend/description/
   '''

for i in range( input()) :
	p, m = map (int, raw_input().split())
	check = p^m
	print bin( check).count("1")


