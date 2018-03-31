
#ex10
#Knight move

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2-x1 == 2*(y2-y1) or x2-x1 == 2*(y1-y2) or x1-x2 == 2*(y2-y1) or x1-x2 == 2*(y1-y2) or y2-y1 == 2*(x2-x1) or y2-y1 == 2*(x1-x2) or y1-y2 == 2*(x2-x1) or y1-y2 == 2*(x1-x2): 
    print ('YES')
else:
    print ('NO')
