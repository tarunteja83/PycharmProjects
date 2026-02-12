#Clases : Classes are user defined blueprint or prototype
#Call will have methods, variables, instance variables, constructors etc.
#Self Keyword is mandatory for calling Variable names into method
#Instance and Class variables have whole different purpose
##one attached to Object and another not attached to object
#Constructor name should be __init__
#New keyword is not required unlike java when u create object

class Calculator:
    num = 100 #Class Variables

    #Default Constructor
    def __init__(self,a,b):
        self.firstNum = a
        self.secondNum = b
        print("I am called Automatically when object is created")


    def getclassdata(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNum + self.secondNum + Calculator.num


obj = Calculator(2,3)
obj.getclassdata()
print(obj.num)

obj1 = Calculator(4,5)
obj1.getclassdata()
print(obj1.num)

obj2 = Calculator(6,7)
obj2.summation()
print(obj2.summation())