number_of_requests <- c(0, 1,2,3,4,5,6,7,8,9,10)
number_of_days <- c(5, 4, 10, 12, 20, 18, 18, 12, 15, 2, 4)
#input for the calculations


w_mean <- weighted.mean(number_of_requests, number_of_days) 
# stores the weighted mean in a variable

print(w_mean) 

