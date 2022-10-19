#Write a Python program to read a random line from a file.

import random
def random_lines(filename):
    lines=open(filename).read().splitlines()
    return random.choice(lines)

print(random_lines("new.txt"))