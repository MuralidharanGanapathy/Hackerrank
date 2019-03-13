input()
set1 = set(input().split())

for _ in range(int(input())):
    l = input().split()

    if l[0] == "intersection_update":
        set1.intersection_update(set(input().split()))
    elif l[0] == "update":
        set1.update(set(input().split()))
    elif l[0] == "difference_update":
        set1.difference_update(set(input().split()))
    elif l[0] == "symmetric_difference_update":
        set1.symmetric_difference_update(set(input().split()))
print(sum(map(int, set1)))
