s=input()
l1=s.split()
li1=list(map(int,l1))
s2=input()
arr1=s2.split()
m=[0]*li1[0]
for i in range(li1[0]):
    new=(i+(li1[0]-li1[1]))%li1[0]
    m[new]=arr1[i]
print(*m)
