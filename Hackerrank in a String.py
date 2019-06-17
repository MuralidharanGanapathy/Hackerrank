for _ in range(int(input())):
    hackerrank = list("hackerrank")
    s = list(input())
    t = -1
    cnt = 0
    for i in range(len(hackerrank)):
        if hackerrank[i] in s:
            t = s.index(hackerrank[i])
            del s[0:t+1]
            cnt += 1
        else:
            print("NO")
            break
    if cnt == len(hackerrank):
        print("YES")
