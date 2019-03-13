from collections import Counter
n = input()
l = list(map(int, input().split()))
cnter = Counter(l)
set1 = set(l)
l1 = []
for i in set1:
    l1.append(cnter[i])
print(int(n) - max(l1))
