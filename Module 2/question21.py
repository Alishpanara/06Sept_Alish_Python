#Write a Python function to reverses a string if its length is a multiple of 4.

str=input("Type a string:")
l=len(str)

if l%4==0:
    print(str[::-1])
else:
    print(str)