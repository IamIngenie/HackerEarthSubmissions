#  https://www.hackerearth.com/problem/algorithm/binary-strings/

fibao , MOD = [1,1], 1000000007
for j in xrange(2,1000001):
	fibao.append( ( fibao[ j-1 ]%MOD + fibao[ j-2 ] % MOD ) %MOD )
	
for i in xrange(input()):
	val=input()
	print fibao[val]