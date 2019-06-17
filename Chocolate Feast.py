for _ in range(int(input())):
    money,cost,no_of_wrappers = (map(int, input().split()))
    initial_chocolates = int(money/cost)
    initial_wrapper = initial_chocolates
    wrappers = initial_wrapper
    while(initial_wrapper >= no_of_wrappers):
        choco_wrappers = int(initial_wrapper / no_of_wrappers)
        wrappers += choco_wrappers
        initial_wrapper = (initial_wrapper % no_of_wrappers) + choco_wrappers
    print(wrappers)
