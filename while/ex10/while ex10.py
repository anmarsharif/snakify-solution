
##Problem 10 «The number of even elements of the sequence» (Medium)
##Statement
##Determine the number of even elements in the sequence ending with the number 0. 


a = True
i = 0
while a is True:
     x = int(input())
     if x != 0:
        if x%2 == 0:
         i = i+1
     else:
        a =False
print(i)
