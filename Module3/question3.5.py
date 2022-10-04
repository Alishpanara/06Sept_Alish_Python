#How will you compare two lists? 

"""list1=[1,2,3,4,5]
list2=[1,2,3,4,5]

print(list1==list2)"""

"""list1=[3,5,2,1,4]
list2=[1,2,4,3,5]
list1.sort()
list2.sort()
print(list1==list2)"""

list1=[3,6,8,4,5]
list2=[2,5,6,7,9]

result=set(list1)&set(list2)
print(list(result))

result1=set(list1)-set(list2)
print(list(result1))