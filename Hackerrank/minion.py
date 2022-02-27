def minion_game(string):
    vowels = 'AEIOU'
    
    stuart = 0
    kevin = 0
    
    for x in range(len(string)):
        if string[x] in vowels:
            kevin += len(string) - x
        else:
            stuart += len(string) - x
    
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print('Draw')
