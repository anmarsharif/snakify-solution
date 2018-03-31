
#ex07
#Total cost

A = int(input())
B = int(input())
N = int(input())
x  = (A+B/100) * N
a = int(x)
b = (x-int(x)) * 100
print (str(a) +  '  '  +  str(b))
