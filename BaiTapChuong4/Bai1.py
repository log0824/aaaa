def greedy_coloring(graph):
    n = len(graph)

    color = {v : -1 for v in graph}

    for u in graph:
        used_colors = set()

        for v in graph[u]:
            if color[v] != -1:
                used_colors.add(color[v])
        
        color_u = 0
        while color_u in used_colors:
            color_u += 1
        
        color[u] = color_u

    return color

matrix = [
    [2, 3],
    [1, 2],
    [1, 3],
    [3, 1],
    [4, 2]
]

graph = {}

for eage in matrix:
    u, v = eage

    if u not in graph:
        graph[u] = []
    graph[u].append(v)

    if v not in graph:
        graph[v] = []
    graph[v].append(u)

colors = greedy_coloring(graph)
print("Màu sắc của các đỉnh:", colors)