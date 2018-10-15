#To get the input string
s=input()
#To get the number of times of character repititions
n=int(input())
#If input string is a single a
if s=="a":
    print(n)
else:
    #To get string length
    l1=len(s)
    #To get the number of repition of whole string
    les=int(n/l1)
    #To get the number of characters added up after 
    mod=int(n%l1)
    count=0
    #To find how many a is in the given string input
    for i in range(0,l1):
        if s[i]=='a':
            count+=1
    #to get the number of a's to be repeated after and if there are 2 substrings present after #character repitition
    res=count*les
    #to get remaining a afetr the complete substring
    for i in range(0,mod):
        if s[i]=='a':
            res+=1
    print (int(res))
