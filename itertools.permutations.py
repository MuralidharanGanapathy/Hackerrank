import itertools

input_string, length_permutator = input().split()

lister_of_perm = sorted(list(map(list,(list(itertools.permutations(input_string, int(length_permutator)))))))

soretd_order = []

for i in lister_of_perm:
    print("".join(i))
