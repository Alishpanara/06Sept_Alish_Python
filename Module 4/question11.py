#Write a Python program to write a list to a file.

x=open("question4.txt",'a')

list=['My Fadher name is Nareshbhai.','My Brother name is Yash.','My Mother name is Bhavanaben.']
x.write('\n')
for i in list:
    x.write(f'{i}\n')
    

    


    