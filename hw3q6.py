# find all coprimes, and then test if by fermats theorem they give one if one gives one then stop

from math import gcd as bltin_gcd


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

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

n=int(input("n:"))
p=int(input("p:"))
B=[]
print(B)


def Fermat(a,n,p):
    return power(a, n-1,p) % n == 1

res=0

count=0
for i in range(2,n):
    if(coprime2(i,n)):
        B.append(i)
        if(Fermat(i,n,p)):
            print(i)
            count+=1
            #break
        if count==3:
            break
        #print(B) 

#print(B)

#print(res)


#find coprimes
