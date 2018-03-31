
##Problem 8 «The maximum of the sequence» (Medium)
##Statement
##A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence. 


finished = True

i= 1
while finished is True:
    x = int(input())
    if x != 0:
        if x > i:
            i = x
    else :
         finished = False
print (i)
