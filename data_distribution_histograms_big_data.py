# Big Data Histogram Example
# Create an array with 100,000 random numbers, and display them using a histogram with 100 bars:

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(1)
x = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()
