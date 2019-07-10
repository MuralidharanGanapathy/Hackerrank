n1,n2,k = list(map(int,input().split()))
c = 0
for i in range(n1,n2+1):
    j = int(str(i)[::-1])
    a = abs(i-j)
    if a%k == 0:
        c+=1
print(c)
