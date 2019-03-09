from collections import defaultdict
grp_a = []
grp_b = []

l = defaultdict(list)

n,m = list(map(int, input().split()))

for i in range(n):
    grp_a.append(input())
for j in range(m):
    grp_b.append(input())

l3 = [0]

for i in grp_b:
    if i in grp_a:
        l[i].append(" ".join([str(j+1) for j, x in enumerate(grp_a) if x == i]))
    else:
        #l3[0] = "-1"
        l[i].append(-1)

for i in grp_b:
    print(l[i][0])
