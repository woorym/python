from collections import deque
import sys

input = sys.stdin.readline

cnt = 0
n, m = map(int, input().split())

visited = [0] * (100001)
def bfs():
    global cnt

    queue = deque()
    queue.append(n)

    while queue:        
        num = queue.popleft()

        if num == m:
            print(visited[num])
            break
        
        for j in (num - 1, num + 1, num * 2):
            if j >= 0 and j < 100001 and not visited[j]:
                visited[j] = visited[num] + 1
                queue.append(j)

bfs()

# print(visited)