# This program calculates the iterative sequence 
# for the set of positive integers

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

if __name__ == '__main__':
	# starting from here
	n = 13
	# call this function
	sequence(n)