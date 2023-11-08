from collections import deque
import sys

input = sys.stdin.readline

cnt = 1

computer_count = int(input())
connect_count = int(input())

graph = [
    []
    for _ in range(computer_count + 1)
]

visited = [0] * (computer_count + 1)

for _ in range(connect_count):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(num):
    global cnt

    queue = deque()
    queue.append(num)
    visited[num] = cnt

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = cnt

bfs(1)
# print(visited)
print(visited.count(1) - 1)
