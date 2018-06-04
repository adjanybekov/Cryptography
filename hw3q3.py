a=int(input("a"))
n=int(input("n"))
#p=int(input("p"))


for i in range(n):
	if (i*i)%n==a:
		print(i)
		break
