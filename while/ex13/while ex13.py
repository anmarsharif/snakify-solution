
##Problem 13 «The number of elements equal to the maximum» (Hard)
##Statement
##A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are equal to its largest element. 


finished = True
j=0
i= 1
while finished is True:
    x = int(input())
    if x != 0:
        if x > i  :
            i = x
            j=1
        elif i==x :
             j=j+1
    else :
         finished = False
print (j)
