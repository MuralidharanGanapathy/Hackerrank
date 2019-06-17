for _ in range(int(input())):
    flag = 0
    string = input()
    l1 = []
    rev_string = string[::-1]
    l2 = []
    for i in range(len(string)):
        l1.append(ord(string[i]))
        l2.append(ord(rev_string[i]))
    for i in range(len(l1)-1):
        if abs(l1[i]-l1[i+1]) != abs(l2[i]-l2[i+1]):
            flag = 1
    if flag == 0:
        print("Funny")
    else:
        print("Not Funny")
