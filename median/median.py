a = 1,2,3,4,5,6,7,8,9,10
b = 1,2,3,4,5,6,7,8,9,10, 11
#input for the calculations


def median(x):
#defines a function that accepts one vector as parameter

	x = sorted(x)
	#sort the values in increasing order
	
	n = len(x)
	#defines the value of n
	
	if n % 2 == 0:
		#if n is even, the median is calculated as the arithmetic mean of the two central values "x[n/2]" and "x[n/2 + 1]" 
		median = (x[n/2] + x[n/2 + 1]) / float(2)
	else:
		#if n is odd, the median is the central value "x[n/2]"
		median = x[n/2]
	
	return median


print median(a)
print median(b)