#Write a Python function that checks whether a passed string is palindrome or not

def str(x):
    if x==x[::-1]:
        print("String is palindrome...")
    else:
        print("String is not palindrome...")

str("aba")