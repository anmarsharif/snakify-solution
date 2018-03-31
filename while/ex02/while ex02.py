##2-Problem «Least divisor» (Easy)
##Statement
##Given an integer not less than 2. Print its smallest integer divisor greater than 1. 


    x = int(input())
a =2
finished = True
while finished is True:
     if x % a == 0:
         print(a)
         break 
     else:
         finished is False
         a = a+1
