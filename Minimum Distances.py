n = int(input())
lister = list(map(int, input().split()))
unique_list = list(set(lister))

sample_list = []
for i in range(len(lister)):
    for j in range(i+1, len(lister)):
        if lister[i] == lister[j]:
            sample_list.append(abs(i-j))
if len(sample_list) > 0:
    print(min(sample_list))
else:
    print(-1)

