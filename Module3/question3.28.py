#Write a Python program to remove an empty tuple(s) from a list of tuples.

a=[(1,2,3),(),(),(7,8,9)]

i=0
while i<len(a):

    if len(a[i])==0:
        a.remove(a[i])
        i=i+1
print(a)