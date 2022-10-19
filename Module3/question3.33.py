#Write a Python script to concatenate following dictionaries to create a new one

dic1={"Name":"Alish"}
dic2={"Id":101}
dic3={"Sub":"Python"}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)