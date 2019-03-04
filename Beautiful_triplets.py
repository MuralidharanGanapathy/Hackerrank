import sys
x = list(map(int,input().strip().split(' ')))
n=x[0]
d=x[1]
a = list(map(int,input().strip().split(' ')))
count=0
for i in range(n):
    if a[i]+d in a and a[i]+2*d in a:
        count+=1
print(count)
