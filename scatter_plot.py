# Scatter Plot
# A scatter plot is an X, Y diagram where each value in the data set is represented by a dot (x, y).
# It needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis.
# 
# Example 1 - Car Age X Car Speed

import matplotlib.pyplot as plt
age_of_car = [5,7,8,7,2,17,2,9,4,11,12,9,6]
speed_of_car = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(age_of_car, speed_of_car)
plt.show()

# Example 2 - Ramdomly Generated Data
# A scatter plot with 1000 dots:
# The first array will have the mean set to 5.0 with a standard deviation of 1.0.
# The second array will have the  mean set to 10.0 with a standard deviation of 2.0:

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(1) # This is to enforce same "random" results for reproducibility matters.
x_mean = 5.0
x_sd = 1.0
y_mean = 10.0
y_sd = 2.0
x = numpy.random.normal(x_mean, x_sd, 1000)
y = numpy.random.normal(y_mean, y_sd, 1000)
plt.scatter(x, y)
plt.show()
