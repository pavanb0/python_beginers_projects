# Print Pascal's Triangle in Python

# input n
n = int(input("r"))
for i in range(n):
	for j in range(n-i+1):

		# for left spacing
		print(end=" ")

	for j in range(i+1):

		# nCr = n!/((n-r)!*r!)
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")

	# for new line
	print()
