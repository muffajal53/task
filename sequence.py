# This program calculates the iterative sequence 
# for the set of positive integers

# create the iterative sequence for the given number
def sequence(n):
	print(n)
	if (n==1):
		pass
	elif (n%2==0):
		n = int(n/2)
		return sequence(n)
	else:
		n = int((3*n)+1)
		return sequence(n)

# Main method from which we call the sequence method
if __name__ == '__main__':
	# get the number from console for calculation
	number = int(input("Please insert the number for iterative sequence :- "))
	# call sequence function
	sequence(number)
