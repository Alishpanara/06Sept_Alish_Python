#Write a Python function that takes a list of words and returns the length of the longest one.


word=str(input("Enter a string:"))

s=word.split()
max=0



for i in s:
    if len(i)>max:
        max=len(i)
        temp=i
print(f"The length of longest word in the string:{temp} - {max}")
