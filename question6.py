#Write python program that swap two number with temp variable and without temp variable.

num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))

print("Before swapping....")
print(f"A={num1} \n B={num2}")
temp=num1
num1=num2
num2=temp

print("After swapping......")
print(f"A={num1} \n B={num2}")
