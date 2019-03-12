import collections

d = collections.OrderedDict()

for _ in range(int(input())):
    ip = input()
    if ip in d:
        d[ip] = d[ip]+1
    else:
        d[ip] = 1
for key,values in d.items():
    print(values,end = " ")
