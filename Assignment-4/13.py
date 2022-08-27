def minion_game(string):
    # your code goes here

    vowels = 'AEIOU'

    kevin = 0
    stu = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += (len(string)-i)
        else:
            stu += (len(string)-i)

    if kevin > stu:
        print ("Kevin", kevin)
    elif kevin < stu:
        print ("Stuart", stu)
    else:
        print ("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)