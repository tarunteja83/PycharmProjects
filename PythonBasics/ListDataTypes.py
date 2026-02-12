#List is a data type that allow miultiple values that can be of different data types
values = [1, 2, "Ramu", 3.4, 5]

print(values[0]) #value should be 1
print(values[2]) #value should be "Ramu"
print(values[3]) #value should be 3.4
print(values[-1]) #value should be 5 to get last
print(values[1:4]) #value should be 2,"Ramu,3.4 to get collection of list

print(type(values))

#How to insert new value to existing list
values.insert(3, "Raja")
print(values)

print(values[1:4]) #value change post list update should be 2,"Ramu", "Raja"
print(values)

values.append("Rest") #To add value to list with value at last
print(values)

values[2] = "Ramoji" #To update value in existing list
print(values)

del values[0]#To delete values
print(values)

#Tupple data type
#Tupple - Same as list data type but immutable(Not allowed for modification)
val = (1,2,"Rajesh", 4.5)
print(val)

#val[2] = "RAJU"
print(val)

#Dictionary

dict = {"a":"Hi there", 4 : "You know it is not applicable", "c" : "RIP World", 5 : 1.34}

print(dict)
print(dict[4])
print(dict[5])
print(dict["a"])
print(dict["c"])

dicti = {}

dicti["Name"] = "Raja"
dicti["Age"] = 25
dicti["Height"] = 100

print(dicti)
