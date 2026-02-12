# file = open('test.txt')
# file1 = open('test.txt')
file2 = open('test.txt')
#
# #Read all contents in file
# print(file.read())#To read & print what is read
# print("**********************************")
# #Read n number of character by passing parameter
# print(file1.read(10))
# print("**********************************")
#Read one single line at a time readLine()
print(file2.readline())
print(file2.readline())
#

# file1.close()
# file2.close()

#Print line by line using readline method(**IVQ**)

# line = file.readline()
# #
# while line != '':
#     print(line)
#     line=file.readline()

# line = file.readlines()
# print(line)

# for line in file.readlines():
#     print(line)

file2.close()#To close file which is opened