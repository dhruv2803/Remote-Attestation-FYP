import networkx as nx
import random
from itertools import combinations, groupby

FYP_CONST = 1000
SCRAPS_CONST = 10

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


def generateMST(G,nodes):
    mst = nx.Graph()
    mst.add_nodes_from(range(nodes))
    queue = [0]
    vis = [False]*nodes
    vis[0] = True
    while len(queue) > 0:
        l = len(queue)
        while l > 0:
            l -= 1
            front = queue[0]
            adj = G.neighbors(front)
            for v in adj:
                if vis[v]:
                    continue
                else:
                    vis[v] = True
                    mst.add_edge(front, v)
                    queue.append(v)
            queue.pop(0)
    
    return mst

def calculateHeight(G,nodes):
    height = 0
    queue = [0]
    vis = [False]*nodes
    vis[0] = True
    while len(queue) > 0:
        height+=1
        l = len(queue)
        while l > 0:
            l -= 1
            front = queue[0]
            adj = G.neighbors(front)
            for v in adj:
                if vis[v]:
                    continue
                else:
                    vis[v] = True
                    mst.add_edge(front, v)
                    queue.append(v)
            queue.pop(0)
    return height


nodes = [100, 200, 300, 400, 500, 700, 800, 1000, 2500, 5000, 7500, 10000]
seed = random.randint(1, 10)
probability = 0.1
fypAttTime = []
scrapsAttTime = []
for tnode in nodes:
    node = int(tnode / 4)
    height = 0
    for i in range (0,10):
        G = gnp_random_connected_graph(node, probability)

        mst = generateMST(G,node)

        height += calculateHeight(mst,node)

    fypAttTime.append((height/10)*FYP_CONST)
    scrapsAttTime.append(tnode*SCRAPS_CONST)
print(fypAttTime)
print(scrapsAttTime)
    
