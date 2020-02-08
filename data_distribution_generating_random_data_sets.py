# Data Distribution
# Generating Random Data Sets
# To create [big or not] data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.
# 
# Example 1:
# Create an array containing 250 random floats between 0 and 5:

import numpy
numpy.random.seed(1)
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)

# Example 2:
# Create an array containing 250.000 random floats between 0 and 5000:

import numpy
numpy.random.seed(1)
x = numpy.random.uniform(0.0, 5000, 250000)
print(x)

# The line 'numpy.random.seed(1)' enforces the reproducibility of the experiment.
# If that line is ommited, each time the numpy.random.uniform() [or numpy.random.randint()] method is called, different results will come up no matter what parameters are passaed to it.

# Example 2:
# Create an array containing 10 random INTEGERS between 0 and 50:

import numpy
numpy.random.seed(1)
x = numpy.random.randint(0, 50, 10)
print(x)
