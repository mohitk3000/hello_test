def factorial(n):
	if n==0:
		return n
	else:
		return n * factorial(n-1)
		
		
n=5
result=factorial(n)
print(result)
