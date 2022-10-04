# Write a Python program to count the number of strings
#  where the string length is 2 or more and the first and last character are same from a given list of strings. 


list=[]

n=int(input("Enter total number of element:"))
for i in range(n):
    el=str(input("Enter element:"))
    if  el[0]==el[-1] and len(el)>=2:
     list.append(el)

    print(list)

