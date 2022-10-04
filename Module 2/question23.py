# Write a Python function to insert a string in the middle of a string.
i=str(input("Enter the string:"))
j=str(input("Enter a string to insert:"))
x=int(input("Enter the index:"))

print("new string:",i[:x]+j+i[x:])
