import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])


n = int(input())

for i in range(1, n + 1):
    queue.append(i)

for _ in range(n - 1):
    queue.popleft()

    queue.append(queue[0])
    queue.popleft()

print(queue[0])