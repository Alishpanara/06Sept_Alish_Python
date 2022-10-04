#Write a Python function that takes two lists and returns true if they have at least one common member.


a=[]
b=[]
n1=int(input("Enter number of element in a:"))
n2=int(input("Enter number of element in b:"))


for i in range (n1):
    for j in range(n2) :
        el1=int(input("Enter el1:"))
        a.append(el1)
        print(a)
    el2=int(input("Enter el2:"))
    b.append(el2)
    print(b)
    if el2 in a:
        print("true")
    else:
        print("false")

    



