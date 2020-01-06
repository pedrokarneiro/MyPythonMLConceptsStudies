# Polynomial Regression
# =====================
# If your data points clearly will not fit a linear regression (a straight line
# through all data points), it might be ideal for polynomial regression.
# 
# Polynomial regression, like linear regression, uses the relationship between
# the variables x and y to find the best way to draw a line through the data points.
# 
# How Does it Work?
# -----------------
# Python has methods for finding a relationship between data-points and to draw
# a line of polynomial regression. We will see how to use these methods instead
# of going through the mathematic formula for now.
# 
# In the example below, we have registered 18 cars as they were passing a
# certain tollbooth. We have registered the car's speed, and the time of day
# (hour) the passing occurred. The x-axis represents the hours of the day and
# the y-axis represents the speed.

import numpy                        # Import numpy and sklearn then draw the line of Polynomial Regression.
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

hour_array = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
speed_array = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel_1 = numpy.poly1d(numpy.polyfit(hour_array, speed_array, 1)) # Degree of the fitting polynomial 1 for linear regression
myline_1 = numpy.linspace(1, 22, 100)                               # Then specify how the line will display, we start at position 2, and end at position 22.
mymodel_2 = numpy.poly1d(numpy.polyfit(hour_array, speed_array, 2)) # Degree of the fitting polynomial 2 for a single curve
myline_2 = numpy.linspace(1, 23, 100)                               # If the end at position raises to 25 (if the domain was not closed to 24 h), different results may arrise.
mymodel_3 = numpy.poly1d(numpy.polyfit(hour_array, speed_array, 3)) # Degree of the fitting polynomial 3, a curve...
myline_3 = numpy.linspace(1, 23, 100)                               # For example, this one would suggest a future negative slope...
mymodel_4 = numpy.poly1d(numpy.polyfit(hour_array, speed_array, 4)) # Degree of the fitting polynomial 4, tighter...
myline_4 = numpy.linspace(1, 23, 100)                               # And this, a future positive slope.
# mymodel_5 = numpy.poly1d(numpy.polyfit(hour_array, speed_array, 5)) # Degree of the fitting polynomial 5, tighter...
# myline_5 = numpy.linspace(1, 23, 100)                               # Then specify how the line will display, we start at position 2, and end at position 22.
# mymodel_6 = numpy.poly1d(numpy.polyfit(hour_array, speed_array, 6)) # Degree of the fitting polynomial 6, tighter...
# myline_6 = numpy.linspace(1, 23, 100)                               # Then specify how the line will display, we start at position 2, and end at position 22.
mymodel_9 = numpy.poly1d(numpy.polyfit(hour_array, speed_array, 9)) # Degree of the fitting polynomial 7, tighter...
myline_9 = numpy.linspace(1, 23, 100)                               # Then specify how the line will display, we start at position 2, and end at position 22.


# R-Squared
# ---------
# It is important to know how well the relationship between the values of the x-
# and y-axis is, if there are no relationship the polynomial regression can not
# be used to predict anything.
# 
# The relationship is measured with a value called the r-squared which value
# ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
# 
# Python and the Sklearn module will have computed this value for you, all you
# have to do is feed it with the x and y arrays.
#
# How well does my data fit in a polynomial regression?
# 
# The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

r2_1 = r2_score(speed_array, mymodel_1(hour_array))
r2_2 = r2_score(speed_array, mymodel_2(hour_array))
r2_3 = r2_score(speed_array, mymodel_3(hour_array))
r2_4 = r2_score(speed_array, mymodel_4(hour_array))
r2_9 = r2_score(speed_array, mymodel_9(hour_array))

def get_r2_fit_message(r2):
    if (abs(r2) == 0): return 'Really bad fit.'
    elif (abs(r2) > 0) and (abs(r2) < 0.25): return 'Somehow bad fit.'
    elif (abs(r2) >= 0.25) and (abs(r2) < 0.5): return 'Not very bad fit.'
    elif (abs(r2) >= 0.5) and (abs(r2) < 0.75): return 'Not bad fit.'
    elif (abs(r2) >= 0.75) and (abs(r2) < 1): return 'Good fit.'
    elif (abs(r2) == 1): return 'Perfect fit.'

print('Degree 1 related R2: ' + str(r2_1) + '. ' + get_r2_fit_message(r2_1))
print('Degree 2 related R2: ' + str(r2_2) + '. ' + get_r2_fit_message(r2_2))
print('Degree 3 related R2: ' + str(r2_3) + '. ' + get_r2_fit_message(r2_3))
print('Degree 4 related R2: ' + str(r2_4) + '. ' + get_r2_fit_message(r2_4))
print('Degree 9 related R2: ' + str(r2_9) + '. ' + get_r2_fit_message(r2_9))

# Predict Future Values
# ---------------------
# Now we can use the information we have gathered to predict future values.
# Example: Let us try to predict the speed of a car that passes the tollbooth at around 17 P.M.
# To do so, we need the same mymodel array from the example above.
speed_1 = mymodel_1(23)
print('Speed of car at 23:00 (degree 1): ' + str(speed_1))
speed_2 = mymodel_2(23)
print('Speed of car at 23:00 (degree 2): ' + str(speed_2))
speed_3 = mymodel_3(23)
print('Speed of car at 23:00 (degree 3): ' + str(speed_3))
speed_4 = mymodel_4(23)
print('Speed of car at 23:00 (degree 4): ' + str(speed_4))
speed_9 = mymodel_9(23)
print('Speed of car at 23:00 (degree 4): ' + str(speed_9))

# Plot
plt.scatter(hour_array, speed_array, color='grey')                        # Prepares the scatterplot.
plt.plot(myline_1, mymodel_1(myline_1), color='gold', label='Degree 1')   # Prepares the regression line.
plt.plot(myline_2, mymodel_2(myline_2), color='orange', label='Degree 2')
plt.plot(myline_3, mymodel_3(myline_3), color='red')
plt.plot(myline_4, mymodel_4(myline_4), color='purple')
# plt.plot(myline_5, mymodel_5(myline_5), color='navy')
# plt.plot(myline_6, mymodel_6(myline_6), color='green')
plt.plot(myline_9, mymodel_9(myline_9), color='blue')
plt.text(15,70, 'Predicted speed at 23:00: ', color='black')
plt.text(15,67, 'Degree 1: ' + str(round(speed_1, 2)), color='gold')
plt.text(15,64, 'Degree 2: ' + str(round(speed_2, 2)), color='orange')
plt.text(15,61, 'Degree 3: ' + str(round(speed_3, 2)), color='red')
plt.text(15,58, 'Degree 4: ' + str(round(speed_4, 2)), color='purple')
plt.text(15,55, 'Degree 9: ' + str(round(speed_9, 2)), color='blue')
plt.show()                                                                   # Shows the plot.

