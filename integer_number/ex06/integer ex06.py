
#ex06
#Car route
N = int(input())
M = int(input())
if M%N != 0:
    Days = (M // N) + 1 
    print(Days)
else:
    print (M/N)
