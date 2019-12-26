# Normal Data Distribution
# How to create an array where the values are concentrated around a given value.
# In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.
# Example:
# A typical normal data distribution:

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(1) # This is to enforce same "random" results for reproducibility matters.
mean_value = 5.0
standard_deviation = 1.0
number_of_values = 100000
number_of_bars = 100
x = numpy.random.normal(mean_value, standard_deviation, number_of_values)
plt.hist(x, number_of_bars)
plt.show()

# Histogram Explained
# We use the array from the numpy.random.normal() method, with 100000 values, specifying that the mean value is 5.0, and the standard deviation is 1.0.
# Meaning that the values should be consentrated around 5.0, and rarely further away than 1.0 from the mean.
# Than we use plt.hist(x, 100) to draw a histogram with 100 bars.
# And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
