import matplotlib.pyplot as plt

nodes = [100, 200, 300, 400, 500, 700, 800, 1000, 2500, 5000, 7500, 10000]
max_overhead = [6, 7, 12, 12, 15, 20, 18, 34, 63, 132, 208, 234]
avg_overhead = [0.96, 0.98, 0.9866666666666667, 0.99, 0.992, 0.9942857142857143, 0.995, 0.996, 0.9984, 0.9992, 0.9994666666666666, 0.9996]
fig, ax = plt.subplots()

ax.plot(nodes, max_overhead, 'b-', label='FYP')
ax.plot(nodes, nodes, 'r-', label='scraps')
ax.set_xlabel('No of devices')
ax.set_ylabel('Overhead')
ax.set_title('Maximum overhead of node in network')
ax.legend()


# ax.plot(nodes, avg_overhead, 'r-', label='FYP')

# ax.set_xlabel('No of devices')
# ax.set_ylabel('Average Overhead')
# ax.set_title('Average overhead of node in network')
# ax.legend()

plt.show()
