import numpy as np
from scipy.interpolate import interp1d

import matplotlib.pyplot as plt

x_values = [100, 200, 300, 400, 500, 700, 2500, 5000, 7500, 10000]

y1_values = [2.0, 2.75, 3.166666666666667, 5.125, 5.5, 6.571428571428571, 9.080000000000002, 8.75, 9.080000000000002, 5.999803441194361]
y2_values = [12.5, 7.75, 9.166666666666668, 10.125, 8.2, 8.999999999999998, 9.14, 9.23, 9.426666666666666, 9.35]
y3_values = [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

fig, ax = plt.subplots()

# Generate a range of x-axis values with more data points
# x_smooth = np.linspace(min(x_values), max(x_values), 200)

# Interpolate the y-axis values between the data points
# y1_smooth = interp1d(x_values, y1_values, kind='cubic')(x_smooth)
# y2_smooth = interp1d(x_values, y2_values, kind='cubic')(x_smooth)
# y3_smooth = interp1d(x_values, y3_values, kind='cubic')(x_smooth)

# Plot the smooth lines
ax.plot(x_values, y1_values, 'b-', label='FYP')
ax.plot(x_values, y2_values, 'r-', label='scraps')
ax.plot(x_values, y3_values, 'g-', label='legiot')

ax.set_xlabel('Nodes')
ax.set_ylabel('Hit Percentage')
ax.set_title('Hit percentage comparison')
ax.legend()

plt.show()
