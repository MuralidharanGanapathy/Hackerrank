def minion_game(string):
    vowels = "AEIOU"
    stuart = 0
    kevin = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if stuart > kevin:
        print("Stuart ",end="")
        print(stuart)
    elif kevin > stuart:
        print("Kevin ",end="")
        print(kevin)
    else:
        print("Draw")




