# Differentiate between append () and extend () methods? 

#Append

#It adds an element at the end of the list.
#  The argument passed in the append function is added as a single element at end of the list .
#  the length of the list is increased by 1.

#extend

#This method appends each element of the iterable (tuple, string, or list) to the end of the list. 
# increases the length of the list by the number of elements of the iterable passed as an argument.

list1=[]

list1.append("a")
list1.append("b")
list1.append("c")


print(list1)



list2=['d','e','f']
list1.extend(list2)
print(list1)


    

