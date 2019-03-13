from collections import Counter
input()
l = input().split()

set1 = list(set(l))
cnter = Counter(l)

for i in set1:
    if cnter[i] == 1:
        print(i)
