#Write a Python program to find the highest 3 values in a dictionary 

dict={'a':15,'b':53,'c':34,'d':29,'e':20}
d=list(dict.values())
d.sort()
d1=d[-3:]

for i in d1:
    for j in dict.keys():
        if dict[j]==i:
            print(f'{j}  :  {dict[j]}')




