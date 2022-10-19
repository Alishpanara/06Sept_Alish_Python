#Write a Python program to calculate surface volume and area of a cylinder 

from math import pi

def cylinder(r,h):
    if r or h>0:
        area=round((2*pi*r*h)+(2*pi*r**2))
        volume=round(pi*r**2*h)

        print(area)
        print(volume)

print(cylinder(5,5))
        