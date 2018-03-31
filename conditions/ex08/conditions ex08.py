
#ex08
#Bishop moves
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2-x1 == y2-y1 or x1-x2 == y1-y2 or x2-x1 == y1-y2 or x1-x2 == y2-y1:
    print ('YES')
else :
    print ('NO')
