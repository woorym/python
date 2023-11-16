from collections import deque
import sys

cnt = 0
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [
    []
    for _ in range(n + 1)
]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)
def bfs():
    global cnt
    queue = deque()
    
    for i in range(1, n + 1):
        flag = 0
        if not visited[i]:
            visited[i] = True
            queue.append(i)

        while queue:
            x = queue.popleft()

            for j in graph[x]:
                if not visited[j]:
                    queue.append(j)
                    visited[j] = True
            flag = 1
        if flag == 1:
            cnt += 1
    # return cnt

bfs()
# print(visited)

print(cnt)