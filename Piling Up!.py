for t in range(int(input())):
    z = input()
    lst = [int(i) for i in input().split()]
    min_list = lst.index(min(lst))
    left = lst[:min_list]
    right = lst[min_list+1:]
    if left == sorted(left,reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")
