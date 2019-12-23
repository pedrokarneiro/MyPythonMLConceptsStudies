# Mean - The average value of a group of numbers
# Median - The mid point value of a group of numbers
# Mode - The the most common value in a group of numbers
# 
# [99,86,87,88,111,86,103,87,94,78,77,85,86]
# 
# 077
# 078
# 085
# 086086086
# 087087
# 088
# 094
# 099
# 103
# 111
#
########
# Mode #
########
# To find the Mode (the number that appears the most):

from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
my_mode = stats.mode(speed)

print('my_mode: ' + my_mode)
print('my_mode.mode: ' + my_mode.mode)
print('my_mode.count: ' + my_mode.count)

# Results:
# C:\My Path>python mode.py
# my_mode: ModeResult(mode=array([86]), count=array([3]))
# my_mode.mode: [86]
# my_mode.count: [3]
