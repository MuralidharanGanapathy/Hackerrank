import statistics
row, column = list(map(int,input().split()))
nested = []
for i in range(column):
    nested.append(map(float,input().split()))
for i in zip(*nested):
    print("%.1f"%(sum(i)/len(i)))


    


