if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    print(sorted(arr)[len(arr)-2])

