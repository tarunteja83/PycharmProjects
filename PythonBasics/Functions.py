#In Python or any programing language, Function is a group of related statements that perform similar task
#def : is an identifier which mandatory to use to create a Function
#Function Declaration


def GreetMsg(name):
    print("Good Morning "+name)

def AddIntegers(a,b):
    print(a+b)

def AddNum(a,b):
    return a+b#with return keyword

#Function Call
GreetMsg("Tarun")
AddIntegers(2,4.5)
print(AddNum(3,5))
