
from fractions import gcd



def func(x,n):
	#sth here
	return (x**2+1)%n

def func2(x0,n):
	L=[x0]
	xi=x0
	cnt=0
	flag=False
	while True:
		cnt+=1
		xi=func(xi,n)
		print(cnt,xi)
		for i in range(cnt-1):
			if(gcd(xi-L[i],n) != 1 ):
				#print(xi)
				print("break point:",L[i],xi-L[i])
				flag=True
				break
		L.append(xi)
		if flag==True:
			print(gcd(xi-L[i],n))
			break
			
if "__main__"==__name__:
    x0=int(input("x0"))
    n=int(input("n"))
    func2(x0,n)
