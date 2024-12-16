class DisjointSet():
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[u] += 1

def kruskal(graph, n):
    mst = []

    ds = DisjointSet(n)

    graph.sort(key=lambda edge: edge[2])

    for u, v, w in graph:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, w))
            ds.union(u, v)

    return mst

graph = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
]

n = 4

mst = kruskal(graph, n)

print("Các cạnh trong MST:")
for edge in mst:
    print(edge)