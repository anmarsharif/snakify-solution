
##Problem 5 «The length of the sequence» (Easy)

##Statement
##Given a sequence of non-negative integers, where each number is written in a separate line. Determine the length of the sequence, where the sequence ends when the integer is equal to 0. Print the length of the sequence (not counting the integer 0). The numbers following the number 0 should be omitted. 


finished = True
i=0

while finished is True:
    x = int(input())
    if x != 0:
        i = i+1
        
    else :
         finished = False
print (i)
