#Write a Python program to calculate the area of a trapezoid

def areaOfTrapezoid(a,b,h):
    if a >0 or b>0 or h>0:
       area=round((a+b)/2*h)
    print(area)

print(areaOfTrapezoid(5,5,5))
    