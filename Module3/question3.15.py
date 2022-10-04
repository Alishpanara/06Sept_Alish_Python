#Write a Python program to get unique values from a list 

list=[]
n=int(input("Enter number of element in list:"))
for i in range(n):
    el=int(input("Enter element:"))
    if el not in list:
    
     list.append(el)

     print("unique list:",list)
    