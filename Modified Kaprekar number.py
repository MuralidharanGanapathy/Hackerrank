flag = 0
for i in range(int(input()),int(input())+1):
    if i == 1:
        print(i, end = " ")
        continue
    sqr = str(i**2)
    length = len(str(i))
    if len(sqr) == 1:
        continue
    #print(sqr[-1-length],-1-length)
    if len(sqr) == 2*length:
        str2 = sqr[-length::]
        str1 = sqr[0:length]
    if len(sqr) == (2*length)-1:
        str2 = sqr[-length::]
        str1 = sqr[0:length-1]
    if str1 == "":
        str1 = "0"
    if int(str2)+int(str1) == i:
        flag = 1
        print(i, end = " ")
if flag == 0:
    print("INVALID RANGE")
