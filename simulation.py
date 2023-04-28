import networkx as nx
import random
from itertools import combinations, groupby
import time
import textwrap
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    return G


def _dedent_string(string):
    if string and string[0] == '\n':
        string = string[1:]
    return textwrap.dedent(string)


def trustValue(evidence, timeFunction):
    x = time.time() - evidence
    # print(x)
    timeFunc = timeFunction[0]
    xmin = timeFunction[1]
    xmax = timeFunction[2]

    assert xmin <= xmax
    if (x <= xmin):
        trustScore = 1
    elif (xmin < x <= xmax):
        # parse and evaluate time function: eval() does not need to be sanitized, administration transaction family input only by administrators
        trustScore = eval(_dedent_string(timeFunc))
    else:
        trustScore = 0
    return trustScore


def findPath(G, nodes, prover, evidenceList, timeFunction, minReliability):
    queue = [0]
    vis = [False]*nodes
    vis[0] = True
    last = 0
    while len(queue) > 0:
        l = len(queue)
        while l > 0:
            l -= 1
            front = queue[0]
            adj = G.neighbors(front)
            for v in adj:
                if vis[v]:
                    continue
                if v == prover:
                    if v not in evidenceList:
                        return False, v
                    value = trustValue(evidenceList[v], timeFunction)
                    if value >= minReliability:
                        return True, None
                    else:
                        return False, v
                if v not in evidenceList:
                    continue
                else:
                    value = trustValue(evidenceList[v], timeFunction)
                if value < minReliability:
                    last = v
                    continue
                vis[v] = True
                queue.append(v)
            queue.pop(0)
    return False, last


nodes = [100, 200, 300, 400, 500, 700, 800, 1000, 2500, 5000, 7500, 10000]
seed = random.randint(1, 10)
probability = 0.1

simRepetitions = 1
simulationDuration = 1200
rate = 5
securityParameter = 6
minReliability = 0.80
timeFunction = ['-0.0006666667*x + 1.2', 300, 600]
trustQueryHits = 0
trustQueryMisses = 0
hitPercentages = []

for node in nodes:
    hitPer = 0
    # for i in range (0,10):
    G = gnp_random_connected_graph(node, probability)
    evidence = [None] * node
    evidenceList = {}
    trustQueryRate = node / rate
    for j in range(0, simRepetitions):
        simulationStart = time.time()
        lastSecond = time.time()
        secondIterations = 0
        while time.time() < (simulationStart + simulationDuration):
            currentSecond = time.time()
            if ((currentSecond - lastSecond) < 1) and (secondIterations < trustQueryRate):
                secondIterations += 1
                prover = random.randint(0, node - 1)
                pathFound, last = findPath(
                    G, node, prover, evidenceList, timeFunction, minReliability)
                if pathFound:
                    trustQueryHits += 1
                else:
                    trustQueryMisses += 1
                    evidenceList[last] = time.time()

            elif (currentSecond - lastSecond) >= 1:
                lastSecond = currentSecond
                secondIterations = 0
            else:
                currentSecond = time.time()
                sleepTime = (1 - (currentSecond - lastSecond))
                time.sleep(sleepTime)
        # print("Report -----------------------------------------------------------------")
        # print("Number of Nodes:", node)
        # print("Security Parameter:", securityParameter)
        # print("Minimal Reliability:", minReliability)
        # print("Time Function:", timeFunction)
        # print("Simulation Duration:", simulationDuration)
        # print("Number of TrustQueries:", (trustQueryHits + trustQueryMisses))
        # print("Actual Trust Query Rate:", (trustQueryHits +
        #     trustQueryMisses) / (time.time() - simulationStart))
        # print("Hits:", trustQueryHits)
        # print("Misses:", trustQueryMisses)
        # print("HitPercentage:", (trustQueryHits /
        #     (trustQueryHits + trustQueryMisses)) * 100)
        hitPer = (trustQueryHits / (trustQueryHits + trustQueryMisses)) * 100
        # print("Simulation Duration:", (time.time() - simulationStart))
        # print("Report -----------------------------------------------------------------")
        trustQueryHits = 0
        trustQueryMisses = 0
    hitPercentages.append(hitPer)
print(hitPercentages)

fig, ax = plt.subplots()
x_smooth = np.linspace(min(nodes), max(nodes), 200)
y1_smooth = interp1d(nodes, hitPercentages, kind='cubic')(x_smooth)

ax.plot(x_smooth, y1_smooth, 'b-', label='FYP')
ax.set_xlabel('x-axis values')
ax.set_ylabel('y-axis values')
ax.set_title('Smooth Line Graph for Arrays')
ax.legend()
plt.show()
