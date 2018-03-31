
#ex03
#Sum of digits

x = int(input())
sum = int(x//100) + (x%100)//10 + x%10
print(sum)
