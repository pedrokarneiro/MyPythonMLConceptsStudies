# STANDARD DEVIATION AND VARIANCE
# How spread are the numbers in the vector?
# 
# Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.
# 
# Example of low standard deviation:
# 
# speed = [86,87,88,86,87,85,86]
# The standard deviation is:
# 0.9
# Meaning that most of the values are within the range of 0.9 from the mean value, which is 86.4.
# Let us do the same with a selection of numbers with a wider range:
# 
# Demonstrating the calculation of the Standard Deviation "by hand",
# (considering the formula found in https://standarddeviationformula.com/):
# Results:
# speed: [86, 87, 88, 86, 87, 85, 86]
# xbar: 86.42857142857143
# n: 7
# variance: 0.8163265306122449
# sd: 0.9035079029052513
#
# Considering a handmade histogram:
# 
# 85
# 868686
# 8787
# 88
# 
# Note that the histogram shows that most of the numbers are close to the mean (average or xbar) value, confirming the low value for sd.
# 
# The code for the demonstration of the calculation of the Standard Deviation "by hand":

import numpy
import math
speed = [86,87,88,86,87,85,86]
print('speed: ' + str(speed))
xbar = numpy.mean(speed)
print('xbar: ' + str(xbar))
n = len(speed)
print('n: ' + str(n))
variance = (math.pow(86-xbar, 2) + math.pow(87-xbar, 2) + math.pow(88-xbar, 2) + math.pow(86-xbar, 2) + math.pow(87-xbar, 2) + math.pow(85-xbar, 2) + math.pow(86-xbar, 2))/n
print('variance: ' + str(variance))
sd = math.sqrt(variance)
print('sd: ' + str(sd))

# Example of high standard deviation:
# speed = [32,111,138,28,59,77,97]
# The standard deviation is:
# 37.85
# Meaning that most of the values are within the range of 37.85 from the mean value, which is 77.4.
# As you can see, a higher standard deviation indicates that the values are spread out over a wider range.
# 
# Demonstrating the calculation of the Standard Deviation "by hand",
# (considering the formula found in https://standarddeviationformula.com/):
# Results:
# speed: [32, 111, 138, 28, 59, 77, 97]
# xbar: 77.42857142857143
# n: 7
# variance: 1432.2448979591834
# sd: 37.84501153334721
#
# Considering (this time "trying") to build a handmade histogram:
# 
# 028
# 032
# 059
# 077
# 097
# 111
# 138
# 
# No repetition occurring in the series makes it difficult to look like a histogram.
# Also note that, the values are very sparse and one far from the other.
# 
# You can percieve that the histogram shows that most of the numbers are far from the mean (average or xbar) value, confirming the high value for sd.
# 
# The code for the demonstration of the calculation of the Standard Deviation "by hand":
# (Only the speed vector - and its elements in the calculation of variance - has changed)

import numpy
import math
speed = [32,111,138,28,59,77,97]
print('speed: ' + str(speed))
xbar = numpy.mean(speed)
print('xbar: ' + str(xbar))
n = len(speed)
print('n: ' + str(n))
variance = (math.pow(32-xbar, 2) + math.pow(111-xbar, 2) + math.pow(138-xbar, 2) + math.pow(28-xbar, 2) + math.pow(59-xbar, 2) + math.pow(77-xbar, 2) + math.pow(97-xbar, 2))/n
print('variance: ' + str(variance))
sd = math.sqrt(variance)
print('sd: ' + str(sd))

# 
# But the Standard Deviation may be more straightforward in Python.
# The NumPy module has a method to calculate the standard deviation:
# Example:
# Use the NumPy std() method to find the standard deviation:

import numpy
print('Using the NumPy std() method to find the standard deviation:')

print('Low Standard Deviation example:')
speed_1 = [86,87,88,86,87,85,86]
print('speed_1: ' + str(speed_1))
sd_1 = numpy.std(speed_1)
print('sd_1: ' + str(sd_1))

print('High Standard Deviation example:')
speed_2 = [32,111,138,28,59,77,97]
print('speed_2: ' + str(speed_2))
sd_2 = numpy.std(speed_2)
print('sd_2: ' + str(sd_2))

# Results:
# Using the NumPy std() method to find the standard deviation:
# Low Standard Deviation example:
# speed_1: [86, 87, 88, 86, 87, 85, 86]sd_1: 0.9035079029052513
# High Standard Deviation example:
# speed_2: [32, 111, 138, 28, 59, 77, 97]
# sd_2: 37.84501153334721
# 
# Variance is another number that indicates how spread out the values are.
# In fact, note that if you take the square root of the variance, you get the standard variation.
# Or the other way around, if you multiply the standard deviation by itself, you get the variance.
# You can get more detailed explanation at https://www.w3schools.com/python/python_ml_standard_deviation.asp.
# 
# Just like for Standard Deviation, Python has a simplified way for calculating the Variance.
# The NumPy var() method finds the variance.
# 
# Example:

import numpy
speed = [32,111,138,28,59,77,97]
print('speed: ' + str(speed))
variance = numpy.var(speed)
print('variance: ' + str(variance))

# Results:
# speed: [32, 111, 138, 28, 59, 77, 97]
# variance: 1432.2448979591834
