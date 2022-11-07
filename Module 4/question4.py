#Write a Python program to read first n lines of a file.

x=open("question4.txt",'a')
x.write('''I am Alish.
I am from Jamnagar.
I am Electrical Engineer.''')


x.close()
x=open("question4.txt",'r')
print(x.readlines()[:5])


