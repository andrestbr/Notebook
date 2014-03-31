numbers = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
weights = 5, 4, 10, 12, 20, 18, 18, 12, 15, 2, 4
#input for the calculations

def weighted_mean(values, weights):
	table = []
	#creates an empty table to store the pairs of values
		
	if len(values) == len(weights):
	#checks if there is a weight for every value
		
		i = 0
		while i < len(values):
			table.append([values[i], weights[i]])
			i += 1
			#assigns a weight to a value
					
		sum = 0 
		# initializes the variable sum to zero. It stores the sum of the values multiplied with their respective weights		
		for i in table:
			sum += i[0]*i[1]
			#table has two elements in each object. This multiplies them with each other 
			#and saves the results in the variable sum
					
		freq = 0
		# initializes the variable freq_sum to zero. It stores the sum of the frequencies
		
		for i in weights:
			freq += i
			#calculation for the sum of the frequencies
		 	
		weighted_mean = float(sum)/float(freq)
		#weighted mean = sum of all values * weight / Sum of all weights
		
		return(weighted_mean)
		
	else:
		return("values and weights don't match")
		
print weighted_mean(numbers, weights)
