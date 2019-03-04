def valid(l):
    flag = False
    for i in l:
        if i<0:
            flag = False
        else:
            if str(i) == str(i)[::-1]:
                flag = True
    return flag
n = int(input())
print(valid(list(map(int,input().split()))))
