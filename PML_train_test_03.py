# PML train test 03
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

# Display the Testing Set
# -----------------------
# To make sure the testing set is not completely different, we will take a look at it as well.
#
# Example:

plt.scatter(test_x, test_y) # Switch between this line and the one of training set with the line plot in the "Fit the Data Set" section.
plt.show()                  # This one too.

# Result:
# The testing set also looks like the original data set.
