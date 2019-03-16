from itertools import combinations
#from itertools import chain

n = int(input())

l = input().split()

c = int(input())

combo = list(map(list,list(combinations(l, c))))

length = len(combo)

a_counter = 0

for i in combo:
    if 'a' in i:
        a_counter = a_counter + 1

print("%0.3f"%(a_counter/length))



