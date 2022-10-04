#Write a Python program to remove duplicates from a list.
list=[]
n=int(input("Enter number of element in list:"))
for i in range(n):
    el=int(input("Enter element:"))
    if el not in list:
    
     list.append(el)

     print(list)
    
    




