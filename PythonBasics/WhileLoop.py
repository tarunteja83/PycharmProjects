fam = 10
jam = 5
bam = 10

while fam>1:
    if fam != 3:
        print(fam)
    fam = fam - 1 #If there is no deduction this will run as infinite loop

print("**************While Loop execution is completed**************")

while jam>1:
    if jam == 3:
        break
    print(jam)
    jam = jam - 1 #If there is no deduction this will run as infinite loop

print("**************While - Break Loop execution is completed**************")

while bam>1:
    if bam == 9:
        bam = bam - 1#If the value is not deducted it will run as infinite loop
        continue
    if bam == 3:
        break
    print(bam)
    bam = bam - 1 #If there is no deduction this will run as infinite loop

print("**************While - Continue Loop execution is completed**************")