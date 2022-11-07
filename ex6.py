''' Find the largest item from a given list'''

def largest(l):
    lrgs = 0
    for i in l:
        if i > lrgs:
            lrgs = i
    print(lrgs)

x = [4, 6, 8, 24, 12, 2]
largest(x)