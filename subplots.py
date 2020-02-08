# Source: http://queirozf.com/entries/matplotlib-pyplot-by-example
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 100, 50)
y = np.random.uniform(low=0, high=10, size=50)

print("x:", x)
print("y:", y)

# passing 2,2 as parameters indicates that you will
# get 4 subplots (2 rows and 2 columns)
fig, axes = plt.subplots(2,2)

# just plot things on each individual axes
# ========================================
# + 0 1
# 0 x .
# 1 . .
#axes[0][0].scatter(x,y,c='red',marker='+')
axes[0][0].scatter(x, y, color="red", marker="+")
# + 0 1
# 0 . x
# 1 . .
axes[0][1].bar(x, y)
# + 0 1
# 0 . .
# 1 x .
axes[1][0].scatter(x, y, marker="x")
# + 0 1
# 0 . .
# 1 . x
axes[1][1].barh(x, y)
plt.show()

