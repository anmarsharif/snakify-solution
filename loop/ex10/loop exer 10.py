
# exer 10
#

n = int(input())
x =1
z =1
for i in range (1,n+1):
     x = x * i
#print(x)    
for i in range (n-1):
    y = int(input())
    z =z*y
#print(z)    
print (int(x/z))
