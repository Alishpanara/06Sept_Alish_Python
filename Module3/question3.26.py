#Write a Python program to replace last value of tuples in a list.
list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for i in range(len(list1)):
    upd_list=list(list1[i])
    upd_list[-1] = 100
    list1[i]=tuple(upd_list)

    print(list1)
















