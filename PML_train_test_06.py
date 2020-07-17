# PML train test 05
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
# What does the data set look like? In the opinion of the author, the best fit would be a polynomial regression, so let us draw a line of polynomial regression.

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4)) # <-- this line generates the regression line of the training set

# But what about the R-squared score? The R-squared score is a good indicator of how well my data set is fitting the model.
#
# R2
# --
# Remember R2, also known as R-squared?
# It measures the relationship between the x axis and the y axis, and the value ranges from 0 to 1, where 0 means no relationship, and 1 means totally related.
# The sklearn module has a method called r2_score() that will help us find this relationship.
# In this case we would like to measure the relationship between the minutes a customer stays in the shop and how much money they spend.
# Example:
# How well does my training data fit in a polynomial regression?

from sklearn.metrics import r2_score
r2_train =  r2_score(train_y, mymodel(train_x))
print(r2_train)

# Note 1: The result 0.799 shows that is a OK relationship.
# Note 2: I had to run this before being able to run: pip install -U scikit-learn scipy matplotlib

# Bring in the Testing Set
# ------------------------
# Now we have made a model that is OK, at least when it comes to training data.
# Now we want to test the model with the testing data as well, to see if it gives us the same result.
#
# Example:
# Let us find the R2 score when using testing data.

r2_test =  r2_score(test_y, mymodel(test_x))
print(r2_test)

# Note: The result 0.809 shows that the model fits the testing set as well, and we are confident that we can use the model to predict future values.
