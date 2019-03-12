def validator(l):
    if len(l) == 0:
        return False
    if len(set(l)) == 0:
        return False
    return True

n = int(input())

l = list(map(int,input().split()))

while(validator(l)):
    mini = min(l)
    i = 0
    print(len(l))
    while i<len(l):
        l[i] = l[i] - mini
        if l[i] == 0:
            del l[i]
            i-=1
        i+=1
