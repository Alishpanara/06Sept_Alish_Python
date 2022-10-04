#Write a Python program to select an item randomly from a list.

'''    import random
    list1=[1,'a','p',4,'t',5,6,'i',7]
    print("Random element is :",random.choice(list1))'''


'''
    import random


    list1=[1,'a','p',4,'t',5,6,'i',7]
    print ( "Random element is:",random.randint(0,len(list1)-1)) '''


'''    import random
    list1=[1,'a','p',4,'t',5,6,'i',7]
    print("Random element is :",random.randrange(0,len(list1)-1,))
'''


'''    import secrets
    list1 = [1,'a','p',4,'t',5,6,'i',7]
    print("Random element is :",secrets.choice(list1))'''


import random 
list1 = [1,'a','p',4,'t',5,6,'i',7]
print("Random element are :",random.sample(list1, 3))














