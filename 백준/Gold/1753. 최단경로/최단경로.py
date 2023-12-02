# 백준 1753번
import sys
import heapq
input = sys.stdin.readline

inf = sys.maxsize
node_num, e = map(int, input().split())
start_point = int(input())
d = [inf] * (node_num + 1)

heap = []
graph = [
    []
    for _ in range(node_num + 1)
]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

# print(graph)

def dijstra(start):
    d[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)

        if d[now] < weight:
            continue

        for w, next in graph[now]:
            next_weight = w + weight
            # print(f"{next}")
            if next_weight < d[next]:
                d[next] = next_weight
                heapq.heappush(heap, (next_weight, next))

dijstra(start_point)
# print(v)
for i in range(1, node_num + 1):
    # print(i)
    if d[i] == inf:
        print("INF")
    else:
        print(d[i])

# print(d)