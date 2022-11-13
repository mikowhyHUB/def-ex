'''Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*'''


def pattern(high):
    for i in range(1, high+1):
        for j in range(1, i+1):
            print('*', end=' ')
        print('\n')
    for i in range(high-1, 0, -1):
        for j in range(i, 0, -1):
            print('*', end=' ')
        print('\n')


h = int(input('How high: '))
pattern(h)
