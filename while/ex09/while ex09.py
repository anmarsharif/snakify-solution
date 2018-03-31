

##Problem  9 «The index of the maximum of a sequence» (Hard)
##Statement
##A sequence consists of integer numbers and ends with the number 0. Determine the index of the largest element of the sequence. If the highest element is not unique, print the index of the first of them. 


max = 0
index = 0
index1 =0
element = -1
while element != 0:
    element = int(input())
    index= index+1
    if element > max:
        max = element
        index1 = index
        
print(index1)
