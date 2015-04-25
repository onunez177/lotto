__author__ = 'Rob Wilson'

# Program to generate numbers and test them

import random

def generate(lines):
    for x in range(0, lines):
        newLine = []
        for i in range(0, 6):
            r = random.randint(1,49)
            newLine.append(r)
            newLine.sort()
        print (newLine)
    print('\n1 - Return to main menu')
    print('2 - Quit')
    choice = int(raw_input('Make a choice [1, 2]'))
    if choice == 1:
        main()
    else:
        exit(0)

def test(nums):
    userNums = map(int,nums.split(' '))
    userNums.sort()
    count = 0
    num3 = 0
    num4 = 0
    num5 = 0
    testNums = []

    while userNums != testNums:
        numMatch = 0
        count += 1
        testNums = []
        while len(testNums) != 6:
            r = random.randint(1,49)
            if r not in testNums:
                testNums.append(r)
                if r in userNums:
                    numMatch += 1
                    if numMatch == 3:
                        num3 += 1
                    if numMatch == 4:
                        num4 += 1
                    if numMatch == 5:
                        num5 += 1
        testNums.sort()
        if count % 100000 == 0:
            print('Upto '+str(count)+ ' checked...')
    print('\n[!] Numbers match after '+str(count)+' draws!')
    print('\nStatistics:')
    print('3 number matches: '+str(num3))
    print('4 number matches: '+str(num4))
    print('5 number matches: '+str(num5))
    print('\n 1 - Return to main menu')
    print('2 - Quit')
    choice = int(raw_input('Make a choice [1, 2]'))
    if choice == 1:
        main()
    else:
        exit(0)

def main():
    print('\n1 - Generate lotto numbers')
    print('2 - Test your numbers\n')
    choice = int(raw_input('Make a choice [1, 2]'))

    if choice == 1:
        lines = int(raw_input('\nHow many line to generate?'))
        generate(lines)
    elif choice == 2:
        nums = raw_input('\nPlease enter 6 numbers to test separated with a space ')
        test(nums)
    else:
        print('Enter 1 or 2')
        main()

if __name__ == '__main__':
    main()






