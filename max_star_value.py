T=0
try:
	T = int(input())
except EOFError:
	pass
for i in range(T):
	N=int(input())
	A=list(map(int, input().split()))
	A_set=set()
	max_c=0
	for i in range(N):
		if A[N-1-i] not in A_set:
			c=0
			x=A[N-1-i]
			B=A[0:N-1-i]
			for j in B:
				if j % x == 0:
					A_set.add(j)
					c+=1
			if c>max_c:
				max_c=c
	print(max_c)