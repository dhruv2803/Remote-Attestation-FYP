import numpy as np
from scipy.interpolate import interp1d

import matplotlib.pyplot as plt

x_values = [100, 200, 500, 700, 1000, 5000, 10000]

y1_values = [0.0, 2.5, 7.000000000000001, 5.714285714285714, 4.5, 9.1, 6.001304631441617]
y2_values = [20.0, 15.0, 11.0, 12.142857142857142, 8.5, 9.0, 9.1]
y3_values = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

fig, ax = plt.subplots()

# Generate a range of x-axis values with more data points
x_smooth = np.linspace(min(x_values), max(x_values), 200)

# Interpolate the y-axis values between the data points
y1_smooth = interp1d(x_values, y1_values, kind='cubic')(x_smooth)
y2_smooth = interp1d(x_values, y2_values, kind='cubic')(x_smooth)
y3_smooth = interp1d(x_values, y3_values, kind='cubic')(x_smooth)

# Plot the smooth lines
ax.plot(x_smooth, y1_smooth, 'b-', label='FYP')
ax.plot(x_smooth, y2_smooth, 'r-', label='scraps')
ax.plot(x_smooth, y3_smooth, 'g-', label='legiot')

ax.set_xlabel('x-axis values')
ax.set_ylabel('y-axis values')
ax.set_title('Smooth Line Graph for Arrays')
ax.legend()

plt.show()
