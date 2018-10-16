#to get the input of str length and iterations
s=input()
#To split the space seperated into list 
l1=s.split()
#To convert string list to integer
li1=list(map(int,l1))
#To get input elements from user
s2=input()
ct=0
#Run the iteration until iterator input
for i in range(0,li1[1]):
    #To convert given input elements to lists
    arr1=s2.split()
    #save the first element
    s1=arr1[0]
    #Delete the first element
    del(arr1[0])
    #Concatenate the list to string
    s2=' '.join(arr1)
    #Join the first element to the last
    s2=s2+" "+s1
print(s2)
