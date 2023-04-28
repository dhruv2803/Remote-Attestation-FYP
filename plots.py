import numpy as np
from scipy.interpolate import interp1d

import matplotlib.pyplot as plt

x_values = [100, 200, 300, 400, 500, 700, 2500, 5000]
# x_values = [100, 200, 300, 400, 500, 700, 800, 1000, 2500, 5000, 7500, 10000]
y1_values = [98.10878661087867, 98.61924686192468, 98.80402472891693, 98.91122278056952, 98.95641240569991, 99.0092304003836,
             98.49105486118404, 97.78844029029456]
y2_values = [99.1638795986622, 99.16317991631799, 99.1638795986622, 99.16317991631799, 99.1638795986622,
             99.1638795986622, 99.16317991631799, 99.16317991631799]
y3_values = [48.0550918196995, 31.614452798663322, 23.425153032832498, 18.543545903133545, 12.54350736278447,
             8.042372881355933, 3.137875563195944, 1.7422071771196292]

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
