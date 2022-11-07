#Write a Python program to copy the contents of a file to another file.

x=open("question4.txt",'r')
y=open("question12.txt",'w')

for i in x:
   y.write(i)

   