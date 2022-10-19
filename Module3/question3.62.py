#Write a Python program to returns sum of all divisors of a number

def div(n):
    i=1
    sum=0
    l=[]
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
            l.append(i)
            print(i,end='')
    print('\nSum:',sum)

print(div(10))