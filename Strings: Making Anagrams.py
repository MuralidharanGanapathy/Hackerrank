from collections import Counter
str1 = input()
str2 = input()
char_list = list(set(str1 + str2))
count1 = Counter(str1)
count2 = Counter(str2)
ct = 0
for i in char_list:
    if count1[i] == count2[i]:
        continue
    elif count1[i] > count2[i]:
        ct += count1[i] - count2[i]
    elif count2[i] > count1[i]:
        ct += count2[i] - count1[i]
print(ct)
        
