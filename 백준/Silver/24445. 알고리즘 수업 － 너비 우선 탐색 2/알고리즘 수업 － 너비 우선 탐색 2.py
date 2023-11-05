from collections import deque
import sys

cnt = 1
n, m, r = map(int, input().split())

graph = [
    []
    for _ in range(n + 1)
]

visited = [0] * (n + 1)

# print(graph)
for _ in range(m):
    line_info = list(map(int, input().split()))

    graph[line_info[0]].append(line_info[1])
    graph[line_info[1]].append(line_info[0])

    # print(graph)
    
for i in range(n + 1):
    graph[i].sort(reverse=True)

# print(graph)

def bfs(r):
    global cnt
    queue = deque()
    queue.append(r)
    visited[r] = cnt

    while queue:
        num = queue.popleft()

        for i in graph[num]:
            if visited[i] == 0:
                cnt += 1 
                visited[i] = cnt
                queue.append(i)
        
bfs(r)

for i in range(1, n + 1):
    print(visited[i])

# print(visited)