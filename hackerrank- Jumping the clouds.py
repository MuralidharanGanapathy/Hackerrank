n=int(input())
s=input()
l1=s.split()
li=list(map(int,l1))
i=0
cnt=0
while(1):
    if i==n-1:
        break
    if i==n-2:
        if li[i+1]==0:
            cnt=cnt+1
            break
    if i==n-3:
        if li[i+2]==0:
            cnt=cnt+1
            break
        elif li[i+1]==0:
            cnt=cnt+1
            break
        else:
            break
    if li[i+2]==0:
        i=i+2
        cnt+=1
    elif li[i+1]==0:
        i=i+1
        cnt+=1

print(cnt)
        


Language Version:  3.6.5
