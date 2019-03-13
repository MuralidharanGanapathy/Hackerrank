input()
set1 = set(map(int, input().split()))
input()
set2 = set(map(int, input().split()))
list1 = []
list1 = list(set1.difference(set2))
list2 = []
list2 = list(set2.difference(set1))
list3 = list1 + list2
for i in sorted(list3):
    print(i)
