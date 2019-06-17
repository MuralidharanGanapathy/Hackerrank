n = int(input())
l1 = []
l2 = []
l = [[0 for i in range(n)]for j in range(n)]
if __name__ == '__main__':
    for i in range(n):
        name = input()
        score = float(input())
        l[i-1][i] = name
        l[i][i] = score
        l1.append(score)
l1 = sorted(set(l1))
min2 = l1[1]
for i in range(0,n):
    if l[i][i] == min2:
        l2.append(l[i-1][i])
l2 = sorted(l2)
for i in l2:
    print(i)
        


