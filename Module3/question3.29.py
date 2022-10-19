#Write a Python program to remove an empty tuple(s) from a list of tuples. 

list=[('Alish',1),('Panara',2),('Nareshbhai',3)]
print("original list is:",(list))

res=[[i for i,j in list],[j for i,j in list]]
print(res)