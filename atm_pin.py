import math
T=0
try:
    T = int(input())
except EOFError:
    pass
for i in range(T):
	N = int(input())
	q=pow(10,int(N/2))
	print('1'+' '+str(q))
