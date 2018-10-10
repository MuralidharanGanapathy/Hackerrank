n = int(input())
s = input()
a, b = 0,0
for s1 in s:
    if s1 == 'D':
        b -= 1
    else:
        if b == -1:
            a += 1
        b += 1
print(a)
