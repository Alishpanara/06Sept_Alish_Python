#Write a Python function to calculate the factorial of a number (a nonnegative integer)

from math import factorial


def fact(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
print(fact(3))



