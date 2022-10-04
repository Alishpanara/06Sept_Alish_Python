#Write a Python function to get the largest number, smallest num and sum of all from a list. 

list=[]


n=int(input("Enter total number of element:"))
for i in range(n):
    value=int(input("Enter the value:"))
    list.append(value)
    #print(list)
print("Smallest number in list:",min(list))
print("Largest number in list:",max(list))
print("Sum of all element in list:",sum(list))

    

    
