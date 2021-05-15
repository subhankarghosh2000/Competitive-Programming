import math
def center_dist(x1,x2,y1,y2):
	d=math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
	return d
N=0
Q=0
try:
    N,Q=[int(v) for v in input().split()]
except EOFError:
    pass
X,Y,R,K=[],[],[],[]
if N==0 or N==1 or Q==0  :
	exit()
for i in range(N):
	x,y,r=[int(v) for v in input().split()]
	X.append(x)
	Y.append(y)
	R.append(r) 
for i in range(Q):
	k=int(input())
	K.append(k)
ld=0
sd=0
arr=[0]*(1000002)
for j in range(N):
	for l in range(j+1,N):
		dis=center_dist(X[j],X[l],Y[j],Y[l])
		if dis==0:
			if R[j]==R[l]:
				ld=0
				sd=0
			else:
				if (R[j]-R[l])>0:
					sd=math.ceil(R[j]-R[l])
					ld=math.floor(sd+(2*R[l]))
				else:
					sd=math.ceil(R[l]-R[j])
					ld=math.floor(sd+(2*R[j]))
		elif dis>=(R[j]+R[l]):
			sd=math.ceil(dis-R[j]-R[l])
			ld=math.floor(dis+R[j]+R[l])
		elif (dis+R[l])<R[j]:
			ld=math.floor(dis+R[j]+R[l])
			sd=math.ceil(R[j]-dis-R[l])
		elif (dis+R[j])<R[l]:
			ld=math.floor(dis+R[j]+R[l])
			sd=math.ceil(R[l]-dis-R[j])
		elif (((dis+R[l])>=R[j]) or ((dis+R[j])>=R[l])):
			ld=math.floor(dis+R[j]+R[l])
			sd=0
		arr[sd]+=1
		arr[ld+1]=arr[ld+1]-1
for i in range(1,1000002):
    arr[i]+=arr[i-1]
for k in range(0,Q):
    print(arr[K[k]])
