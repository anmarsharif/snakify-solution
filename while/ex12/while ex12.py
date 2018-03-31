
##Problem 12 «The second maximum» (Hard)
##Statement
##The sequence consists of distinct positive integer numbers and ends with the number 0. Determine the value of the second largest element in this sequence. It is guaranteed that the sequence has at least two elements. 



max_ = 0
sec = 0
in_ = int(input())

while in_ != 0:
    if in_ > max_:
        sec = max_
        max_ = in_
    else:
        if in_ > sec and in_ != max_:
            sec = in_
    in_ = int(input())
print (sec)
