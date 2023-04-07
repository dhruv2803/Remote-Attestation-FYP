import matplotlib.pyplot as plt

nodes = [100, 200, 300, 400, 500, 700, 800, 1000, 2500, 5000, 7500, 10000]
max_overhead = [12,24,33,42,55,70,89,93,236,518,748,1015]
avg_overhead = [0.99,0.995,0.99666,0.9975,0.998,0.99857,0.99875,0.999,0.9996,0.9998,0.99986666,0.9999]
fig, ax = plt.subplots()

# ax.plot(nodes, max_overhead, 'b-', label='FYP')

# ax.set_xlabel('No of devices')
# ax.set_ylabel('Overhead')
# ax.set_title('Maximum overhead of node in network')
# ax.legend()


ax.plot(nodes, avg_overhead, 'r-', label='FYP')

ax.set_xlabel('No of devices')
ax.set_ylabel('Average Overhead')
ax.set_title('Average overhead of node in network')
ax.legend()

plt.show()
