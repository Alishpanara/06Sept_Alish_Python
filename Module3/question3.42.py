#Write a Python program to print all unique values in a dictionary. 

dict={'a':11,'b':12,'c':13,'d':13,'e':14,'f':12}

d=list(dict.values())

for i in range(len(d)):
    if d[i] not in d[i+1:]:
        print(d[i])
    else:
        pass