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


x=int(input("x"))
n=int(input("n"))
p=int(input("p"))

for i in range(p):
	if(power(i,n,p)==1):
		#find roots
		#print(i)
		#check if it is primitive
		flag=True
		for j in range(1,n-1):
			if power(i,j,p)==1:
				print(i,"is not primitive")
				flag=False
				break
		if flag:
			print(i,"is primitive")
