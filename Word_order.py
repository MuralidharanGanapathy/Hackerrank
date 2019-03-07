str_list = []
for i in range(int(input())):
    str_list.append(input())
print(len(set(str_list)))
#To sort the list of unique strings on the order of input list
list1 = sorted(set(str_list), key = str_list.index)
l = []
for i in list1:
    l.append(str(str_list.count(i)))
print(" ".join(l))
