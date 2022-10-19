# Write a Python program to convert degree to radian 



from math import pi


def degtorad(d):
    rad=d*pi/180
    print(f'{d} Degrees={rad} Radians')
print(degtorad(5))