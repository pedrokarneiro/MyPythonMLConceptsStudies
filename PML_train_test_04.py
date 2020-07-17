# PML train test 04
# 
# PYTHON MACHINE LEARNING
# =======================
# Train / Test
#
# Evaluate Your Model
# -------------------
# In Machine Learning we create models to predict the outcome of certain events, like in the previous chapter where we predicted the CO2 emission of a car when we knew the weight and engine size.
# To measure if the model is good enough, we can use a methos called Train/Test.
#
# What is Train/Test
# ------------------
# Train/Test is a method to measure the accuracy of a model.
# 
# It is called Train/Test because you split the data set into two sets: a training set and a testing set.
# 80% for training, and 20% for testing.
# You train the model using the training set.
# You test the model using the testing set.
# To train the model means to create the model.
# To test the model means to test the accuracy of the model.
#
# Start With a Data Set
# ---------------------
# Start with a data set you want to test.
# Our data set illustrates 100 customers in a shop, and their shopping habits.
#
# Example:

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

# Split into Train/Test
# ---------------------
# The training set should be a random selection of 80% of the original data.
# and the testing set should be the remaining 20%.

train_x = x[:80] # At this point all data is already randomized anyway... LOL
train_y = y[:80] # So we're just picking the first 80 of x (x[:80]) and y (y[:80]),
test_x = x[80:]  # and the last 20 of x and y (x[80:] and y[80:]).
test_y = y[80:]

# Fit the Data Set
# ----------------
# What does the data set look like? In the opinion of the author, the best fit would be a polynomial regression,
# so let us draw a line of polynomial regression.
#
# To draw a line through the data points, we use the plot() method of the matplotlib module.

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4)) # <-- this line generates the regression line of the training set
myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# Result:
#
# The result can back the suggestion of the data set fitting a polynomial regression, even though it would
# give us some weird results if we tried to predict values outside of the data set.
# Example: the line indicates that a customer spending 6 minutes in the shop would make a purchase worth 200.
#          That is probably a sign of overfitting.
