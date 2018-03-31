
##Problem 6  «The sum of the sequence» (Medium)

##Statement
##Determine the sum of all elements in the sequence, ending with the number 0. 




finished = True

sum = 0
while finished is True:
    x = int(input())
    if x != 0:
        sum = sum + x
    else :
         finished = False
print (sum)
