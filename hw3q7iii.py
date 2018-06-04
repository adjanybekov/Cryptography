import math

def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p 
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res



n = int(input("n:"))
cnt=0
t=3*7*829
s=5

for i in range(2,n):
    if (power(i,t,n)==1):
        print(i)
        cnt+=1
    if (cnt==9):
        break
