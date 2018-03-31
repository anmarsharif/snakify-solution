
#ex09
#Clock face - 1

H =int(input())
M = int(input())
S = int(input())
print (float(360/12*H) + float(360/(60*12)*M)+float(360/(60*60*12)*S))
