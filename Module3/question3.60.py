#Write a Python program to calculate the area of a parallelogram

def parallelogram(b,h):
    if b or h>0:
        area=round(b*h)
        print(area)



print(parallelogram(10,5))