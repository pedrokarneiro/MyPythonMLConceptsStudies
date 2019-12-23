# Mean - The average value of a group of numbers
# Median - The mid point value of a group of numbers
# Mode - The the most common value in a group of numbers
# 
# [99,86,87,88,111,86,103,87,94,78,77,85,86]
# 
# 077
# 078
# 085
# 086086086
# 087087
# 088
# 094
# 099
# 103
# 111
#
##########
# Median #
##########
# The median value is the value in the middle of the vector, after you have sorted all the values:
# - Sort the vector before you can find the median.
# - If there are two numbers in the middle, sum them and then divide by two.
# - numby.median() does it all (sorts the vector and calculates the median).

import numpy
speed_array_1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]
speed_array_2 = [99,86,87,88,86,103,87,94,78,77,85,86]
my_median_1 = numpy.median(speed_array_1)
my_median_2 = numpy.median(speed_array_2)
print('my_median_1: ' + str(my_median_1))
print('my_median_2: ' + str(my_median_2))

# Results:
# C:\My Path>python median.py
# my_median_1: 87.0
# my_median_2: 86.5
