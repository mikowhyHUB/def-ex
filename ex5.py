'''Generate a Python list of all the even numbers between 4 to 30'''

def even_nums():
    l=[]
    l = [i for i in range(4,31,2)]
    return l

print(even_nums())
