from collections import deque
import sys

cnt_dfs = 1
cnt_bfs = 1
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph_dfs = [
    []
    for _ in range(n + 1)
]
graph_bfs = [
    []
    for _ in range(n + 1)
]

visited_dfs = [0] * (n + 1)
visited_bfs = [0] * (n + 1)
node_cnt = [0] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph_dfs[x].append(y)
    graph_dfs[y].append(x)

    graph_bfs[x].append(y)
    graph_bfs[y].append(x)

for line in graph_dfs:
    line.sort(reverse=True)

for line in graph_bfs:
    line.sort()

# print(graph)

def dfs(v):
    global cnt_dfs
    stack = deque()
    stack.append(v)
    visited_dfs[v] = cnt_dfs
    
    while stack:
        v = stack.pop()
        if node_cnt[v] == 0:
            node_cnt[v] = cnt_dfs
            cnt_dfs += 1

        for i in graph_dfs[v]:
            if node_cnt[i] == 0:
                visited_dfs[i] = cnt_dfs
                stack.append(i)     

def bfs(v):
    global cnt_bfs
    queue = deque()
    queue.append(v)
    visited_bfs[v] = cnt_bfs

    while queue:
        node = queue.popleft()
        for i in graph_bfs[node]:
            if visited_bfs[i] == 0:
                cnt_bfs += 1
                visited_bfs[i] = cnt_bfs
                queue.append(i)



bfs(r)
dfs(r)    

answer_dfs = []
answer_bfs = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if visited_bfs[j] == i:
            answer_bfs.append(j)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if node_cnt[j] == i:
            answer_dfs.append(j)

# print(node_cnt)
# print(f'visited_dfs : {node_cnt}')
# print(f'answer_dfs : {answer_dfs}')
# print(f'answer_bfs : {answer_bfs}')
# 
for i in answer_dfs:
    print(i, end = " ")
print()
for j in answer_bfs:
    print(j, end = " ")
