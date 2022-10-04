#Write a Python program to check whether a list contains a sub list 

list1=[]
list2=[]
n1=int(input("Enter number of element in list1:"))
n2=int(input("Enter number of element in list2:"))

for i in range(n1):
    print("Enter element in list1:")
    a=int(input())
    list1.append(a)



for j in range (n2):
    print("Enter element in list2:")
    b=int(input())
    list2.append(b)

if j in list1:
    print("list2 is part of list1")
else:
    print("list2 is not part of list1")



        
