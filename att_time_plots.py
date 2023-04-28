import matplotlib.pyplot as plt

nodes = [100, 200, 300, 400, 500, 700, 800, 1000]
fypAttTime = [4600.0, 4300.0, 4000.0, 4000.0, 4000.0, 4000.0, 4000.0, 4000.0]
scrapsAttTime = [1000, 2000, 3000, 4000, 5000, 7000, 8000, 10000]
fig, ax = plt.subplots()

ax.plot(nodes, fypAttTime, 'b-', label='FYP')
ax.plot(nodes, scrapsAttTime, 'r-', label='scraps')
ax.set_xlabel('No of devices')
ax.set_ylabel('Estimate Attestation Time')
ax.set_title('Estimate Attestation Time comparison')
ax.legend()


# ax.plot(nodes, avg_overhead, 'r-', label='FYP')

# ax.set_xlabel('No of devices')
# ax.set_ylabel('Average Overhead')
# ax.set_title('Average overhead of node in network')
# ax.legend()

plt.show()
