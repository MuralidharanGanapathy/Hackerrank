import math
for p in range(int(input())):
    n,m=list(map(int,input().split()))
    c=math.floor(math.sqrt(m)) - math.floor(math.sqrt(n-1))
    print(c)

