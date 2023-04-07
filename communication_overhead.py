import networkx as nx
import random
from itertools import combinations, groupby

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

def calculateOverheads(G,nodes):
    overheads = []
    queue = [0]
    vis = [False]*nodes
    vis[0] = True
    while len(queue) > 0:
        front = queue[0]
        adj = G.neighbors(front)
        cnt = 0
        for v in adj:
            if vis[v]:
                continue
            else:
                vis[v] = True
                queue.append(v)
                cnt+=1
        overheads.append(cnt)
        queue.pop(0)
    return overheads

def statistics(array):
    mn = min(array)
    mx = max(array)
    sum = 0
    for ele in array:
        sum += ele
    mean = sum / len(array)

    array.sort()

    if len(array)%2 == 1:
        median = array[len(array)//2]
    else:
        median = (array[len(array)//2 - 1] + array[len(array)//2]) / 2
    return mn,mx,mean,median

nodes = [100, 200, 300, 400, 500, 700, 800, 1000, 2500, 5000, 7500, 10000]
seed = random.randint(1, 10)
probability = 0.1

for node in nodes:
    G = gnp_random_connected_graph(node, probability)

    mst = generateMST(G,node)

    overheads = calculateOverheads(mst,node)

    mn,mx,mean,median = statistics(overheads)

    print(mn,mx,mean,median)
    
