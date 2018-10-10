n = input()
ar=input()
l1=ar.split()
s=set(l1)
b=0
for i in s:
    a=l1.count(i)
    if(a%2==0) and a>1:
        b=b+(a/2)
    elif (a%2==1) and a>1:
        a=a+1
        b=b+((a/2)-1)
print(int(b))
