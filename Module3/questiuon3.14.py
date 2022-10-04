#Write a Python program to find the second smallest number in a list.

from re import L


list=[]

n=int(input("Enter number of element:"))
for i in range(n):
    el=int(input("Enter element:"))
    
    list.append(el)

small=list[0]
for i in range(n):
    if small>list[i]:
        list[i]=small
secondSmall=list[0]
for i in range(n):
    if secondSmall>list[i]:
        if list[i]!=small:
            list[i]=secondSmall
print("secondSmall number is:",secondSmall)





    
