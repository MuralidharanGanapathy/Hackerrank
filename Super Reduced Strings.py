stack = []
def top(j):
    return j[len(j)-1]

def super_reduced_string(l):
    for i in range(len(l)):
        if len(stack) <= 0:
            stack.append(l[i])
        elif top(stack)==l[i]:
            stack.pop()
        elif len(stack)>0 and top(stack)!=l[i]:
            stack.append(l[i])
    return stack        
string_list = list(input())
#set_length = len(list(set(string_list)))
super_string = super_reduced_string(string_list)
if(len(super_string) == 0):
    print("Empty String")
else:
    print(''.join(super_string))
