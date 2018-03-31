
##Statement
##1- For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order. 


N= int(input())
x=1
y =''
while x**2 <= N:
    y = y +'  '+ str(x**2) 
    x=x+1
print (y )
