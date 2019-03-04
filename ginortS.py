s1 = ''.join(sorted(list(input())))
lo = []
up = []
eveno = []
oddno = []
for i in s1:
    if i.islower() == True:
        lo.append(i)
    elif i.isupper() == True:
        up.append(i)
    else:
        if int(i)%2==0:
            eveno.append(i)
        elif int(i)%2==1:
            oddno.append(i)
s = ''.join(lo)+''.join(up)+''.join(oddno)+''.join(eveno)
print(s)
