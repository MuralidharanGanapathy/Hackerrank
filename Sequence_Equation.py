n = int(input())
l = ['w']
l = l+list(map(int,input().split()))
for i in range(1,len(l)):
    a = l.index(i)
    b = l.index(a)
    print(b)

