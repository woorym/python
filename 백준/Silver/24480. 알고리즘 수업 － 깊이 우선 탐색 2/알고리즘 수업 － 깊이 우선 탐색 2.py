from collections import deque
import sys

# sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline
cnt = 1

n, m, r = map(int, input().split())

graph = [
    []
    for _ in range(n + 1)
]

visited = [0] * (n + 1)

node_cnt = [0 for _ in range(n + 1)]


for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


# print(graph)
for i in range(n + 1):
    graph[i].sort()

# print(graph)
# print(stack)

# def dfs(r):
    # global cnt
    # stack = [r]
    # print(visited)
    # visited[r] = cnt
        # num = stack[-1] 
        # print(stack)
    # for i in graph[r]:
        # if visited[i] == 0:
            # cnt += 1
            # visited[i] = cnt
                 
            # dfs(i)
stack = deque()
stack.append(r)

while stack:
    node = stack.pop()
    visited[node] = cnt

    if node_cnt[node] == 0:
        node_cnt[node] = cnt
        cnt += 1

    for next_node in graph[node]:
        if visited[next_node] == 0:
            stack.append(next_node)
            # cnt += 1


# dfs(r)

# print(graph)
for i in range(1, n + 1):
    print(node_cnt[i])