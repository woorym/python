from collections import deque
# import sys

# input = sys.stdin.readline
dist, check = 1, 0
n, m = map(int, input().split())

graph = [
    list(input().strip())
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]
    # 동 남 서 북
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    # global dist, check
    queue = deque()
    # result = []
    
    queue.append([0, 0])
    visited[0][0] = True
        
    while queue:
        check = 0
        nx, ny = queue.popleft()
        for dx, dy in zip(dxs, dys):
            ch_x, ch_y = nx + dx, ny + dy   
            if in_range(ch_x, ch_y) and not visited[ch_x][ch_y] and graph[ch_x][ch_y] == '1':
                queue.append([ch_x, ch_y])
                graph[ch_x][ch_y] = int(graph[nx][ny]) + 1
                visited[ch_x][ch_y] = True
                # continue
            # check += 1
        # if check == 4:
            # result.append([nx, ny, distance])
    # return result

result = bfs()
# print(result)
# print(graph)

list_dist = []

# for x, y, dis in result:
    # if x == (n - 1) and y == (m - 1):
        # list_dist.append(dis)


# print(min(list_dist))
# print(n, m)
print(graph[n - 1][m - 1])