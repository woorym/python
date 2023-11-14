from collections import deque
import sys

input = sys.stdin.readline

# test_case = int(input())
# m, n, k = map(int, input().split())

# graph = [
    # [0] * m
    # for _ in range(n)
# ]
# visited = [
#     [False] * m
#     for _ in range(n)
# ]

# for _ in range(k):
#     x, y = map(int, input().split())
#     graph[y][x] = 1

    #동 남 서 북
dxs = [0, 1, 0, -1] 
dys = [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs(m, n, k, cnt):
    graph = [
        [0] * m
        for _ in range(n)
        ]
    
    visited = [
        [False] * m
        for _ in range(n)
        ]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    queue = deque()

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                queue.append([i, j])
                visited[i][j] = True
                cnt += 1
                # print(f"i, j : {i} {j}")
                # print(cnt)
    
            while queue:
                nx, ny = queue.popleft()
                # print(f"first {cnt} : {nx}, {ny}")
                for dx, dy in zip(dxs, dys):
                    check_x, check_y = nx + dx, ny + dy
                    # print(f"{cnt} : {check_x}, {check_y}")
                    # print(f"{cnt} : {check_x}, {check_y}, {visited[check_x][check_y]}")
        
                    if in_range(check_x, check_y) and not visited[check_x][check_y] and graph[check_x][check_y] == 1:
                        visited[check_x][check_y] = True
                        queue.append([check_x, check_y])
    return cnt
    
test_case = int(input())

for _ in range(test_case):
    cnt = 0
    m, n, k = map(int, input().split())

    result = bfs(m, n, k, cnt)
    print(result)
# for i in visited:
    # print(i)
                


        

# print(graph)
# for i in graph:
    # print(i)