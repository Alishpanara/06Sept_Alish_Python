#Write a Python program to append text to a file and display the text. 

from fileinput import close


x=open("question1.txt",'a')
x.write("\nI am a boy.")
x.close()

y=open("question1.txt",'r')
print(y.read())