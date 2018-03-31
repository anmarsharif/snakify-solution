
##Problem 14 «Fibonacci numbers» (Hard)
##Statement
##The Fibonacci sequence is defined as follows: 
##ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
##Given a non-negative integer nn, print the nth Fibonacci number ϕnϕn
. ##This problem can also be solved with a for loop. 


x = int(input())
fibonacci =[1,1]
while x >0:

    for i in range(2,x+1):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    print(fibonacci[-2])
    break
else:
    print(0)
