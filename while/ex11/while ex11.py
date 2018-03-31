
##Problem 11 «The number of elements that are greater than the previous one» (Hard)
##Statement
##A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are greater than their neighbours above. 

first = int(input())
count = 0

while first != 0:
    second = int(input())
    if second > first:
        count = count + 1
    first = second
print (count)
