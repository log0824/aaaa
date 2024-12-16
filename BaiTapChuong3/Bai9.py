from collections import deque

def flood_fill_bfs(image, sr, sc, newColor):
    queue = deque()
    queue.append((sr, sc))

    r, c = len(image), len(image[0])
    startColor = image[sr][sc]

    if newColor == startColor:
        return image

    while queue:
        x, y = queue.popleft()
        if image[x][y] == startColor:
            image[x][y] = newColor

            if x + 1 < r:
                queue.append((x+1,y))
            if x - 1 >= 0:
                queue.append((x - 1, y))
            if y + 1 < c:
                queue.append((x, y + 1))
            if y - 1 >= 0:
                queue.append((x, y - 1))

    return image


image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr, sc = 1, 1
newColor = 2
result = flood_fill_bfs(image, sr, sc, newColor)
print(result)


