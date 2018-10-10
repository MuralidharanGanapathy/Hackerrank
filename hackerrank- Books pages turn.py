n=int(input())
p=int(input())
cnt=0
if n-p>=p:
    for i in range(1,n+1,2):
        if i<p:
            cnt=cnt+1
        elif i>=p:
            break
elif p>n-p:
    if n%2==1:
        p=p+1
    for i in range(n,p-1,-2):
        if i>p:
            cnt=cnt+1
        elif i<=p:
            break
print(cnt)
