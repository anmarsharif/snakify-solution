
#ex 04
#Equal numbers

a = int(input())
b = int(input())
c = int(input())
if a == b and a == c:
    print (3)
elif a == b or  a == c  or  b == c:
    print (2)
elif a != b or a != b  or b != c :
    print (0)
