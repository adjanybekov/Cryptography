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



b = int(input("b:"))
m = int(input("m:"))
h = int(input("h:"))
bound = int(input("bound:"))

t = int(math.sqrt(m))
print(t)

Giant=[]
Baby=[]
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


for i in range(bound):
	gg= power(b,(i)*t,m)%m
	Giant.append(gg)

	bb=(h*power(b,(i),m))%m
	Baby.append(bb)
	#print(Giant,Baby)
	if any(j in Baby for j in Giant):           
	    inter=intersection(Giant,Baby)
	    print("interElem:",inter,"at b_i=",i)
	    bj=0
	    for  j in range(len(Giant)):
	        if Giant[j]==inter:
	             print("interElem:",inter,"at b_i=",i,"at g_i=",j)
	             break

	   
	    print(Giant,Baby)
	    break


