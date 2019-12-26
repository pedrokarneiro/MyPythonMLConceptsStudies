# Histogram
# To visualize the data set we can draw a histogram with the data we collected.
# We will use the Python module Matplotlib to draw a histogram.
# 
# IMPORTANT:
# Matplotlib and its dependencies are available as wheel packages for macOS, Windows and Linux distributions.
# Run these lines under Windows CMD or the equivalent command line interface of your OS:

python -m pip install -U pip
python -m pip install -U matplotlib

# Example 1
# Draw a histogram with random float numbers:

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(1)
x = numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()

# Example 2
# Draw a histogram with random INTEGER numbers:
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(1)
x = numpy.random.randint(0, 5, 250)
plt.hist(x, 5)
plt.show()

# For test purposes, these will work better in your local machine.
# Repl.it seem not to handle matplotlib yet.

# The line 'numpy.random.seed(1)' enforces the reproducibility of the experiment.
# If that line is ommited, each time the numpy.random.uniform() [or numpy.random.randint()] method is called, different results will come up no matter what parameters are passaed to it.
