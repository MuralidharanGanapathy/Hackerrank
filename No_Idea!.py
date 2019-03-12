n, m = input().split()

array = input().split()

set1 = set(input().split())
set2 = set(input().split())

#i is the iterator that runs all through the 'array' of elements. It returns True which value is 1 if the element is present.The subtract
#is used to nullify if the element is present in both sets acting as a counter balance and gives -1 if only present in set2
#The values will be appended on list and sum will give us the overall sum

print(sum([(i in set1) - (i in set2) for i in array]))
