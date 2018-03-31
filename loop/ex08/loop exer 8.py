
#exer 8
#Adding factorials

sum = 0
x = 1
n = int(input())
for i in range (1,n+1):
    x = x * i
    sum = sum + x
print(sum)
