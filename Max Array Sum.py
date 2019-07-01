o = int(input())
lister = list(map(int,input().split()))
incl = 0
excl = 0
for i in lister:
    temp = incl
    incl = max(incl,excl+i)
    excl = temp
print(max(incl,excl))
    
