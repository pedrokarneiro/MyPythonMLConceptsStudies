# Multiple Regression
# ===================
# Multiple regression is like linear regression, but with more than one
# independent value, meaning that we try to predict a value based on two or more
# variables.
# 
# Consider the cars dataset (see cars.csv file).
# 
# We can predict the CO2 emission of a car based on the size of the engine, but
# with multiple regression we can throw in more variables, like the weight of
# the car, to make the prediction more accurate.
#
# How Does it Work?
# -----------------
# In Python we have modules that will do the work for us. Start by importing the
# Pandas module.
import pandas # Consider running "pip install pandas" on command line prompt first.
import math

# The Pandas module allows us to read csv files and return a DataFrame object.
df = pandas.read_csv("cars.csv")

# Then make a list of the independent values (the values that affect the other
# ones) and call this variable X (uppercase). Put the dependent values (the
# values that change when they are affected) in a variable called y.
X = df[['Weight', 'Volume']] # Weight and volume will affect the CO2 production.
y = df['CO2']                # CO2 production is affected by weight and volume of the car.

# Tip: It is common to name the list of independent values with a upper case X,
# and the list of dependent values with a lower case y.
# 
# We will use some methods from the sklearn module, so we will have to import
# that module as well.
from sklearn import linear_model

# From the sklearn module we will use the LinearRegression() method to create a
# linear regression object.
regr = linear_model.LinearRegression()

# The regr object will have a method called fit() that takes the independent and
# dependent values as parameters and fills the regression object with data that
# describes the relationship.
regr.fit(X, y) # The fit() method fills the regr object with data that describes the relationship.

# Now we have a regression object (regr) that is ready to predict CO2 values
# based on a car's weight and volume. For example, let's predict the CO2
# emission of a car where the weight is 2300g, and the volume is 1300ccm.
predictedCO2 = regr.predict([[2300, 1300]])
print("We have predicted that a car with 1.3 liter engine, and a weight of 2.3 kg, will release approximately " + str(round(predictedCO2[0], 2)) + " grams of CO2 for every kilometer it drives.")
# Note: I used predictedCO2[0] because the variable predictedCO2 is an ndarray and the (only) numeric element must be referenced.

# Coefficient
# -----------
# 
# The coefficient is a factor that describes the relationship with an unknown
# variable.
# Example: if x is a variable, then 2x is x two times. x is the unknown variable, and the number 2 is the coefficient.
# 
# In this case, we can ask for the coefficient value of weight against CO2, and for volume against CO2. The answer(s) we get tells us what would happen if we increase, or decrease, one of the independent values.
print(regr.coef_)



























