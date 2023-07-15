import sys
from collections import deque

test_case = int(input())

for i in range(test_case):
    cmd = sys.stdin.readline().rstrip()
    length = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    reverse, front, back = 0, 0, len(queue)-1
    flag = 0
    if length == 0:
        queue = []
        front = 0
        back = 0

    for j in cmd:
        if j == 'R':
            reverse += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if reverse % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if reverse % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")