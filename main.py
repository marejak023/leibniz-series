#Author: marejak023
#Contact: marejak023@gmail.com, marejak023.wz.cz
#Date: 06/02/2021

import matplotlib.pyplot as plt
import numpy as np
import math

#code for computing Leibniz series
k = 1 # denominator
s = 0 # sum

# x and y array for storing plot values
y = np.array([])
x = np.array([])
PI_CONST_LINE = np.array([]) # pi contstant for y reference value (set for 15f points from math package)

sum_range = int(input("\nEnter a range: ")) # range for the series

for i in range(sum_range):
    # even numbers have + sign
    if i % 2 == 0:
        s += 4/k
    else: # changes + to - sign
        s -= 4/k
    k += 2
    y = np.append(y, s) # adds current value of sum of the series to the y array
    PI_CONST_LINE = np.append(PI_CONST_LINE, math.pi) # append math.pi values to PI_CONST_LINE array, so pi y reference value is for every n (sum_range) = math.pi

# stores value in x array (sum_range = n [number of steps])
for i in range(sum_range):
    x = np.append(x, i)

error = ((s-math.pi)/math.pi)*100 # Percentage value of error

# printing out computed values
print("\nApproximate value of pi using Liebniz series is: ", "{:.15f}".format(s))
print("Real value using math python constant math.pi is: ", math.pi)
print("Value of error in % is: ", abs(error), "%")
print("\nApproximate value is limited to 15 float digits, so it matches the internal float value of math.pi")

# making plot
# titles & labels
plt.figure().canvas.set_window_title("Pi approximation using Leibniz series")
plt.title(r"$\pi$ approximation using Leibniz series $\frac{\pi}{4}=\sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1}$", y = 1.05) # y is for title positioning on y axis
plt.xlabel(r"n", fontsize = 20) # r is for using mathmode ($$ for entering mathmode, same as LaTeX notation)
plt.ylabel(r"$S_n$", fontsize = 20)

plt.plot(x, y, marker = 'X', mec = "#0085E7", mfc = "#FFF", c = "#0085E7", ls = '--') # plots Leibniz series, mec = marker edge color, mfc = marker face color c = linecolor, ls = linestyle
plt.plot(x, PI_CONST_LINE, ls = '-.', c = "#000") # plots constant line with y value = pi (from math.pi, 15f points) & x value = n (sum_range)
plt.grid(linestyle = '--')
plt.show() # display plot