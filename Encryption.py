import math
s = input()
length = len(s)
lister = []
sqr_root = math.sqrt(length)
floor = math.floor(sqr_root)
ceil = math.ceil(sqr_root)

if floor*ceil < length:
    while(floor*ceil < length):
        floor += 1
for i in range(0,length,int(math.ceil((length/floor)))):
    string_sample = s[i:ceil+i]
    lister.append(string_sample)
for i in range(ceil):
    string = ""
    for j in range(len(lister)):
        if i >= len(lister[j]):
            break
        string = string + lister[j][i]
    print(string, end = " ")
