#Read teth file and store all the lines in list
#Reverse the list
#Write back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines() #[apple, ball, ...]
    reversed(content) #[goad(MSD), fox, ...]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)