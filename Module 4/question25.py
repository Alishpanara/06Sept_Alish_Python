#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python? 

class Fadher:
    car=0
    bal=0

    def getdata(self):
     self.car=input("Enter car detais:")
     self.bal=input("Enter bank ")

class Son(Fadher):
    def printdata(self):
        print("Car:",self.car)
        print("Bank Balance:",self.bal)

n=Son()
n.getdata()
n.printdata()


        