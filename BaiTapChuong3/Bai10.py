import heapq 

def the_tich(hcn):

    heap = []

    if not hcn or len(hcn) < 3 or len(hcn[0]) < 3:
        return 0
    
    n, m  = len(hcn), len(hcn[0])
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                heapq.heappush(heap, (hcn[i][j], i, j))
                visited[i][j] = True
    
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    total_water = 0

    while heap:
        h, x, y = heapq.heappop(heap)
        for dx, dy in d:
            nx, ny = dx+x, dy+y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                water = max(0, h - hcn[nx][ny])
                total_water += water
                heapq.heappush(heap, (max(h, hcn[nx][ny]), nx, ny))
                visited[nx][ny] = True
    
    return total_water



heightMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]
print(the_tich(heightMap))