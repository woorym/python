import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])
result = []

n, k = list(map(int, input().split()))

for i in range(1, n + 1):
    queue.append(i)

while len(queue) != 0:
    for _ in range(k - 1):
        queue.append(queue[0])
        queue.popleft()
    
    result.append(queue[0])
    queue.popleft()


result1 = ", ".join(map(str, result))

print("<", end = "")
print(result1, end = "")
print(">")


