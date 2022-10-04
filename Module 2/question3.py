#Write a Python program to get the Fibonacci series of given range.

num=int(input("Enter a range of number:"))
n1=0
n2=1
i=2
if num<=0:
    print("Invalid input")
elif num==1:
    print(f"fibonacci series:{n1}")
else:
    print("fibonacci series:")
    for i in range(num):
        print(n1,end=' ')
        n3=n1+n2
        n1=n2
        n2=n3
        