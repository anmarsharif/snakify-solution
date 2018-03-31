
##Problem  7 «The average of the sequence» (Medium)

##Statement
##Determine the average of all elements of the sequence ending with the number 0. 


finished = True
i=0
sum = 0
while finished is True:
    x = int(input())
    if x != 0:
        sum = sum + x
        i = i+1
    else :
         finished = False
print (sum/i)
