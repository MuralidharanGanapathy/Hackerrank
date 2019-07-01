n, amount = list(map(int, input().split()))
lister = sorted(map(int, input().split()))
stack = []
i = 0
while sum(stack)<=amount:
    stack.append(lister[i])
    i+=1
print(i-1)
