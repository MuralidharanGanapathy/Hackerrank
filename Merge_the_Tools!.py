def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        l = list(string[i:k+i])
        #to sort the list based on its index 
        print("".join(sorted(set(l), key =l.index )))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
