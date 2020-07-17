
def validate(string, char_set):
    quo = len(string)//2
    if len(string) % 2 == 0:
        for i in char_set:
            if "".join(i) * quo == string:
                return len(string)
    else:
        for i in char_set:
            #print(string[:len(string) - 1])
            if "".join(i) * quo == string[:len(string) - 1] and string[0] == string[-1]:
                return len(string)
        
    return 0

def removal_set(string, rem_chars):
    for i in rem_chars:
        string = string.replace(i, "")
    return string
    
from itertools import combinations, permutations
input()
inp_string = input()
unique_characters = list(set(inp_string))
if len(unique_characters) > 1:
    rem_char_list = list(map(list, list(combinations(unique_characters, len(unique_characters) - 2))))
    char_set = list(map(list, list(permutations(unique_characters, 2))))
    maxi = 0
    for i in range(len(rem_char_list)):
        length = validate(removal_set(inp_string, list(rem_char_list[i])), char_set)
        if length > maxi:
            maxi = length
    print(maxi)
else:
    print(0)
