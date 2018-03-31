
##3-Problem «The power of two» (Medium)
##Statement

##For a given integer N, find the greatest integer x where 
##2x 2x is less than or equal to N. Print the exponent value and the result of
##the expression 2x
##Don't use the operation **.



N = int(input())
x = 0
finished = True
while finished is True:
    if 2**(x+1) > N :
        finished = False
    else:
        x = x+1
print(x, 2**x)
