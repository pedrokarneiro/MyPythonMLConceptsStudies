# Machine Learning - Percentiles
# What are Percentiles?
# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
# Example: Let's say we have an array of the ages of all the people that lives in a street.
# ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
# What is the 75. percentile? The answer is 43, meaning that 75% of the people are 43 or younger.
#
# How to calculate the Percentile of a series by hand:
# (Explanation from https://www.shorttutorials.com/how-to-calculate-percentile/index.html)
# 
# Formula:
# To calculate the kth percentile (where k is any number between zero and one hundred), do the following steps:
# 
# 1. Arrange the values in the data set in ascending order.
# 2. Find the "k"th percentage for the data set. That is, for a data set of 25 numbers, 100% will be 25 and 50% will be 12.5. Similary find the Kth percentage of the data set by multiplying the "k" percent by the total number of values, n.
# 3. If the number obtained above is not a whole number, round it up to the nearest whole number. This number is called the index and is the number corresponding to the kth percentage.
# 4. Count the values in the data set from left to right until you reach the index number.
# 5. Now, the "Kth" percentile is the value corresponding to this index number.
# 
# Hence, percentile calculation can be done using the below formula,
# Kth Percentile = Value corresponding to the Index Number I
# Index Number (I) = K% x N
# Where,
# N is the total number of values in data set.
# 
# Kth Percentile = Value corresponding to the Index number (I)
# Index number (I) = K% * N
# Where N = Total number of values in the dataset.
# 
# Step 1: Assigning Values:
# Let us consider a data set with 25 values as given below. We are required to find the 90th percentile of the data set.
# Data Set = 3, 67, 34, 89, 56, 23, 90, 67, 104, 29, 38, 46, 65, 62, 87, 86, 49, 50, 58, 72, 83, 16, 19, 48, 88
# N = 25
# 
# Step 2: Ordering Data Set
# Arrange the numbers in the data set in ascending order.
# Data Set (Ordered) = 3, 16, 19, 23, 29, 34, 38, 46, 48, 49, 50, 56, 58, 62, 65, 67, 67, 72, 83, 86, 87, 88, 89, 90, 104
# 
# Step 3: Finding Index Number:
# Index Number (I) = 90% x 25
# I = 0.90 x 25
# I = 22.5
# I = 23 (Rounded Off)
# 
# Step 4: Percentile Calculation
# 90th Percentile = Value corresponding to the Index Number (23)
# P90 = Value at 23rd place in data set
# P90 = 89
# 
# Hence, the 90th percentile of the given data set is 89, which is the value at the 90th percentage of the data set, which is the value at the index number 23 out of the total 25 numbers.
# 
# The same example using the NumPy module:

import numpy
import math
ds = [3, 67, 34, 89, 56, 23, 90, 67, 104, 29, 38, 46, 65, 62, 87, 86, 49, 50, 58, 72, 83, 16, 19, 48, 88]
print('ds: ' + ds)
p90 = numpy.percentile(ds, 90)
print('p90.............: ' + str(p90))
print('\"Rounded up\" p90: ' + str(math.ceil(p90)))

# Results:
# ds: [3, 67, 34, 89, 56, 23, 90, 67, 104, 29, 38, 46, 65, 62, 87, 86, 49, 50, 58, 72, 83, 16,19, 48, 88]
# p90.............: 88.6
# "Rounded up" p90: 89

# I don't know the reason yet, but NumPy seems to do the calculation a bit differently from simply counting the positions.

# Calculating the Percentile of a series by hand (not using NumPy percentile() function):
# (According to https://www.shorttutorials.com/how-to-calculate-percentile/index.html)

import math
# dataset
ds = [3, 67, 34, 89, 56, 23, 90, 67, 104, 29, 38, 46, 65, 62, 87, 86, 49, 50, 58, 72, 83, 16, 19, 48, 88]
print('ds: ' + str(ds))
# dataset length
n = len(ds)
print('n: ' + str(n))
# Ordering the dataset
ds.sort()
print('Ordered ds: ' + str(ds))
# Calculating the index where the 90% sits.
i = 0.9 * n
print('i........: ' + str(i))
# Rounding up i
i = math.ceil(i)
print('Rounded i: ' + str(i))
# Calculating the 90th percentile.
p90 = ds[i]
print('p90: ' + str(p90))
print('Oops! Python is zero-based for vectors while Statistics is not!!!')
p90 = ds[i-1]
print('p90: ' + str(p90))

# Results:
# ds: [3, 67, 34, 89, 56, 23, 90, 67, 104, 29, 38, 46, 65, 62, 87, 86, 49, 50, 58, 72, 83, 16,19, 48, 88]
# n: 25
# Ordered ds: [3, 16, 19, 23, 29, 34, 38, 46, 48, 49, 50, 56, 58, 62, 65, 67, 67, 72, 83, 86, 87, 88, 89, 90, 104]
# i........: 22.5
# Rounded i: 23
# p90: 90
# Oops! Python is zero-based for vectors while Statistics is not!!!
# p90: 89