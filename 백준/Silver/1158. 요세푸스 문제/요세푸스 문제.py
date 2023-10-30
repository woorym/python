from collections import deque
import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))
dq = deque([i for i in range(1, n + 1)])
result = []

while len(dq) > m:
    result.append(dq[m - 1])
    if len(dq) > m:
        del dq[m - 1]

    for _ in range(m - 1):
        dq.append(dq.popleft())

result.append(dq[m - 1])
del dq[m - 1]

while len(dq) > 0:
    i = m % len(dq) - 1
    result.append(dq[i])
    del dq[i]

    for _ in range(i):
        dq.append(dq.popleft())

string ="<" + ', '.join(list(map(str, result))) + ">"

print(string)