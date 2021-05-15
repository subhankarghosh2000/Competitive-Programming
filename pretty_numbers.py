T = int(input())
for i in range(T):
	A, B = [int(v) for v in input().split()]
	c=0
	for i in range(A,B+1):
		if i%10==2 or i%10==3 or i%10==9 :
			c=c+1
	print(c)
