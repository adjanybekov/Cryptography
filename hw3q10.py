
def ps(x):
	return (x**.5%1==0)
		

def func2(x):
	if(ps(x)):
		print(x**.5)
	else:
		sqrtN= int(x**.5)
		for i in range(1,n):
			t= sqrtN+i
			
			s2 = (t**2-n)%n
			print(s2,t)
			if(ps(s2)):
				print(s2**.5)
				break



if "__main__"==__name__:
    n=int(input("n"))
    func2(n)
