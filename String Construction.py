for _ in range(int(input())):
    stack = []
    string_ip = input()
    string_list = list(string_ip)
    cost = 0
    for i in string_list:
        if i not in stack:
            stack.append(i)
            cost += 1
    print(cost)
