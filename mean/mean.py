a = 1,2,3,4,5,6,7,8,9,10, 11
#input for the calculations

def mean(x):
#defines a function that accepts one parameter
	
	sum = 0
	for i in x:
		sum = sum + i  
	#calculates the sum of the elements from x 
	
	lenght = len(x)
	
	mean = float(sum/lenght)
	#the mean is calculated as the sum of the values divided by the number of values
	
	return mean

print mean(a)