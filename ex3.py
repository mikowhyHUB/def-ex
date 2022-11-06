'''Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it'''

def two_par(a, b):
    def calculate(a, b):
        return a + b
    
    add = calculate(a,b)
    return add + 5

print(two_par(5,10))