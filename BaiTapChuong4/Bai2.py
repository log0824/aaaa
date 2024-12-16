graph = {
    2: [5, 8],   
    5: [2, 8],   
    8: [2, 5],  
    1: [5, 8],   
}
vertices = list(graph.keys())

vertices.sort(key=lambda x:len(graph[x]), reverse=True)

def greedy_coloring_improved(graph):
    n = len(graph)
    color = {v : -1 for v in graph}

    color[vertices[0]] = 0

    for u in vertices[1:]:
        used_color = [False]*len(graph)

        for v in graph[u]:
            if color[v] != -1:
                used_color[color[v]] = True

        for c in range(len(graph)):
            if not used_color[c]:
                color[u] = c
                break

    return color
colors = greedy_coloring_improved(graph)
print("Màu sắc của các đỉnh:", colors)