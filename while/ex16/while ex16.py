
##Problem 16 «The maximum number of consecutive equal elements» (Hard)
##Statement
##Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where all the elements are equal to each other. 


occur1 = 1
occur2 = 1

first = int(input())
while first != 0:
    second = int(input())
    if second == first:
        occur1 = occur1 + 1
    else:
        if occur2 < occur1:
            occur2 = occur1
        occur1 = 1
    first = second
print (occur2)
