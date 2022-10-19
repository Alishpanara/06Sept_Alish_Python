#Write a Python script to sort (ascending and descending) a dictionary by value.

from audioop import reverse


dic={"A":1,"B":2,"D":4,"C":3,"E":5}

a=dic.values()
print(a)


print("ascending order:",sorted(a))
print("descending order:",sorted(a,reverse=True))











