T=0
try:
	T = int(input())
except EOFError:
	pass
N=1000001
p=[True for i in range(N)] 
p[2]=False
for i in range(2,N):
	if p[i]==True:
		for j in range(2*i,N,i):
			p[j]=False
for i in range(T):	
	n=int(input())
	if n<4:
		print('-1')
	elif n%2==0:
		print('1')
	else:
		if p[n-2]==True:
			print('1')
		else:
			print('2')




