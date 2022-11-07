'''Define a function in python that accepts 3 values and returns the maximum of three numbers.'''

def max_value(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


v1 = input('Enter a number: ')
v2 = input('Enter a number: ')
v3 = input('Enter a number: ')

print(max_value(v1,v2,v3), 'is the maximum among all')