ip=input()
l1=ip.split()
b=int(l1[0])
n=int(l1[1])
m=int(l1[2])
n1=input()
k=n1.split()
keyb=sorted(list(map(int,k)))
m1=input()
u=m1.split()
usb=sorted(list(map(int,u)))
maxi=0
t=0
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        t+=1
        if keyb[i]+usb[j]<=b and keyb[i]+usb[j]>maxi:
            maxi=keyb[i]+usb[j]
if t==i*j:
    print(-1)
else:
    print(maxi)
