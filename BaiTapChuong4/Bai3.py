import heapq

def prim(graph, start):
    mst = []
    prev_node = None
    visited = set()
    heap = [(0, start)]

    while heap:
        weight, node = heapq.heappop(heap)

        if node not in visited:
            visited.add(node)

            if weight != 0:
                mst.append((prev_node, node, weight))
            
            for v, w in graph[node]:
                if v not in visited:
                    heapq.heappush(heap, (w, v))
                    prev_node = node

    return mst

graph = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)],
}

mst = prim(graph, 0)

print("Các cạnh trong MST:")
for edge in mst:
    print(edge)