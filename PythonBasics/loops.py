#If loop

message = "Hello World"
a=4

if message == "WORLD":
    print("Condition matched")
    print("second message")
else:
    print("Condition not matched")

print("Not related to actual condition")

if a > 2:
    print("Condition matched")
    print("second message")
else:
    print("Condition not matched")

print("Not related to actual condition")

#For loop

obj = [2,3,5,7,8]

for i in obj:
    print(i)
    print(i*3)#multiply with list

#Sum of first five natural numbers 1+2+3+4+5 = 15
#Range (i,j) -> i to j-1
summation = 0
for j in range(1,6):
    summation = summation + j
    print(j)

print(summation)

print("*******************************************************")
for k in range(1,10,2):
    print(k)
for l in range(1,10,5):
    print(l)
    print("*************SKIPPED****************")

for m in range(10):
    print(m)

