#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

str="the movie is not that poor!"
a=str.find("not")
b=str.find("poor")

if b>a and a>0 and b>0:
    print(str.replace(str[a:b+4],"good"))
else:
    print(str)