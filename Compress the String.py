from itertools import groupby
for i,j in groupby(input()):
    print(i, len(list(j)))
