'''Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]'''


def convert_to_f(c):
    f = (c*9/5) + 32
    return f


def convert_to_c(f):
    c = (f - 32) * 5/9
    return int(c)


print(convert_to_f(60))
print(convert_to_c(140))
