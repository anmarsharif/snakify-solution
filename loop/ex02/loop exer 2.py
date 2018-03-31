
#exer 2
#Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.

A = int(input())
B = int(input())
if A<B:
   for x in range (A,B+1):
      print(x)
elif A>=B :
    for x in range(A,B-1,-1):
        print(x)
