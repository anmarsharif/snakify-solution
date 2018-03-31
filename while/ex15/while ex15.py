
##Problem 15 «The index of a Fibonacci number» (Hard)
##Statement
##The Fibonacci sequence is defined as follows: 
##ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.Given an integer aa
##determine its index among the Fibonacci numbers, that is, print the number n n such that ϕn=aϕn=a. If a is not a Fibonacci number, print -1.



x = int(input())
a,b = 0,1
fibon=[1]
index =1
while b<=x:
    a,b = b,a+b
    fibon.append(b)
    index =index+1
    
if x not in fibon:
    print(-1)
else:
    print(fibon.index(x)+1)
