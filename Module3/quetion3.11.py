#Write a Python function that takes a list and returns a new list with unique elements of the first list.

unique_list=[1,2,2,3,3,3,3,4,4]
num=[]
for a in unique_list:
    if a not in num:
        num.append(a)
        print(num)
            