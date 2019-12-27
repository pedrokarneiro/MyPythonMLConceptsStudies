# LINEAR REGRESSION
# 
# Regression
# The term regression is used when you try to find the relationship between variables.
# In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.
# 
# Linear Regression
# Linear regression uses the relationship between the data-points to draw a straight line through all them.
# This line can be used to predict future values.
# 
# I have an example in a google spreadsheet in which the user can plug in the X and Y values and all the underlying calculations are done in order to reach R^2, the regression line, etc. The spreadsheet is very didactical if the user pays attention to the formulas in it.
# 
# The linear regression spreadsheet is found at https://tinyurl.com/rbq92sf
# Please let me know of any trouble you have when trying to use it. Send a message to pedrokarneiro.bsa@gmail.com.
#
# Also, I have implemented the same example using the R language. Even knowing that just like Python, R has packages and functions that deal with linear regression that would reduce the code to very few lines, I implemented each step of the calculation so it becomes easier to understand what goes behind the scenes when calculating a linear regression and the R^2.
#
# The basic concept proof linear regression R project is at https://github.com/pedrokarneiro/R_LeastSquareMethod_LR. Please feel free to fork, refactor and help me improve it. Let me know of any trouble you have when trying to use it. Send a message to pedrokarneiro.bsa@gmail.com.
# 
# Let's see if the data of the Car Age X Car Speed problem could be used in a linear regression:

import matplotlib.pyplot as plt            # Import the modules you need.
from scipy import stats                    # Remember to "pip install scipy" before.
# car_age = [5,7,8,7,2,17,2,9,4,11,12,9,6]               # Create the arrays that represents
# car_speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] #  the values of the x and y axis.
car_age = [5,7,8,7,2,17,2,9,4,11,12,9,6, 12, 12, 13, 14, 15, 16, 17, 17, 18, 19, 20]               # Create the arrays that represents
car_speed = [99,86,87,88,111,86,103,87,94,78,77,85,86, 120, 120, 130, 140, 150, 160, 170, 170, 180, 190, 200] #  the values of the x and y axis.
slope, intercept, r2, p, std_err = stats.linregress(car_age, car_speed) # Execute the method linregress() which returns
                                                                       # the important key values of the Linear Regression.
def myfunc(car_age):                 # This function uses the slope and intercept values to return a new value
  return slope * car_age + intercept # which represents where on the y-axis the corresponding x value will be placed.
                                     # In the spreadsheet model I called this as the yHat values, or simply
                                     # the regression line y parameters.
mymodel = list(map(myfunc, car_age)) # Run each value of the x array through the function.
                                     # This will result in a new array with new values for the y-axis
                                     # which make, in combination with the x values, the regression line coordinates.
plt.scatter(car_age, car_speed)  # Draw the original scatter plot.
plt.plot(car_age, mymodel)       # Draw the line of linear regression.
plt.show()                       # Display the diagram.
print(r2)    # It is important to know how well the relationship between the values of the x-axis and the values of the y-axis is.
            # If there are no relationship the linear regression can not be used to predict anything.
            # The relationship is measured with a value called the r-squared.
            # The r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.
if r2 < 0:
    print('Negative slope.')
elif r2 == 0:
    print('Neutral slope.')
elif r2 > 0:
    print('Positive slope.')
    
if (abs(r2) == 0): print('Really bad fit')
elif (abs(r2) > 0) and (abs(r2) < 0.25): print('Somehow bad fit')
elif (abs(r2) >= 0.25) and (abs(r2) < 0.5): print('Not very bad fit')
elif (abs(r2) >= 0.5) and (abs(r2) < 0.75): print('Not bad fit')
elif (abs(r2) >= 0.75) and (abs(r2) < 1): print('Good fit')
elif (abs(r2) == 1): print('Perfect fit')
